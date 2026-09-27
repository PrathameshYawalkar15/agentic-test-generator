"""Auto-generate step definitions from Gherkin files"""

import os
import re
from pathlib import Path
from typing import Dict, List


class StepDefinitionGenerator:
    """Generate step definitions from feature files"""

    def __init__(self):
        self.steps: Dict[str, List[str]] = {}

    def extract_steps_from_features(self, features_dir: str = "features") -> Dict:
        """Extract all unique steps from feature files"""
        steps = {
            "given": set(),
            "when": set(),
            "then": set()
        }

        if not os.path.exists(features_dir):
            return {k: list(v) for k, v in steps.items()}

        for feature_file in Path(features_dir).glob("*.feature"):
            with open(feature_file, 'r') as f:
                content = f.read()

            # Extract Given steps
            givens = re.findall(r'Given\s+(.+)', content)
            steps["given"].update(givens)

            # Extract When steps
            whens = re.findall(r'When\s+(.+)', content)
            steps["when"].update(whens)

            # Extract Then steps
            thens = re.findall(r'Then\s+(.+)', content)
            steps["then"].update(thens)

        return {k: list(v) for k, v in steps.items()}

    def generate_conftest(self, output_file: str = "step_definitions/conftest.py") -> str:
        """Generate conftest.py with step definitions"""
        steps = self.extract_steps_from_features()

        conftest_content = '''"""Auto-generated pytest-bdd step definitions.

Every Given/When/Then that appears in features/*.feature gets a matching
placeholder step here so pytest-bdd can bind scenarios to something. These
placeholders just assert True / return a status dict -- replace the ones
that matter for your domain with real assertions.
"""

import pytest
from pytest_bdd import given, when, then

# Given steps
'''

        for step in steps.get("given", []):
            step_name = self._safe_step_name(step, "given")
            escaped_step = step.replace('"', '\\"')
            conftest_content += f'''
@given("{escaped_step}")
def {step_name}():
    """Step: {step}"""
    return {{"status": "ready"}}
'''

        conftest_content += '''

# When steps
'''

        for step in steps.get("when", []):
            step_name = self._safe_step_name(step, "when")
            escaped_step = step.replace('"', '\\"')
            conftest_content += f'''
@when("{escaped_step}")
def {step_name}():
    """Step: {step}"""
    return {{"action": "executed"}}
'''

        conftest_content += '''

# Then steps
'''

        for step in steps.get("then", []):
            step_name = self._safe_step_name(step, "then")
            escaped_step = step.replace('"', '\\"')
            conftest_content += f'''
@then("{escaped_step}")
def {step_name}():
    """Step: {step}"""
    assert True
'''

        os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(conftest_content)

        print(f"✅ Generated: {output_file}")
        return output_file

    def _safe_step_name(self, step: str, prefix: str) -> str:
        """Turn arbitrary step text into a valid, reasonably unique
        Python function name. The original approach (lowercase + replace
        spaces with underscores, truncated to 30 chars) can produce
        invalid identifiers for steps containing punctuation like '>',
        '%', or '-', and can collide once truncated. This strips anything
        that isn't alnum/underscore and prefixes with given/when/then
        plus a short hash so names stay valid and distinct.
        """
        import hashlib
        slug = re.sub(r'[^a-zA-Z0-9_]', '_', step.strip().lower())
        slug = re.sub(r'_+', '_', slug).strip('_')[:40]
        digest = hashlib.md5(step.encode()).hexdigest()[:6]
        name = f"{prefix}_{slug}_{digest}" if slug else f"{prefix}_step_{digest}"
        return name


# Usage
if __name__ == "__main__":
    generator = StepDefinitionGenerator()
    generator.generate_conftest()
