# Quick Run Guide - 5 Minutes

## Option 1: Using Docker (Easiest)

```bash
# 1. Start Ollama and generator
docker-compose up

# 2. In another terminal, add a requirement
echo "# Speed Limiter

System must limit vehicle speed to 200 km/h.

## Requirements
- Monitor actual speed
- Trigger warning at 180 km/h
- Reduce throttle at 190 km/h
- Hard limit at 200 km/h
" > requirements/speed_limiter.md

# 3. Watch the pipeline run automatically (push to git)
git add .
git commit -m "Add speed limiter requirement"
git push

# 4. Check GitHub Actions tab for:
# - Test generation
# - Test execution
# - Reports
```

## Option 2: Local Setup

```bash
# 1. Setup
bash setup.sh
source venv/bin/activate

# 2. Start Ollama in background
ollama serve &

# 3. Generate tests
python -c "
from src.orchestrator import TestOrchestrator
TestOrchestrator().process_all_requirements()
"

# 4. Generate step definitions (required before running pytest --
# pytest-bdd matches steps by exact text against features/)
python src/generate_steps.py

# 5. Run generated tests
pytest features/ -v --html=reports/report.html

# 6. View report
open reports/report.html
```

## Option 3: GitHub Actions Only

```bash
# 1. Push requirement file
echo "# My Feature" > requirements/my_feature.md
git add .
git commit -m "Add requirement"
git push

# 2. Watch Actions tab
# GitHub automatically:
# - Generates tests
# - Executes tests
# - Creates report
```

Want only certain condition types instead of all of them? Trigger
Workflow 1 manually from the Actions tab (`workflow_dispatch`) and set
the `condition_types` input, e.g. `threshold,boundary`.

## What You'll See

### Step 1: Requirement Reading
```
✅ Read requirement: abs_system.md
```

### Step 2: Test Condition Generation
```
Condition types: all
✅ Generated 24 test conditions
```

(4 features × 6 condition types by default -- threshold, boundary,
timing, state, error, recovery. Pass a `condition_types` list to
generate fewer.)

### Step 3: Gherkin Generation
```
✅ Feature file created: features/abs_system.feature

Feature: ABS Braking System

  # Generated: 2026-01-15 10:30:45

@test
Scenario: Threshold - Detect brake pressure > 50%
  Given a Detect brake pressure > 50% system in normal state
  When Detect brake pressure > 50% exceeds > 50%
  Then the system should respond correctly

@test
Scenario: Boundary - Detect brake pressure > 50%
  Given a Detect brake pressure > 50% system at boundary conditions
  When Detect brake pressure > 50% is at boundary value > 50% at exact threshold
  Then the system should trigger correctly
```

### Step 4: Test Execution
```
✅ Generated: step_definitions/conftest.py

features/abs_system.feature::Threshold - Detect brake pressure > 50% PASSED
features/abs_system.feature::Boundary - Detect brake pressure > 50% PASSED
features/abs_system.feature::Error - Detect brake pressure > 50% PASSED

========== 3 passed in 0.42s ==========
```

### Step 5: Report Generated
```
HTML Report: reports/report.html
- Total Tests: 24
- Passed: 24
- Failed: 0
- Duration: 2.5s
```

## File Structure After Execution

```
project/
├── requirements/
│   ├── sample_requirement.md
│   ├── speed_limiter.md
│   └── abs_system.md
├── features/                    # AUTO-GENERATED
│   ├── abs_system.feature
│   ├── speed_limiter.feature
│   └── sample_requirement.feature
├── step_definitions/            # AUTO-GENERATED
│   └── conftest.py
├── reports/                     # AUTO-GENERATED
│   ├── report.html
│   └── allure-results/
└── generation_result.json       # AUTO-GENERATED
```

## End-to-End Flow

```
Your Requirement (Markdown)
         ↓
  [1️⃣ Read Requirement] ← Step 1: RequirementReader
         ↓
  [2️⃣ Generate Conditions] ← Step 2: TestConditionGenerator
         ↓                     (for the condition types you chose)
  [3️⃣ Generate Gherkin] ← Step 3: GherkinGenerator
         ↓
  Feature Files (.feature)
         ↓
  [4️⃣ Generate Step Definitions] ← src/generate_steps.py
         ↓
  [5️⃣ Execute Tests] ← pytest + pytest-bdd
         ↓
  Test Results (PASS/FAIL)
         ↓
  [6️⃣ Generate Reports] ← HTML + Allure
```

## GitHub Actions Pipeline

```
Push Requirement File
         ↓
Workflow 1: Generate Tests
  ├─ Read requirement
  ├─ Generate conditions (all types, or the condition_types input)
  └─ Create feature files
         ↓
Workflow 2: Execute Tests
  ├─ Download features (from workflow 1's run)
  ├─ Generate step definitions (src/generate_steps.py)
  ├─ Run pytest
  ├─ Generate reports
  └─ Forward the generation report for workflow 3
         ↓
Workflow 3: Report Results
  ├─ Create HTML report
  ├─ Comment on PR
  └─ Create GitHub issue
```

## Key Files

| File | Purpose |
|------|---------|
| `src/requirement_reader.py` | Reads markdown requirements |
| `src/test_condition_generator.py` | Generates test conditions for chosen condition types |
| `src/gherkin_generator.py` | Creates Gherkin feature files |
| `src/orchestrator.py` | Orchestrates entire pipeline |
| `src/generate_steps.py` | Generates step_definitions/conftest.py from features/ |
| `.github/workflows/1_generate_tests.yml` | GitHub Actions: Generate |
| `.github/workflows/2_execute_tests.yml` | GitHub Actions: Execute |
| `.github/workflows/3_report_results.yml` | GitHub Actions: Report |

---

**Start now:**
```bash
bash setup.sh && ollama serve &
```

Then run:
```bash
python -c "from src.orchestrator import TestOrchestrator; TestOrchestrator().process_all_requirements()"
python src/generate_steps.py
pytest features/ -v
```

That's it! 🚀
