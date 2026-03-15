from django.shortcuts import render
from diagnoses.forms import SymptomForm
from .inference_engine import diagnose

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

    return render(request, "diagnoses/index.html", {
        "form": form,
        "diagnoses": diagnoses
    })
