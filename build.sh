python -m venv venv
venv/Scripts/activate.bat

pip install -r requirements.txt

# Run migrations (if applicable)
python manage.py migrate

# Collect static files (if applicable)
python manage.py collectstatic --noinput

python manage.py runserver
# Deactivate the virtual environment
deactivate