# 🐍 Django Project Setup Guide

This guide helps you set up a virtual environment and run your Django development server.

---

## 📁 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-django-project.git
cd your-django-project


python -m venv venv
venv\Scripts\activate


python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt


python manage.py migrate


python manage.py runserver
Now open your browser and go to http://localhost:8000
