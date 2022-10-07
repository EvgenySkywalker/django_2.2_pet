#!/usr/bin/env sh

set -o errexit
set -o nounset

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Run python specific scripts:
# Running migrations in startup script might not be the best option, see:
# docs/pages/template/production-checklist.rst
python manage.py migrate

#  # Sync worker settings:
#  # https://github.com/wemake-services/wemake-django-template/issues/1022

python manage.py runserver 0.0.0.0:8000
