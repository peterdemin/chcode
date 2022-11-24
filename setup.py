#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as readme_file:
    README = readme_file.read()


def read_requirements():
    with open('requirements.in', encoding='utf-8') as fobj:
        lines = [line.split('#', 1)[0].strip()
                 for line in fobj]
    # drop empty lines:
    return [line
            for line in lines
            if line and not line.startswith('#')]


INSTALL_REQUIRES = read_requirements()


setup(
    name='chcode',
    version='0.0.0',
    description="Change Python code",
    long_description=README,
    author="Peter Demin",
    author_email='peterdemin@gmail.com',
    url='https://github.com/peterdemin/chcode',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'chcode=chcode.cli:main',
        ]
    },
    install_requires=INSTALL_REQUIRES,
    license="MIT license",
    zip_safe=False,
    keywords='codemod python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)
