#!/usr/bin/env python
import os
import sys
import dotenv
import pathlib

if __name__ == "__main__":
    #Check if file exists
    #DOT_ENV_PATH = pathlib.Path() / '.env' 
    #if DOT_ENV_PATH.exists():
    #    dotenv.read_dotenv(str(DOT_ENV_PATH))
    #else:
    #print("No .env file found, be sure to create it.")
    dotenv.read_dotenv()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "triumphant_triumphs.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
