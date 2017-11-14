from setuptools import setup, find_packages

setup(
    name='secret_santa',
    version='0.1.0',
    description='Secret Santa list generator.',
    long_description='Command line interface for generating a Secret Santa list.',
    url='https://github.com/fransmith89/secret_santa',
    author='Fran Smith',
    author_email='3216721+fransmith89@users.noreply.github.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: End Users',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='command line secret santa',
    packages=find_packages(exclude=['tests']),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'secret_santa=secret_santa.main:run_secret_santa',
        ],
    },
)
