# heroku ps:scale web=1
web: gunicorn app:app --preload -b 0.0.0.0:5000
clock: python clock.py
heroku ps:scale clock=1


