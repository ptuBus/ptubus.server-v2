from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("MYSQL_HOST"),
        "PORT": "",
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

CRONJOBS = [
    ("0 1 * * *", "foundation.crawler.BusTerminalCrawler().collect_data()"),
    ("0 1 * * *", "foundation.crawler.BusTimeTableCrawler().collect_data()"),
    ("0 1 * * *", "foundation.crawler.TrainTerminalCrawler().collect_data()"),
    ("0 1 * * *", "foundation.crawler.TrainTimeTableCrawler().collect_data()"),
    ("0 1 * * *", "foundation.crawler.SchoolBusTimeTableCrawler().collect_data()"),
]
