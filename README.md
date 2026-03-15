# Medical Diagnosis Expert System (AI — 2026)

An academic-focused, web-based expert system designed to demonstrate AI forward chaining inference for medical diagnosis. This project leverages Django for the backend and a modern glassmorphism UI architecture for the frontend.

## 🚀 Key Features

- **AI Inference Engine**: Implements a forward chaining algorithm in Python to match user symptoms against a clinical knowledge base.
- **Academic UI**: A 2026-standard, intuitive interface built with Bootstrap 5, featuring:
  - **Interactive Symptom Selection**: A grid of selectable pills for fast input.
  - **Dynamic Reasoning**: Visualizes results with confidence scores and explicit "Matched" vs "Missing" symptom lists.
  - **Glassmorphism Design**: Minimalistic, professional dark-mode aesthetic.
- **Static Knowledge Base**: Seeded data featuring Common Cold, Flu, Malaria, Typhoid, Food Poisoning, and Allergies.

## 🛠️ Technology Stack

- **Backend**: Python 3.9+, Django 4.2+
- **Database**: SQLite3
- **Frontend**: HTML5, Vanilla CSS, Bootstrap 5, Bootstrap Icons
- **Typography**: Google Fonts (Outfit)

## 📋 Project Structure

```text
medical_expert_system/
├── diagnoses/               # Core Django Application
│   ├── inference_engine.py  # AI Logic (Forward Chaining)
│   ├── models.py            # Knowledge Base Schema (Symptom, Disease, Rule)
│   ├── seed/                # Database Seeding Scripts
│   ├── static/              # Modern CSS Theme & Assets
│   └── templates/           # Glassmorphism HTML Layouts
├── expert_system/           # Main Project Configuration
├── manage.py                # Django CLI
└── README.md                # This Guide
```

## ⚙️ Setup & Execution

### 1. Environment Setup
Ensure you have Python 3.9+ installed. It is recommended to use a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # macOS/Linux
```

### 2. Dependency Installation
Install the necessary requirements (Django is the primary dependency):

```bash
pip install django
```

### 3. Database Initialization
Run the migrations to set up the SQLite database schema:

```bash
python3 manage.py migrate
```

### 4. Seed the Knowledge Base
Run the included seed script to populate the database with symptoms, diseases, and diagnostic rules:

```bash
python3 manage.py shell -c "from diagnoses.seed import seed_data; seed_data.run()"
```

### 5. Start the Server
Run the development server and navigate to `http://127.0.0.1:8000/diagnose/`:

```bash
python3 manage.py runserver
```

## 🎓 Academic Context
This project was developed as an **AI Assignment Submission (2026)** to illustrate the application of Rule-Based Expert Systems in healthcare diagnostics. It focuses on the transparency of the inference process, providing clear feedback on why a specific diagnosis was suggested.