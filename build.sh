
source venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py collectstatic --noinput

python3 manage.py runserver


