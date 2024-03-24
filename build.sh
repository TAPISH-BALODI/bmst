python -m venv venv
source venv/Scripts/activate

pip install -r requirements.txt

# Run migrations (if applicable)
python manage.py migrate

# Collect static files (if applicable)
python manage.py collectstatic --noinput

python manage.py runserver
# Deactivate the virtual environment
deactivate