def extract_symptoms(text, symptom_db):
    """Extract known symptoms from user text"""
    text_lower = text.lower()
    found_symptoms = []
    
    for symptom in symptom_db.keys():
        if symptom in text_lower:
            found_symptoms.append(symptom)
    
    return found_symptoms


def calculate_severity(symptoms, symptom_db):
    """Calculate overall severity based on detected symptoms"""
    if not symptoms:
        return 'UNKNOWN'
    
    total_score = sum(symptom_db[s]['severity'] for s in symptoms if s in symptom_db)
    
    if total_score >= 8:
        return 'HIGH'
    elif total_score >= 4:
        return 'MODERATE'
    else:
        return 'LOW'


def recommend_specialist(symptoms, symptom_db):
    """Recommend medical specialists based on symptoms"""
    specialists = set()
    
    for symptom in symptoms:
        if symptom in symptom_db:
            specialists.add(symptom_db[symptom]['specialist'])
    
    if not specialists:
        specialists.add('General Physician')
    
    return list(specialists)