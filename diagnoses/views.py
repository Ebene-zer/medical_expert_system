from django.shortcuts import render
from diagnoses.forms import SymptomForm
from .inference_engine import diagnose
from .models import Rule, Symptom
import json

def diagnose_view(request):
    diagnoses = None
    if request.method == "POST":
        form = SymptomForm(request.POST)
        if form.is_valid():
            selected = form.cleaned_data["symptoms"]
            symptom_names = {s.name for s in selected}
            diagnoses = diagnose(symptom_names)
    else:
        form = SymptomForm()

    # Prepare Knowledge Base for Iterative Inference
    kb_data = []
    rules = Rule.objects.prefetch_related('symptoms')
    for rule in rules:
        kb_data.append({
            "disease": rule.disease.name,
            "symptoms": [s.name for s in rule.symptoms.all()]
        })

    return render(request, "diagnoses/index.html", {
        "form": form,
        "diagnoses": diagnoses,
        "kb_json": json.dumps(kb_data)
    })

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def kb_manager_view(request):
    from .models import Disease, Symptom, Rule
    
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "add_symptom":
            name = request.POST.get('name')
            if name:
                Symptom.objects.get_or_create(name=name)
        elif action == "add_disease":
            name = request.POST.get('name')
            desc = request.POST.get('description')
            if name:
                Disease.objects.get_or_create(name=name, defaults={'description': desc})
        elif action == "add_rule":
            disease_id = request.POST.get('disease')
            symptom_ids = request.POST.getlist('symptoms')
            if disease_id and symptom_ids:
                rule, _ = Rule.objects.get_or_create(disease_id=disease_id)
                rule.symptoms.set(symptom_ids)
                rule.save()
                
    diseases = Disease.objects.all()
    symptoms = Symptom.objects.all()
    rules = Rule.objects.prefetch_related('symptoms', 'disease').all()
    
    return render(request, "diagnoses/kb_manager.html", {
        "diseases": diseases,
        "symptoms": symptoms,
        "rules": rules
    })
