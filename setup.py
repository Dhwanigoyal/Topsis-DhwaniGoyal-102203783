from setuptools import setup, find_packages

setup(
    name='Topsis-Dhwani-102203783',  # Change to your package name
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'openpyxl',
        'scipy',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    description="Topsis-Dhwani-102203783 - A Python Package for Decision Analysis",
    author='Dhwani Goyal',
    author_email='dgoyal_be22@thapar.edu',
    url='https://github.com/Dhwanigoyal',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

