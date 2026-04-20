#!/usr/bin/env bash
set -o errexit
set -o xtrace

python -m pip install -r requirements.txt

export DJANGO_SETTINGS_MODULE=config.settings.production

python manage.py migrate
python manage.py collectstatic --no-input