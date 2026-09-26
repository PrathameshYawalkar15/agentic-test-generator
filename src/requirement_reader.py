"""Read requirements from markdown files"""

import os
import re
from pathlib import Path
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
        """Parse requirement into structured format"""
        lines = content.strip().split('\n')
        
        # Extract title (first header)
        title = ""
        description = ""
        features = []
        
        current_section = None
        
        for line in lines:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
            elif line.startswith('## '):
                current_section = line.replace('## ', '').strip()
            elif line.startswith('- '):
                feature = line.replace('- ', '').strip()
                if feature:
                    features.append(feature)
            elif not line.startswith('#'):
                if description and not description.endswith('\n'):
                    description += ' '
                description += line.strip()
        
        return {
            "title": title,
            "description": description.strip(),
            "features": features,
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
    
    # Create sample requirement
    sample = """# ABS Braking System

The system shall implement anti-lock braking to prevent wheel lockup.

## Requirements
- Detect brake pressure > 50%
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
    
    print(f"✅ Parsed: {parsed}")
    print(f"✅ Valid: {validation}")