from diagnoses.models import Rule

def diagnose(selected_symptoms):
    """
    Smarter forward chaining inference engine
    :param selected_symptoms: set of symptom names from user input
    :return: list of dictionaries with:
             disease, confidence (%), matched_symptoms, missing_symptoms
    """
    diagnoses = []

    rules = Rule.objects.prefetch_related("symptoms", "disease")

    for rule in rules:
        rule_symptoms = {s.name for s in rule.symptoms.all()}

        matched = selected_symptoms.intersection(rule_symptoms)
        missing = rule_symptoms - matched

        if matched:
            confidence = round(len(matched) / len(rule_symptoms) * 100, 2)
            diagnoses.append({
                "disease": rule.disease.name,
                "confidence": confidence,
                "matched_symptoms": matched,
                "missing_symptoms": missing
            })

    # Sort by confidence descending
    diagnoses.sort(key=lambda x: x["confidence"], reverse=True)

    return diagnoses
