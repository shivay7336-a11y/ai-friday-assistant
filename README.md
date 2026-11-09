# AI Friday Assistant 🤖

An AI-powered Friday assistant for intelligent task management, weekly summaries, and workflow automation.

## Features

✨ **Task Management**
- Create and manage tasks with priority levels
- Track task completion status
- Set due dates and reminders

📊 **Weekly Summaries**
- Automated weekly performance reports
- Completion rate analytics
- Progress tracking

🔴 **Smart Prioritization**
- Filter tasks by priority (high, medium, low)
- Focus on what matters most
- Quick status overview

🚀 **Automation**
- Scheduled task checks
- Automated reminders
- Integration-ready architecture

## Installation

```bash
git clone https://github.com/shivay7336-a11y/ai-friday-assistant.git
cd ai-friday-assistant
pip install -r requirements.txt
```

## Quick Start

```bash
python main.py
```

## Usage

### Add a Task
```python
assistant = AIFridayAssistant()
assistant.add_task("Review pull requests", priority="high")
```

### Complete a Task
```python
assistant.complete_task(task_id)
```

### Get Weekly Summary
```python
summary = assistant.get_weekly_summary()
```

### View High Priority Tasks
```python
high_priority = assistant.get_high_priority_tasks()
```

## Project Structure

```
ai-friday-assistant/
├── main.py           # Entry point
├── demo.py           # Demo and core functionality
├── requirements.txt  # Dependencies
├── README.md         # This file
└── .gitignore        # Git ignore rules
```

## Commands

Run the demo:
```bash
python demo.py
```

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## License

MIT License - See LICENSE file for details

---

**Made
 with ❤️ for productive Fridays!**

name: Python CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then
            python -m pip install -r requirements.txt
          fi

      - name: Check Python syntax
        run: python -m compileall -q .

      - name: Run tests if available
        run: |
          if find . -type f \( -name "test_*.py" -o -name "*_test.py" \) | grep -q .; then
            python -m pip install pytest
            python -m pytest -q
          else
            echo "No tests found; skipping."
          fi

