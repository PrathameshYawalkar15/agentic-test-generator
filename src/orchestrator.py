import os
import json
from typing import Dict, List, Optional
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
        print(f"\n{'='*60}")
        print(f"Processing: {filename}")
        print(f"{'='*60}")

        try:
            print("1️⃣  Reading requirement...")
            content = self.req_reader.read_requirement_file(filename)
            parsed = self.req_reader.parse_requirement(content)

            validation = self.req_reader.validate_requirement(parsed)
            if not validation["valid"]:
                print(f"❌ Validation failed: {validation['issues']}")
                return {"success": False, "errors": validation["issues"]}

            print("2️⃣  Generating test conditions...")
            conditions = self.cond_generator.generate_conditions(
                parsed.get("features", []),
                condition_types,
            )
            conditions = self.cond_generator.prioritize_conditions(conditions)
            print(f"✅ Generated {len(conditions)} test conditions")

            print("3️⃣  Generating Gherkin feature file...")
            feature_content = self.gherkin_gen.generate_feature_file(
                parsed.get("title", filename),
                conditions
            )

            print("4️⃣  Saving feature file...")
            feature_file = filename.replace('.md', '').replace('.txt', '')
            filepath = self.gherkin_gen.save_feature_file(
                feature_file,
                feature_content
            )

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
        print("\n" + "="*60)
        print("🚀 AGENTIC TEST GENERATOR - PROCESSING PIPELINE")
        print("="*60)
        if condition_types:
            print(f"Condition types: {', '.join(condition_types)}")
        else:
            print("Condition types: all")

        # Returns a dict of {filename: content}
        requirements = self.req_reader.read_all_requirements()

        if not requirements:
            print("⚠️  No requirements found")
            return {"success": False, "message": "No requirements found"}

        results = []
        for filename in requirements.keys():
            result = self.process_single_requirement(filename, condition_types)
            results.append(result)

        successful = sum(1 for r in results if r.get("success"))
        total_scenarios = sum(r.get("scenarios", 0) for r in results if r.get("success"))

        print(f"\n" + "="*60)
        print("📊 SUMMARY")
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