"""
AI Friday Assistant - Text-to-Speech Module
Provides female voice output for the assistant
"""

import pyttsx3
import threading
from typing import Optional

class VoiceAssistant:
    def __init__(self, rate: int = 150, volume: float = 0.9):
        """
        Initialize the voice assistant with female voice
        
        Args:
            rate: Speech rate (words per minute)
            volume: Volume level (0.0 to 1.0)
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        self._set_female_voice()
        
    def _set_female_voice(self):
        """Set the engine to use a female voice"""
        voices = self.engine.getProperty('voices')
        
        # Try to find and set a female voice
        for voice in voices:
            if 'female' in voice.name.lower() or 'woman' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                return
        
        # Fallback: use the second voice (usually female) if available
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)
        
    def speak(self, text: str, wait: bool = True):
        """
        Speak the given text using female voice
        
        Args:
            text: Text to speak
            wait: Wait for speech to finish
        """
        self.engine.say(text)
        if wait:
            self.engine.runAndWait()
        else:
            threading.Thread(target=self.engine.runAndWait).start()
    
    def speak_async(self, text: str):
        """Speak text asynchronously"""
        self.speak(text, wait=False)
    
    def set_rate(self, rate: int):
        """Set speech rate (words per minute)"""
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume: float):
        """Set volume level (0.0 to 1.0)"""
        self.engine.setProperty('volume', max(0.0, min(1.0, volume)))
    
    def get_voices(self):
        """Get available voices"""
        voices = self.engine.getProperty('voices')
        voice_info = []
        for i, voice in enumerate(voices):
            voice_info.append({
                'id': i,
                'name': voice.name,
                'gender': 'Female' if 'female' in voice.name.lower() else 'Male'
            })
        return voice_info
    
    def stop(self):
        """Stop speaking"""
        self.engine.stop()

# Global voice instance
_voice_instance: Optional[VoiceAssistant] = None

def get_voice_assistant() -> VoiceAssistant:
    """Get or create the global voice assistant instance"""
    global _voice_instance
    if _voice_instance is None:
        _voice_instance = VoiceAssistant()
    return _voice_instance

def speak(text: str, wait: bool = True):
    """Convenience function to speak text"""
    assistant = get_voice_assistant()
    assistant.speak(text, wait)

def speak_async(text: str):
    """Convenience function to speak text asynchronously"""
    assistant = get_voice_assistant()
    assistant.speak_async(text)
