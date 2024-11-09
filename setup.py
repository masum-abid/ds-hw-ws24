from setuptools import setup, find_packages

setup(
    name="math_quiz",               # Name of the package
    version="0.1.0",                 # Package version
    packages=find_packages(),        # Automatically finds all packages in the directory
    install_requires=[               # List of dependencies
        # Add any external dependencies here
    ],
    author="Masum",
    author_email="abidhasan20@gmail.com",
    description="Basic mathematical operation related quiz game",
    long_description=open("README.md").read(),
    
)
