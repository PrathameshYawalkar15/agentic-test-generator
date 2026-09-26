"""Read requirements from markdown files"""

import os
from typing import List, Dict


class RequirementReader:
    """Read and parse requirement files"""

    def __init__(self, requirements_dir: str = "requirements"):
        self.requirements_dir = requirements_dir
        os.makedirs(requirements_dir, exist_ok=True)

    def read_requirement_file(self, filename: str) -> str:
        """Read a single requirement file"""
        filepath = os.path.join(self.requirements_dir, filename)

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Requirement file not found: {filepath}")

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        return content

    def read_all_requirements(self) -> Dict[str, str]:
        """Read all requirement files"""
        requirements = {}

        if not os.path.exists(self.requirements_dir):
            print(f"⚠️  Requirements directory not found: {self.requirements_dir}")
            return requirements

        for filename in os.listdir(self.requirements_dir):
            if filename.endswith(('.md', '.txt')):
                try:
                    content = self.read_requirement_file(filename)
                    requirements[filename] = content
                    print(f"✅ Read requirement: {filename}")
                except Exception as e:
                    print(f"❌ Error reading {filename}: {e}")

        return requirements

    def parse_requirement(self, content: str) -> Dict:
        """Parse requirement into structured format.

        Bullet points ('- ...') are grouped under the '## ' section
        heading they appear under. Bullets that appear before any
        section heading are grouped under a default 'General' key.
        `features` still returns a flat list of every bullet (for
        backwards compatibility), while `sections` exposes the
        per-section breakdown.
        """
        lines = content.strip().split('\n')

        title = ""
        description_lines: List[str] = []
        features: List[str] = []
        sections: Dict[str, List[str]] = {}

        current_section = "General"

        for line in lines:
            stripped = line.strip()

            if line.startswith('# '):
                title = line.replace('# ', '').strip()
            elif line.startswith('## '):
                current_section = line.replace('## ', '').strip()
                sections.setdefault(current_section, [])
            elif line.startswith('- '):
                feature = stripped[2:].strip()
                if feature:
                    features.append(feature)
                    sections.setdefault(current_section, []).append(feature)
            elif not line.startswith('#') and stripped:
                description_lines.append(stripped)

        return {
            "title": title,
            "description": ' '.join(description_lines).strip(),
            "features": features,
            "sections": sections,
            "raw_content": content
        }

    def validate_requirement(self, requirement: Dict) -> Dict:
        """Validate requirement has necessary information"""
        issues = []

        if not requirement.get("title"):
            issues.append("Missing title (use # Title format)")

        if not requirement.get("description"):
            issues.append("Missing description")

        if not requirement.get("features"):
            issues.append("No features defined (use - Feature format)")

        return {
            "valid": len(issues) == 0,
            "issues": issues
        }


# Test
if __name__ == "__main__":
    reader = RequirementReader()

    # Sample with two sections, to demonstrate grouping
    sample = """# ABS Braking System

The system shall implement anti-lock braking to prevent wheel lockup.

## Detection
- Detect brake pressure > 50%
- Detect wheel speed sensor faults

## Response
- Engage within 100ms
- Modulate pressure at 10Hz
- Deactivate below 10 km/h
- Log all events
"""

    os.makedirs("requirements", exist_ok=True)
    with open("requirements/abs_system.md", "w") as f:
        f.write(sample)

    req = reader.read_requirement_file("abs_system.md")
    parsed = reader.parse_requirement(req)
    validation = reader.validate_requirement(parsed)

    print(f"✅ Title: {parsed['title']}")
    print(f"✅ Description: {parsed['description']}")
    print(f"✅ Sections: {parsed['sections']}")
    print(f"✅ Valid: {validation}")