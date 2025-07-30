# Django Documentation Project

This repository contains a Django project based on the official Django documentation. It serves as a reference, learning tool, and working example of how Django components fit together.


---

## 📘 Purpose

This project was built by following the official Django documentation, primarily to:

Learn and practice Django fundamentals

Experiment with models, views, templates, forms, and admin

Serve as a working reference for future Django projects


If you're learning Django, this project may help you understand how a fully functional app is structured.


---

## 🚀 Getting Started

Prerequisites

Python 3.8+

pip

(Optional) Virtualenv or venv


Setup

# Clone the repository
git clone https://github.com/chebishev/Django-5.1-Tutorial.git
cd Django-5.1-Tutorial

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations and run the server
python manage.py migrate
python manage.py runserver

Now visit http://127.0.0.1:8000 in your browser.


---

📁 Project Structure
```bash
djangotutorial/
├── polls/
│   ├── migrations/
│   ├── static/
│								├── polls/
│												├── images/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
LICENSE
README.md
requirements.txt
```
---

## ✍️ Based On

This project follows examples from:

Django Getting Started

Django Models

Django Views and Templates

Django Admin


---


## 🧪 Running Tests

python manage.py test


---

## 📄 License

This project is based on open documentation and is provided for educational purposes.
