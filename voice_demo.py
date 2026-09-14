#!/usr/bin/env python3
"""
AI Friday Assistant - Voice Demo
Demonstrates the female voice functionality
"""

from voice import VoiceAssistant, speak, speak_async
from demo import AIFridayAssistant
import time

def voice_demo():
    """Run a demo of the voice assistant"""
    print("\n🎤 AI Friday Assistant - Voice Demo\n")
    
    # Initialize voice assistant
    voice = VoiceAssistant(rate=150, volume=0.9)
    
    # Greet the user
    greeting = "Hello! I'm your AI Friday Assistant with a female voice!"
    print(f"Assistant: {greeting}")
    voice.speak(greeting)
    
    time.sleep(1)
    
    # Initialize task assistant
    assistant = AIFridayAssistant()
    
    # Add tasks
    print("\n📌 Adding tasks...")
    tasks = [
        ("Review pull requests", "high"),
        ("Update documentation", "medium"),
        ("Deploy to production", "high"),
    ]
    
    for task_title, priority in tasks:
        assistant.add_task(task_title, priority=priority)
        message = f"Added task: {task_title}"
        print(f"  {message}")
        voice.speak(message, wait=False)
        time.sleep(0.5)
    
    time.sleep(1)
    
    # Show status with voice
    print("\n📊 Showing status...")
    status_message = f"You have {len(assistant.tasks)} tasks to complete this Friday"
    print(f"Assistant: {status_message}")
    voice.speak(status_message)
    
    time.sleep(1)
    
    # Get high priority tasks
    high_priority = assistant.get_high_priority_tasks()
    priority_message = f"You have {len(high_priority)} high priority tasks"
    print(f"Assistant: {priority_message}")
    voice.speak(priority_message)
    
    time.sleep(1)
    
    # Completion message
    completion_message = "Your AI Friday Assistant is ready to help you stay productive!"
    print(f"\nAssistant: {completion_message}")
    voice.speak(completion_message)
    
    print("\n✅ Voice demo complete!\n")

if __name__ == "__main__":
    voice_demo()
