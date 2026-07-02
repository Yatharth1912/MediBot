import re

def detect_intent(text):
    """Detect user's intent from their message using pattern matching"""
    text = text.lower().strip()
    
    # Medicine request patterns (NEW)
    medicine_patterns = [
        r'\b(medicine|medication|tablet|pill|drug|dawa|dawai)\b',
        r'suggest .* medicine',
        r'what should i take',
        r'which medicine'
    ]
    for pattern in medicine_patterns:
        if re.search(pattern, text):
            return 'medicine_request'
    
    # Home remedy patterns (NEW)
    remedy_patterns = [
        r'\b(home remedy|natural|gharelu|nuskha|remedies)\b',
        r'home treatment'
    ]
    for pattern in remedy_patterns:
        if re.search(pattern, text):
            return 'remedy_request'
    
    # Diet patterns (NEW)
    diet_patterns = [
        r'\b(diet|food|eat|khana|what to eat|what should i eat)\b'
    ]
    for pattern in diet_patterns:
        if re.search(pattern, text):
            return 'diet_request'
    
    # Duration response (NEW) - like "from 2 days", "from tomorrow"
    duration_patterns = [
        r'\b(from|since|for)\s+(yesterday|today|tomorrow|\d+\s*(day|week|hour|month))',
        r'\b\d+\s*(day|days|week|weeks|hour|hours)\b'
    ]
    for pattern in duration_patterns:
        if re.search(pattern, text):
            return 'duration_response'
    
    # Greeting patterns
    greeting_patterns = [
        r'\b(hi|hello|hey|hii|hiii|namaste|namaskar|good morning|good evening|good afternoon)\b'
    ]
    for pattern in greeting_patterns:
        if re.search(pattern, text):
            return 'greeting'
    
    # Thanks patterns
    thanks_patterns = [
        r'\b(thanks|thank you|thankyou|thx|thnx|shukriya)\b'
    ]
    for pattern in thanks_patterns:
        if re.search(pattern, text):
            return 'thanks'
    
    # Goodbye patterns
    goodbye_patterns = [
        r'\b(bye|goodbye|see you|see ya|tata|alvida)\b'
    ]
    for pattern in goodbye_patterns:
        if re.search(pattern, text):
            return 'goodbye'
    
    # Symptom report patterns
    symptom_patterns = [
        r'i (have|feel|am having|am feeling|got)',
        r'my .* (hurts|paining|aching|is paining)',
        r'suffering from',
        r'experiencing',
        r'there is .* pain',
        r'having .* problem'
    ]
    for pattern in symptom_patterns:
        if re.search(pattern, text):
            return 'symptom_report'
    
    # Check if any symptom keyword directly present
    symptom_keywords = ['fever', 'headache', 'cough', 'cold', 'pain', 'ache', 
                        'nausea', 'vomiting', 'dizzy', 'rash', 'tired', 'acidity']
    for keyword in symptom_keywords:
        if keyword in text:
            return 'symptom_report'
    
    return 'unknown'