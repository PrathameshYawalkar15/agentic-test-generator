"""Main orchestration for test generation and execution"""

import json
from typing import Dict, List, Optional

# NOTE: these are absolute imports rooted at the project (src is a package).
# Every doc/workflow in this project invokes the orchestrator as
# `from src.orchestrator import TestOrchestrator` run from the project
# root, which puts the project root (not src/) on sys.path. Plain
# `from requirement_reader import ...` style imports fail under that
# invocation with ModuleNotFoundError -- these must be `src.`-qualified.
from src.requirement_reader import RequirementReader
from src.test_condition_generator import TestConditionGenerator
from src.gherkin_generator import GherkinGenerator
from src.llm_client import OllamaClient


class TestOrchestrator:
    """Orchestrate the entire test generation pipeline"""

    def __init__(self):
        self.req_reader = RequirementReader()
        self.cond_generator = TestConditionGenerator()
        self.gherkin_gen = GherkinGenerator()
        self.llm_client = OllamaClient()

    def process_single_requirement(
        self,
        filename: str,
        condition_types: Optional[List[str]] = None,
    ) -> Dict:
        """Process a single requirement file.

        condition_types: which condition types (threshold, boundary,
        timing, state, error, recovery) to generate. None means all of
        them -- this keeps automated/CI runs working without any prompt.
        """
        print(f"\n{'='*60}")
        print(f"Processing: {filename}")
        print(f"{'='*60}")

        try:
            # Step 1: Read requirement
            print("1️⃣  Reading requirement...")
            content = self.req_reader.read_requirement_file(filename)
            parsed = self.req_reader.parse_requirement(content)

            # Validate
            validation = self.req_reader.validate_requirement(parsed)
            if not validation["valid"]:
                print(f"❌ Validation failed: {validation['issues']}")
                return {"success": False, "errors": validation["issues"]}

            # Step 2: Generate test conditions
            print("2️⃣  Generating test conditions...")
            conditions = self.cond_generator.generate_conditions(
                parsed.get("features", []),
                condition_types,
            )
            conditions = self.cond_generator.prioritize_conditions(conditions)
            print(f"✅ Generated {len(conditions)} test conditions")

            # Step 3: Generate Gherkin
            print("3️⃣  Generating Gherkin feature file...")
            feature_content = self.gherkin_gen.generate_feature_file(
                parsed.get("title", filename),
                conditions
            )

            # Step 4: Save feature file
            print("4️⃣  Saving feature file...")
            feature_file = filename.replace('.md', '').replace('.txt', '')
            filepath = self.gherkin_gen.save_feature_file(
                feature_file,
                feature_content
            )

            # Step 5: Validate Gherkin
            print("5️⃣  Validating Gherkin syntax...")
            gherkin_validation = self.gherkin_gen.validate_gherkin(feature_content)
            print(f"✅ {gherkin_validation['scenario_count']} scenarios generated")
            if not gherkin_validation["valid"]:
                print(f"⚠️  Gherkin validation issues: {gherkin_validation['issues']}")

            return {
                "success": True,
                "filename": filename,
                "feature_file": filepath,
                "scenarios": gherkin_validation["scenario_count"],
                "conditions": len(conditions)
            }

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
            return {"success": False, "error": str(e)}

    def process_all_requirements(
        self,
        condition_types: Optional[List[str]] = None,
    ) -> Dict:
        """Process all requirement files.

        condition_types: which condition types to generate for every
        requirement in this run (None = all types). Pass this through
        from wherever the selection was made -- a CLI menu for local/
        interactive use, or a workflow_dispatch input in CI.
        """
        print("\n" + "="*60)
        print("🚀 AGENTIC TEST GENERATOR - PROCESSING PIPELINE")
        print("="*60)
        if condition_types:
            print(f"Condition types: {', '.join(condition_types)}")
        else:
            print("Condition types: all")

        requirements = self.req_reader.read_all_requirements()

        if not requirements:
            print("⚠️  No requirements found")
            return {"success": False, "message": "No requirements found"}

        results = []
        for filename in requirements:
            result = self.process_single_requirement(filename, condition_types)
            results.append(result)

        # Summary
        successful = sum(1 for r in results if r.get("success"))
        total_scenarios = sum(r.get("scenarios", 0) for r in results if r.get("success"))

        print(f"\n" + "="*60)
        print(f"📊 SUMMARY")
        print(f"{'='*60}")
        print(f"✅ Successfully processed: {successful}/{len(requirements)}")
        print(f"📝 Total scenarios generated: {total_scenarios}")

        return {
            "success": True,
            "processed": successful,
            "total": len(requirements),
            "total_scenarios": total_scenarios,
            "results": results
        }


# Test / CLI entry point
if __name__ == "__main__":
    import os

    orchestrator = TestOrchestrator()

    # In CI (no TTY, or CI=true set by GitHub Actions) never prompt --
    # fall back to an env var, or all condition types by default.
    is_ci = os.environ.get("CI", "").lower() == "true" or not __import__("sys").stdin.isatty()

    if is_ci:
        env_types = os.environ.get("CONDITION_TYPES", "").strip()
        selected_types = (
            [t.strip() for t in env_types.split(",") if t.strip()]
            if env_types and env_types.lower() != "all"
            else None
        )
    else:
        selected_types = orchestrator.cond_generator.prompt_for_condition_types()

    result = orchestrator.process_all_requirements(selected_types)

    print(f"\n{json.dumps(result, indent=2)}")
