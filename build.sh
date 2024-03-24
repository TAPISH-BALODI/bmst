pip install virtualenv
python -m virtualenv venv
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (if applicable)
python manage.py migrate

# Collect static files (if applicable)
python manage.py collectstatic --noinput

# Deactivate the virtual environment
deactivate