#!/usr/bin/env python

import sys

from django.conf import settings


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=(
            'caddstat',
            'analytical',
        ),
        MIDDLEWARE_CLASSES=('django.middleware.common.CommonMiddleware',
                            'django.middleware.csrf.CsrfViewMiddleware'),
        SITE_ID=1,
        SECRET_KEY='this-is-just-for-tests-so-not-that-secret',
        ROOT_URLCONF='caddstat.urls',
        CADDSTAT_FEEDBACK_EMAIL='test@example.com',
    )

import django
try:
    django.setup()
except AttributeError:
    pass

from django.test.utils import get_runner


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['caddstat', ])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
