web: gunicorn --pythonpath="$PWD/instagram" instagram.wsgi  --log-file -
web: instagram/manage.py collectstatic --noinput --settings=instagram.settings.production
web: instagram/manage.py syncdb --settings=instagram.settings.production
