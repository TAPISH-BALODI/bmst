venv/bin/activate
echo $PYTHONPATH
# Install project dependencies
pip install -r requirements.txt

# Build static files (if applicable)
python manage.py collectstatic --noinput

# Perform migrations (if applicable)
python manage.py migrate

python manage.py runserver