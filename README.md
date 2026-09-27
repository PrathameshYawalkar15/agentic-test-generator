# 🤖 Agentic Test Case Generator with Execution

**Zero-cost, automated test generation and execution pipeline using Ollama, GitHub Actions, and pytest-bdd**

## 🎯 Features

✅ **Step 1: Read Requirements** - Parse markdown requirement files
✅ **Step 2: Generate Test Conditions** - Generate test scenarios from requirements, for condition types you choose (threshold, boundary, timing, state, error, recovery)
✅ **Step 3: Generate Gherkin** - Create BDD-style test cases
✅ **Step 4: Execute Tests** - Run generated tests automatically
✅ **Step 5: Report Results** - Generate HTML and Allure reports

## 🏗️ Architecture

```
Requirements (.md) → Test Conditions → Gherkin Features → Test Execution → Reports
                        ↓                    ↓                  ↓
                  Ollama LLM           pytest-bdd          HTML + Allure
```

## 📦 Tech Stack

| Component | Technology | Cost |
|-----------|-----------|------|
| LLM | Ollama + Mistral 7B | FREE |
| Test Generation | Python | FREE |
| Test Format | Gherkin | FREE |
| Test Execution | pytest-bdd | FREE |
| CI/CD | GitHub Actions | FREE |
| Container | Docker | FREE |
| **TOTAL** | | **$0** |

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone <repo>
cd agentic-test-generator
bash setup.sh
source venv/bin/activate
```

### 2. Start Ollama
```bash
ollama serve &
```

### 3. Add Requirement
```bash
echo "# My Feature

System shall do X, Y, Z.

## Requirements
- Requirement 1
- Requirement 2
- Requirement 3
" > requirements/my_feature.md
```

### 4. Generate & Execute Tests
```bash
# Local execution
python -c "from src.orchestrator import TestOrchestrator; TestOrchestrator().process_all_requirements()"
python src/generate_steps.py
pytest features/ -v --html=reports/report.html

# Or use Docker
docker-compose up
```

### 5. View Results
```bash
# Open HTML report
open reports/report.html

# Or GitHub Actions (if pushed)
# Go to Actions tab
```

## 📝 How It Works

### Step 1: Read Requirement
```
Input: requirements/abs_system.md
Output: Parsed requirement object
```

### Step 2: Generate Test Conditions
```
Input: List of features/requirements, plus which condition types to
       generate (threshold, boundary, timing, state, error, recovery --
       or leave unset for all of them)
Output: Test conditions
```

Condition types are selected, not auto-detected from keywords in the
requirement text. Three ways to choose them:

```bash
# Interactively (prompts with a numbered menu)
python -c "
from src.orchestrator import TestOrchestrator
orch = TestOrchestrator()
types = orch.cond_generator.prompt_for_condition_types()
orch.process_all_requirements(types)
"

# Programmatically
python -c "
from src.orchestrator import TestOrchestrator
TestOrchestrator().process_all_requirements(['threshold', 'boundary'])
"

# Via environment variable (used automatically in CI -- see workflow
# 1's condition_types workflow_dispatch input)
CONDITION_TYPES=threshold,error python -m src.orchestrator
```

### Step 3: Generate Gherkin
```
Input: Test conditions
Output: features/abs_system.feature
  Scenario: Threshold - Detect brake pressure > 50%
    Given a Detect brake pressure > 50% system in normal state
    When Detect brake pressure > 50% exceeds > 50%
    Then the system should respond correctly
```

### Step 4: Execute Tests
```
Command: python src/generate_steps.py && pytest features/ -v
Output: PASSED/FAILED results
```

Step definitions must be (re)generated any time features/ changes --
pytest-bdd matches steps by exact text, so stale step definitions from
an earlier run will report "step not found" for anything new.

### Step 5: Generate Reports
```
Output: 
  - HTML report
  - Allure report
  - GitHub issue
```

## 📁 Project Structure

```
├── src/
│   ├── requirement_reader.py         # Step 1
│   ├── test_condition_generator.py   # Step 2
│   ├── gherkin_generator.py          # Step 3
│   ├── orchestrator.py               # Main
│   ├── llm_client.py                 # Ollama
│   └── generate_steps.py             # Step definitions from features/
├── requirements/                     # Your requirement files
├── features/                         # AUTO-GENERATED Gherkin files
├── step_definitions/                 # AUTO-GENERATED step implementations
├── reports/                          # AUTO-GENERATED test reports
├── .github/workflows/
│   ├── 1_generate_tests.yml          # Workflow 1
│   ├── 2_execute_tests.yml           # Workflow 2
│   ├── 3_report_results.yml          # Workflow 3
│   └── ci_cd_pipeline.yml            # Master pipeline
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── setup.sh
└── README.md
```

## 🔄 CI/CD Pipelines

### Workflow 1: Generate Tests
Triggered: On push to `requirements/` directory, or manually via
`workflow_dispatch` (which lets you set a `condition_types` input --
e.g. `threshold,boundary` -- instead of generating every type)
- Reads requirement files
- Generates test conditions
- Creates Gherkin feature files
- Uploads artifacts

### Workflow 2: Execute Tests
Triggered: After Workflow 1 succeeds
- Downloads generated features (from workflow 1's run)
- Generates matching step definitions with `src/generate_steps.py`
- Runs pytest-bdd
- Generates HTML reports
- Creates test artifacts, and forwards the generation report so
  Workflow 3 can reach it

### Workflow 3: Report Results
Triggered: After Workflow 2 completes
- Generates comprehensive report
- Creates GitHub issue with results
- Archives reports

## 📊 Example Output

### Generated Feature File
```gherkin
Feature: ABS Braking System

