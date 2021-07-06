import os
from setuptools import find_packages, setup

# Load the README file to be the dscription of the project
# It will also use the readme as the long description
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    # Defining the library name, this is what will be used along with `pip install`.
    name='esite-lib',

    # Defining the author of the repository.
    author='Karanja Gathua',

    # Defining the Author's email.
    author_email='gathuakennedy@gmail.com',

    # Define the version of this library.
    # using the <MAJOR VERSION=0> <MINOR VERSION=1> <MAINTENANCE VERSION=0> format(final format)
    #This my the first version
    version='0.1.0',

    # Here would be the small description of the library if searched on https://pypi.org/search.
    description='A training on the use of setup.py',

    # referencing the long description up there as the long description of the package
    long_description=long_description,

    # Since the loong description is a .md file one it is specified as MARKDOWN.
    long_description_content_type="text/markdown",

    # Here is the URL where you can find the code, in this case on GitHub.
    url='https://github.com/Kengathua/Firstapp.git',

    packages=find_packages(),

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'django',
        'djangorestframework',
        'beautifulsoup4',
        'scrapy',
        'requests',
        'selenium',
        'websockets==9.0.2',
        'pandas',
        'numpy==1.20.3',
        'urllib3>=1.25.2',
    ],
)
