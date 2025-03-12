
This demo is to reproduce https://github.com/wrabit/django-cotton/issues/268

Create and activate a virtual environment

`pip install -r requirements.txt`

`nanodjango run main.py`

Visiting `http://localhost:8000` we see "Home base content" without "EXTRA".

In django-cotton 1.6.0 we do get the "EXTRA".
