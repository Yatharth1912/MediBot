import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.engine import MediBot
from chatbot.intents import detect_intent

def test_greeting():
    bot = MediBot()
    response = bot.respond("hello")
    assert "MediBot" in response
    print("✅ Greeting test passed")

def test_symptom_detection():
    bot = MediBot()
    response = bot.respond("I have fever and headache")
    assert "fever" in response.lower()
    print("✅ Symptom detection test passed")

def test_emergency():
    bot = MediBot()
    response = bot.respond("I can't breathe")
    assert "EMERGENCY" in response
    print("✅ Emergency detection test passed")

def test_intent():
    assert detect_intent("hi") == 'greeting'
    assert detect_intent("bye") == 'goodbye'
    assert detect_intent("I have fever") == 'symptom_report'
    print("✅ Intent detection test passed")

if __name__ == "__main__":
    print("Running MediBot tests...\n")
    test_greeting()
    test_symptom_detection()
    test_emergency()
    test_intent()
    print("\n🎉 All tests passed!")