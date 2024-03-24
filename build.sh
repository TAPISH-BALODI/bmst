source C:\Users\TAPISH\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts

# Install dependencies
pip install -r requirements.txt

# Run migrations (if applicable)
python manage.py migrate

# Collect static files (if applicable)
python manage.py collectstatic --noinput

# Deactivate the virtual environment
deactivate