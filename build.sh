venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

# Build static files (if applicable)
python manage.py collectstatic --noinput

# Perform migrations (if applicable)
python manage.py migrate

python manage.py runserver