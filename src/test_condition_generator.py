"""Generate test conditions from requirements, based on condition types
the user selects (e.g. threshold, timing, boundary) rather than
auto-detected keywords."""

import re
from typing import Dict, List, Optional


class TestConditionGenerator:
    """Generate test conditions for requirement features, using condition
    types the user selects from a menu.
    """

    # Each entry defines the sentence template plus the test_type used
    # later for prioritization. Templates with {value}/{state}/{condition}
    # placeholders get a value extracted from the feature text when
    # possible, otherwise a generic fallback phrase.
    CONDITION_TYPES: Dict[str, Dict] = {
        "threshold": {
            "template": "When {feature} exceeds {value}",
            "test_type": "positive",
        },
        "boundary": {
            "template": "When {feature} is at boundary value {value}",
            "test_type": "boundary",
        },
        "timing": {
            "template": "When {feature} is triggered within {value}",
            "test_type": "positive",
        },
        "state": {
            "template": "When {feature} is {state}",
            "test_type": "positive",
        },
        "error": {
            "template": "When {feature} fails or is unavailable",
            "test_type": "negative",
        },
        "recovery": {
            "template": "When {feature} returns to normal after {condition}",
            "test_type": "positive",
        },
    }

    # Regex used to pull a concrete value (e.g. "> 50%", "100ms", "10 km/h")
    # out of the raw feature text, so templates aren't stuck with generic
    # placeholder text when the requirement already states a real value.
    VALUE_PATTERN = re.compile(
        r'([<>]=?\s*[\d.]+\s*\S*|\b[\d.]+\s*(?:ms|milliseconds|s|seconds|km/h|%|Hz)\b)',
        re.IGNORECASE
    )

    def available_condition_types(self) -> List[str]:
        """Return the list of condition type keys that can be selected."""
        return list(self.CONDITION_TYPES.keys())

    def prompt_for_condition_types(self) -> List[str]:
        """Show a simple CLI menu and let the user pick condition types.

        Returns the selected type keys. Empty input or "0" selects all
        types. Swap this out for however input is actually collected in
        your pipeline (CLI flags, a workflow_dispatch input, etc.) --
        generate_conditions() only needs the resulting list of keys.
        """
        types = self.available_condition_types()

        print("\nSelect the condition types to generate (comma-separated numbers):")
        for i, type_key in enumerate(types, start=1):
            print(f"  {i}. {type_key}")
        print("  0. All of the above")

        raw = input("Your selection: ").strip()

        if not raw or raw == "0":
            return types

        selected = []
        for part in raw.split(","):
            part = part.strip()
            if part.isdigit() and 1 <= int(part) <= len(types):
                selected.append(types[int(part) - 1])

        return selected or types

    def generate_conditions(
        self,
        features: List[str],
        condition_types: Optional[List[str]] = None,
    ) -> List[Dict]:
        """Generate test conditions for each feature, using only the
        given condition types. Defaults to all types if none are given.
        """
        if condition_types is None:
            condition_types = self.available_condition_types()

        invalid = set(condition_types) - set(self.CONDITION_TYPES)
        if invalid:
            raise ValueError(f"Unknown condition type(s): {', '.join(sorted(invalid))}")

        conditions = []
        for feature in features:
            for type_key in condition_types:
                conditions.append(self._build_condition(feature, type_key))

        return conditions

    def _extract_value(self, feature: str) -> Optional[str]:
        """Pull a concrete value out of the feature text, if present."""
        match = self.VALUE_PATTERN.search(feature)
        return match.group(0).strip() if match else None

    def _build_condition(self, feature: str, type_key: str) -> Dict:
        """Fill in a condition template for one feature + condition type."""
        spec = self.CONDITION_TYPES[type_key]
        template = spec["template"]
        extracted = self._extract_value(feature)

        fill = {"feature": feature}
        if "{value}" in template:
            fill["value"] = extracted or "the specified value"
        if "{state}" in template:
            fill["state"] = "active"
        if "{condition}" in template:
            fill["condition"] = "the fault is cleared"

        return {
            "type": type_key,
            "feature": feature,
            "description": template.format(**fill),
            "test_type": spec["test_type"],
        }

    def prioritize_conditions(self, conditions: List[Dict]) -> List[Dict]:
        """Prioritize conditions by test type (positive > boundary > negative)."""
        priority_order = {"positive": 1, "boundary": 2, "negative": 3}
        return sorted(
            conditions,
            key=lambda x: priority_order.get(x.get("test_type"), 4),
        )


if __name__ == "__main__":
    generator = TestConditionGenerator()

    features = [
        "Detect brake pressure > 50%",
        "Engage within 100ms",
        "Deactivate below 10 km/h",
    ]

    selected_types = generator.prompt_for_condition_types()
    conditions = generator.generate_conditions(features, selected_types)
    prioritized = generator.prioritize_conditions(conditions)

    print("\nGenerated Test Conditions:")
    for cond in prioritized:
        print(f"  - [{cond['type']}] {cond['description']}")
