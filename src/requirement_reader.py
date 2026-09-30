"""Read requirements from markdown files"""

import os
import subprocess
from typing import Dict, List


class RequirementReader:
    """Read and parse requirement files"""

    def __init__(self, requirements_dir: str = "requirements"):
        self.requirements_dir = requirements_dir
        os.makedirs(requirements_dir, exist_ok=True)

    @staticmethod
    def get_all_requirements(requirements_dir: str = "requirements") -> List[str]:
        """Returns all .md files in the requirements directory as a fallback."""
        all_files = []
        if os.path.exists(requirements_dir):
            for filename in os.listdir(requirements_dir):
                if filename.endswith(".md"):
                    all_files.append(os.path.join(requirements_dir, filename))
        return all_files

    @staticmethod
    def get_modified_requirements(requirements_dir: str = "requirements") -> List[str]:
        """Uses Git to find modified or untracked .md files in the CI/CD pipeline."""
        modified_files = []
        try:
            result = subprocess.run(
                ['git', 'ls-files', '--modified', '--others', '--exclude-standard', requirements_dir],
                stdout=subprocess.PIPE,
                text=True,
                check=True
            )
            for line in result.stdout.splitlines():
                if line.endswith(".md"):
                    filepath = os.path.abspath(line)
                    modified_files.append(filepath)
        except subprocess.CalledProcessError:
            print("Warning: Git command failed. Ensure the CI/CD pipeline has checked out the git repository.")
        return modified_files

    def read_requirement_file(self, filename: str) -> str:
        """Read a single requirement file"""
        filepath = os.path.join(self.requirements_dir, filename) if not os.path.isabs(filename) else filename

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Requirement file not found: {filepath}")

        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def read_all_requirements(self) -> Dict[str, str]:
        """Read all requirement files"""
        requirements = {}

        if not os.path.exists(self.requirements_dir):
            print(f"⚠️️  Requirements directory not found: {self.requirements_dir}")
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
        """Parse requirement into structured format."""
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