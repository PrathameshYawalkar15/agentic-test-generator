"""Generate Gherkin test cases from conditions"""

from typing import List, Dict
from datetime import datetime


class GherkinGenerator:
    """Generate Gherkin feature files from test conditions"""

    def __init__(self):
        self.gherkin_template = {
            "positive": {
                "given": "a {feature} system in normal state",
                "when": "{condition}",
                "then": "the system should respond correctly"
            },
            "negative": {
                "given": "a {feature} system ready to detect errors",
                "when": "{condition}",
                "then": "the system should handle the error gracefully"
            },
            "boundary": {
                "given": "a {feature} system at boundary conditions",
                "when": "{condition} at exact threshold",
                "then": "the system should trigger correctly"
            }
        }

    def generate_feature_file(self, requirement_title: str,
                               conditions: List[Dict]) -> str:
        """Generate complete feature file"""

        feature_header = f"""Feature: {requirement_title}

  # Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

"""

        scenarios = []
        seen_names = {}
        for i, condition in enumerate(conditions, 1):
            scenario = self._generate_scenario(condition, i, seen_names)
            scenarios.append(scenario)

        return feature_header + "\n".join(scenarios)

    def _generate_scenario(self, condition: Dict, index: int,
                            seen_names: Dict[str, int]) -> str:
        """Generate a single Gherkin scenario"""
        test_type = condition.get("test_type", "positive")
        template = self.gherkin_template.get(test_type, self.gherkin_template["positive"])

        feature = condition.get("feature", "system")
        description = condition.get("description", "")

        # Clean up description
        description = description.replace("When ", "").replace("when ", "")

        given = template["given"].format(feature=feature)
        when = template["when"].format(condition=description)
        then = template["then"]

        # Build a scenario name from the condition type + a snippet of the
        # feature text. Using the type alone (e.g. "Threshold") collides
        # whenever more than one requirement feature maps to the same
        # condition type, producing multiple identically-named scenarios
        # in the same feature file -- confusing in reports and something
        # some BDD runners handle poorly. Appending a feature snippet keeps
        # names unique and readable.
        type_label = condition.get("type", f"scenario_{index}").replace("_", " ").title()
        feature_snippet = feature.strip()
        if len(feature_snippet) > 40:
            feature_snippet = feature_snippet[:37].rstrip() + "..."
        base_name = f"{type_label} - {feature_snippet}" if feature_snippet else type_label

        # Guard against remaining duplicates (e.g. identical feature text
        # appearing twice) by suffixing a counter.
        seen_names[base_name] = seen_names.get(base_name, 0) + 1
        scenario_name = base_name if seen_names[base_name] == 1 else f"{base_name} ({seen_names[base_name]})"

        scenario = f"""@test
Scenario: {scenario_name}
  Given {given}
  When {when}
  Then {then}
"""
        return scenario

    def save_feature_file(self, filename: str, content: str,
                           output_dir: str = "features") -> str:
        """Save feature file to disk"""
        import os
        os.makedirs(output_dir, exist_ok=True)

        filepath = os.path.join(output_dir, f"{filename}.feature")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Feature file created: {filepath}")
        return filepath

    def validate_gherkin(self, content: str) -> Dict:
        """Validate Gherkin syntax.

        Checks that the file declares a Feature, has at least one
        Scenario, and that each Scenario is immediately followed (modulo
        blank/tag lines) by Given, then When, then Then -- in that order.
        """
        issues = []
        lines = [l.rstrip() for l in content.split('\n')]

        if not any(l.startswith('Feature:') for l in lines):
            issues.append("Missing 'Feature:' declaration")

        scenario_indices = [i for i, l in enumerate(lines) if l.strip().startswith('Scenario:')]
        scenario_count = len(scenario_indices)

        if scenario_count == 0:
            issues.append("No scenarios found")

        expected_order = ['Given', 'When', 'Then']
        for idx in scenario_indices:
            step_lines = []
            for line in lines[idx + 1:]:
                stripped = line.strip()
                if not stripped or stripped.startswith('@'):
                    continue
                if stripped.startswith('Scenario:'):
                    break
                if stripped.startswith(('Given', 'When', 'Then', 'And', 'But')):
                    step_lines.append(stripped.split(' ', 1)[0])
                else:
                    break

            scenario_name = lines[idx].strip()
            if step_lines[:3] != expected_order:
                issues.append(
                    f"'{scenario_name}' does not have Given/When/Then in order"
                )

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "scenario_count": scenario_count
        }


# Test
if __name__ == "__main__":
    from test_condition_generator import TestConditionGenerator

    features = [
        "Detect brake pressure > 50%",
        "Engage within 100ms"
    ]

    # Generate conditions
    cond_gen = TestConditionGenerator()
    conditions = cond_gen.generate_conditions(features)  # all condition types
    conditions = cond_gen.prioritize_conditions(conditions)

    # Generate Gherkin
    gherkin_gen = GherkinGenerator()
    feature_content = gherkin_gen.generate_feature_file("ABS Braking System", conditions)

    print(feature_content)
    print("\n" + "=" * 60)

    # Validate
    validation = gherkin_gen.validate_gherkin(feature_content)
    print(f"✅ Validation: {validation}")

    # Save
    gherkin_gen.save_feature_file("abs_system", feature_content)
