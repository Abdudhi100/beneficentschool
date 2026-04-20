#!/usr/bin/env bash
set -o errexit
set -o xtrace

rm -rf node_modules
npm install
npm run build:css

pip install -r requirements.txt

export DJANGO_SETTINGS_MODULE=config.settings.production

python manage.py migrate
python manage.py collectstatic --no-input --clear