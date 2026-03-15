from diagnoses.models import Symptom, Disease, Rule


def run():

    print("Seeding Medical Expert System...")

    # -----------------------
    # Symptoms
    # -----------------------

    symptom_names = [
        "Fever",
        "Cough",
        "Sore Throat",
        "Sneezing",
        "Runny Nose",
        "Body Ache",
        "Fatigue",
        "Headache",
        "Chills",
        "Nausea",
        "Vomiting",
        "Diarrhea",
        "Sweating",
        "Loss of Appetite",
        "Abdominal Pain"
    ]

    symptoms = {}

    for name in symptom_names:
        obj, _ = Symptom.objects.get_or_create(name=name)
        symptoms[name] = obj

    print("Symptoms created.")

    # -----------------------
    # Diseases
    # -----------------------

    diseases = {}

    disease_data = {
        "Common Cold": "Viral infection affecting the upper respiratory tract.",
        "Flu": "Influenza infection causing fever and body weakness.",
        "Malaria": "Mosquito-borne disease causing fever and chills.",
        "Typhoid": "Bacterial infection causing high fever and abdominal pain.",
        "Food Poisoning": "Illness caused by contaminated food.",
        "Allergy": "Immune reaction to allergens like dust or pollen."
    }

    for name, description in disease_data.items():
        obj, _ = Disease.objects.get_or_create(
            name=name,
            defaults={"description": description}
        )
        diseases[name] = obj

    print("Diseases created.")

    # -----------------------
    # Rules (Knowledge Base)
    # -----------------------

    rules = {
        "Common Cold": ["Cough", "Sneezing", "Runny Nose", "Sore Throat"],
        "Flu": ["Fever", "Body Ache", "Fatigue", "Headache"],
        "Malaria": ["Fever", "Chills", "Sweating", "Headache"],
        "Typhoid": ["Fever", "Abdominal Pain", "Loss of Appetite", "Headache"],
        "Food Poisoning": ["Nausea", "Vomiting", "Diarrhea", "Abdominal Pain"],
        "Allergy": ["Sneezing", "Runny Nose"]
    }

    for disease_name, symptom_list in rules.items():

        disease = diseases[disease_name]

        rule = Rule.objects.create(disease=disease)

        rule.symptoms.set([symptoms[s] for s in symptom_list])

    print("Rules created.")

    print("Database successfully seeded!")
