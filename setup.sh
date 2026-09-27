#!/bin/bash

set -e

echo "🚀 Setting up Agentic Test Generator with Execution"
# The original "=" * 60 is Python syntax, not bash -- bash has no string
# multiplication operator, so that line just printed the literal
# characters "= * 60" instead of a 60-character divider.
printf '=%.0s' $(seq 1 60)
echo

# 1. Check Python
python_version=$(python3 --version | awk '{print $2}')
echo "✅ Python version: $python_version"

# 2. Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

# 3. Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# 4. Install Ollama
if ! command -v ollama &> /dev/null; then
    echo "⚠️ Installing Ollama..."
    # ollama.ai has been superseded by ollama.com for the install script;
    # ollama.com/install.sh is what the project's own docs point to now.
    curl -fsSL https://ollama.com/install.sh | sh
fi

# 5. Pull models
echo "🦙 Pulling LLM models..."
ollama pull mistral:7b
ollama pull nomic-embed-text

# 6. Create directories
mkdir -p requirements features step_definitions reports

# 7. Create sample requirement
# Filename matches requirements/sample_requirement.md as named in the
# project structure -- the original wrote "sample.md" here, which
# doesn't match and would leave requirements/sample_requirement.md
# looking present in the structure diagram but never actually created.
if [ ! -f "requirements/sample_requirement.md" ]; then
    cat > requirements/sample_requirement.md << 'EOF'
# ABS Braking System

The system shall implement anti-lock braking to prevent wheel lockup.

## Requirements
- Detect brake pressure > 50%
- Engage within 100ms
- Modulate pressure at 10Hz
- Deactivate below 10 km/h
- Log all events
EOF
fi

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Start Ollama: ollama serve &"
echo "2. Generate tests: python -c 'from src.orchestrator import TestOrchestrator; TestOrchestrator().process_all_requirements()'"
echo "   (add a condition_types list to process_all_requirements([...]) to pick specific condition types)"
echo "3. Generate step definitions: python src/generate_steps.py"
echo "4. Run tests: pytest features/ -v"
echo ""
echo "Or use Docker: docker-compose up"