@test
Scenario: Threshold - Detect brake pressure > 50%
  Given a Detect brake pressure > 50% system in normal state
  When Detect brake pressure > 50% exceeds > 50%
  Then the system should respond correctly

@test
Scenario: Timing - Engage within 100ms
  Given a Engage within 100ms system in normal state
  When Engage within 100ms is triggered within 100ms
  Then the system should respond correctly

@test
Scenario: Error - Engage within 100ms
  Given a Engage within 100ms system ready to detect errors
  When Engage within 100ms fails or is unavailable
  Then the system should handle the error gracefully
```

### Test Execution Report
```
features/abs_system.feature::Threshold - Detect brake pressure > 50% PASSED [33%]
features/abs_system.feature::Timing - Engage within 100ms PASSED [66%]
features/abs_system.feature::Error - Engage within 100ms PASSED [100%]

============ 3 passed in 1.23s ============
```

## 🐳 Docker Usage

```bash
# Start with docker-compose (generates conditions for every type,
# then step definitions, then runs pytest)
docker-compose up

# Generate only specific condition types
CONDITION_TYPES=threshold,timing docker-compose up

# Run tests again in the already-built container
docker-compose exec test_generator pytest features/ -v

# Stop
docker-compose down
```

## 🧪 Manual Testing

```bash
# Test requirement reading
python -c "from src.requirement_reader import RequirementReader; r = RequirementReader(); print(r.read_all_requirements())"

# Test condition generation -- all types
python -c "from src.test_condition_generator import TestConditionGenerator; g = TestConditionGenerator(); print(g.generate_conditions(['Detect X', 'Within 100ms']))"

# Test condition generation -- specific types only
python -c "from src.test_condition_generator import TestConditionGenerator; g = TestConditionGenerator(); print(g.generate_conditions(['Detect X', 'Within 100ms'], ['timing', 'error']))"

# Test Gherkin generation
python -c "from src.gherkin_generator import GherkinGenerator; g = GherkinGenerator(); print(g.generate_feature_file('Test', [{'type': 'positive', 'feature': 'X', 'description': 'test'}]))"

# Full pipeline
python -c "from src.orchestrator import TestOrchestrator; TestOrchestrator().process_all_requirements()"
```

## 📈 Metrics & Reports

**Automatically Generated:**
- Total requirements processed
- Test conditions generated
- Gherkin scenarios created
- Test pass/fail rates
- Execution time
- Coverage analysis

## 🔧 Customization

### Change LLM Model
```python
# In src/orchestrator.py
self.llm_client = OllamaClient(model="neural-chat:7b")
```

### Add a New Condition Type
```python
# In src/test_condition_generator.py, add an entry to CONDITION_TYPES:
CONDITION_TYPES: Dict[str, Dict] = {
    ...,
    "custom": {
        "template": "When {feature} is triggered by a custom event",
        "test_type": "positive",  # or "negative" / "boundary"
    },
}
```
It'll automatically show up in the CLI menu (`prompt_for_condition_types`)
and can be selected via `generate_conditions(features, ["custom"])`.

### Modify Gherkin Templates
```python
# In src/gherkin_generator.py
self.gherkin_template["custom"] = {
    "given": "...",
    "when": "...",
    "then": "..."
}
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Ollama not found | `curl -fsSL https://ollama.com/install.sh \| sh` |
| Connection refused | `ollama serve &` |
| Models not loaded | `ollama pull mistral:7b` |
| Python version | Use Python 3.10+ |
| Permission denied | `chmod +x setup.sh` |
| pytest-bdd says "step not found" | Regenerate step definitions after any change to features/: `python src/generate_steps.py` |

## 📚 Documentation

- [QUICK_RUN.md](QUICK_RUN.md) - 5-minute quick start
- [docs/](docs/) - Detailed documentation

## 🤝 Contributing

Improvements welcome! Areas:
- Better test condition generation
- Domain-specific templates
- Enhanced reporting
- Performance optimization

## 📄 License

MIT License - Use freely!

## 📞 Support

- Check troubleshooting guide
- Review GitHub Issues
- Check logs in artifacts

---

**Ready to generate tests?** 🚀

```bash
bash setup.sh && ollama serve &
```

Then:

```bash
python -c "from src.orchestrator import TestOrchestrator; TestOrchestrator().process_all_requirements()"
python src/generate_steps.py
pytest features/ -v
```

**Made with ❤️ for QA Engineers**
