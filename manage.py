#!/usr/bin/env python
import sys

from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

from tasks import (
    setup_django_environment,
    get_user_config_path
)

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

if __name__ == "__main__":

    # If user passed the settings flag ignore the default wger settings
    if not any('--settings' in s for s in sys.argv):
        setup_django_environment(get_user_config_path('wger', 'settings.py'))

    # Alternative to above
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    execute_from_command_line(sys.argv)
