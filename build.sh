
source venv/Scripts/activate


pip install -r requirements.txt


python3 manage.py migrate


python3 manage.py collectstatic --noinput


