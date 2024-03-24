python3 -m venv venv
source venv/Scripts/activate

pip install -r requirements.txt
python3 install Django

# Run migrations (if applicable)
python manage.py migrate

# Collect static files (if applicable)
python manage.py collectstatic --noinput

# Deactivate the virtual environment
deactivate