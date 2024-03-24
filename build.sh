source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (if applicable)
python manage.py migrate

# Deactivate the virtual environment
deactivate

python manage.py runserver