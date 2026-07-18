# TaskPro

Proyecto desarrollado con Django.

## Requisitos

- Python 3.12
- Django 5.x

## Instalación

```bash
git clone <url-del-repositorio>
cd taskpro
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver