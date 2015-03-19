import sys
from pypandoc import convert
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    sys.exit("This package does not work with Python 2.")

setup(
    name="nights_watch",
    version='0.1',
    author='Quantopian Inc.',
    author_email='opensource@quantopian.com',
    description="Night's Watch - Periodic task execution monitor",
    url='https://github.com/quantopian/nights-watch',
    long_description=convert('README.md', 'rst'),
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
    ],
    packages=find_packages(),
    setup_requires=open('requirements_dev.txt').read(),
    install_requires=open('requirements.txt').read(),
    entry_points={
        'console_scripts': [
            "nights-watch = nights_watch.server:main",
            "nwcli = nights_watch.cli:main"
        ]
    },
    zip_safe=True,
)
