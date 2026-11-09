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
