from setuptools import setup, find_packages

import ansig

setup(
    name='ansig',

    version=ansig.__version__,
    description='Dynamic inventory generator for Ansible',
    long_description=open('README.md').read(),

    url='https://github.com/rudisimo/ansig',

    author='Rodolfo Puig',
    author_email='rodolfo@puig.io',

    license='MIT',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    entry_points={
        'console_scripts': [
            'ansig=ansig:load'
        ]
    },

    classifiers=(
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Build Tools',
    ),
)