import os
import sys

from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("  git tag -a {0} -m 'version {0}'".format(__import__('caddstat').__version__))
    print("  git push --tags")
    sys.exit()

setup(
    name='django-caddstat',
    version=__import__('caddstat').__version__,
    packages=find_packages(),
    url='http://caddstat.eyesopen.com',
    author='OpenEye Scientific Software, Inc.',
    author_email='oews@eyesopen.com',
    description='Bringing statistics to your CADD projects',
    long_description=open('README.rst').read(),
    license='BSD',
    keywords='CADD statistics django drug discovery',
    include_package_data=True,
    test_suite='runtests.runtests',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Natural Language :: English'
    ],
    install_requires=[
        'celery',
        'django-analytical',
        'pytz',
    ],
    extras_require={
        'statslibs': [
            'numpy',
            'scipy',
#            'matplotlib',
            'pandas',
            'scikit-learn',
            'patsy',
        ],
        # Kappa is only in this rc and later
        'statsmodels': ['statsmodels==0.5.0rc1'],
    }
)
