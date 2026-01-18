import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internet_blog.settings")
django.setup()