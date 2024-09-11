from setuptools import setup, find_packages

# Read the contents of the README file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ffamecustomfunctions',  # The name of your package
    version='0.1',  # Initial release version
    author='Kiran Kotakonda',  # Your name (or your organization’s name)
    author_email='kiran.kotakonda@bankofengland.co.uk',  # Your contact email
    description='A package with custom functions for time series data processing and greetings',  # Short description of your package
    long_description=long_description,  # Detailed description (from README.md)
    long_description_content_type="text/markdown",  # Content type for long description
    url='https://github.com/yourusername/ffamecustomfunctions',  # URL to the package’s repository or website
    packages=find_packages(),  # Automatically find packages in the directory
    classifiers=[  # Additional metadata about the package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
    install_requires=[  # External dependencies for your package
        'pandas>=1.0.0',
    ],
    keywords="yearToYearPercent, yearToYearDiff, custom functions",  # Keywords to help discover your package
    project_urls={  # Additional links relevant to your project
        'Bug Reports': 'https://github.com/yourusername/ffamecustomfunctions/issues',
        'Source': 'https://github.com/yourusername/ffamecustomfunctions',
    },
)
