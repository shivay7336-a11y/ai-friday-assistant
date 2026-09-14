#!/usr/bin/env python3
"""
AI Friday Assistant - Demo
A simple demo showing the core capabilities of the AI Friday Assistant
"""

import json
from datetime import datetime, timedelta

class AIFridayAssistant:
    def __init__(self):
        self.tasks = []
        self.weekly_summary = {}
        
    def add_task(self, title, priority="medium", due_date=None):
        """Add a task to the assistant"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "due_date": due_date or datetime.now().strftime("%Y-%m-%d"),
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.tasks.append(task)
        return f"✅ Task added: {title}"
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return f"✅ Task completed: {task['title']}"
        return "❌ Task not found"
    
    def get_weekly_summary(self):
        """Generate a weekly summary"""
        completed = sum(1 for t in self.tasks if t["completed"])
        total = len(self.tasks)
        
        summary = {
            "week": datetime.now().strftime("%Y-W%V"),
            "total_tasks": total,
            "completed_tasks": completed,
            "completion_rate": f"{(completed/total*100):.1f}%" if total > 0 else "0%",
            "timestamp": datetime.now().isoformat()
        }
        return summary
    
    def get_high_priority_tasks(self):
        """Get all high priority tasks"""
        return [t for t in self.tasks if t["priority"] == "high" and not t["completed"]]
    
    def show_status(self):
        """Display current status"""
        print("\n🤖 AI Friday Assistant Status")
        print("=" * 50)
        print(f"📅 Date: {datetime.now().strftime('%A, %B %d, %Y')}")
        print(f"📊 Total Tasks: {len(self.tasks)}")
        print(f"✅ Completed: {sum(1 for t in self.tasks if t['completed'])}")
        print(f"⏳ Pending: {sum(1 for t in self.tasks if not t['completed'])}")
        print("\n📝 Tasks:")
        for task in self.tasks:
            status = "✅" if task["completed"] else "⏳"
            print(f"  {status} [{task['priority'].upper()}] {task['title']}")
        print("=" * 50 + "\n")

def main():
    print("🎉 Welcome to AI Friday Assistant Demo!\n")
    
    assistant = AIFridayAssistant()
    
    # Demo: Add some tasks
    print("📌 Adding tasks...")
    assistant.add_task("Review pull requests", priority="high")
    assistant.add_task("Update documentation", priority="medium")
    assistant.add_task("Deploy to production", priority="high")
    assistant.add_task("Team standup meeting", priority="medium")
    assistant.add_task("Code review for feature X", priority="low")
    print()
    
    # Demo: Show status
    assistant.show_status()
    
    # Demo: Complete some tasks
    print("✨ Completing tasks...")
    assistant.complete_task(1)
    assistant.complete_task(4)
    print()
    
    # Demo: Show updated status
    assistant.show_status()
    
    # Demo: Get high priority tasks
    print("🔴 High Priority Tasks:")
    high_priority = assistant.get_high_priority_tasks()
    for task in high_priority:
        print(f"  • {task['title']}")
    print()
    
    # Demo: Weekly summary
    print("📈 Weekly Summary:")
    summary = assistant.get_weekly_summary()
    print(json.dumps(summary, indent=2))
    print()

if __name__ == "__main__":
    main()
