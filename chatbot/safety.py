"""
Safety checks for emergency situations
"""
import json

def load_emergency_keywords():
    try:
        with open('data/emergency_keywords.json', 'r') as f:
            return json.load(f)
    except:
        return {"critical": []}

def is_emergency(text):
    """Check if user's message indicates a medical emergency"""
    text_lower = text.lower()
    emergency_data = load_emergency_keywords()
    
    for keyword in emergency_data.get('critical', []):
        if keyword in text_lower:
            return True
    return False

def get_emergency_response():
    """Return emergency response message"""
    return """🚨 **THIS SOUNDS LIKE AN EMERGENCY!**

Please do the following **IMMEDIATELY**:

1. 📞 **Call 102** (Ambulance) or **108** (Emergency)
2. 🏥 Rush to the nearest hospital emergency room
3. 👥 Don't stay alone — call a family member or neighbor
4. 🫁 Stay calm and try to breathe slowly

**Do NOT wait or try home remedies for this.** Every minute matters.

If you're helping someone else, keep them calm and lying down until help arrives.

I'm just an AI — please get real medical help right now. 🙏"""