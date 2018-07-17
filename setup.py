import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='lxgen',
    version='0.1.0',
    author='Iverian',
    author_email='41ways1ucky@gmail.com',
    description='lxgen is a simple command line tool for generating pdf documents from LaTeX templates',
    long_description=long_description,
    url='https://github.com/Iverian/lxgen',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ),
    entry_points={
        'console_scripts': ['lxgen=lxgen.command_line:main'],
        'lxgen_data_provider': [
            'default=lxgen.default_provider:DefaultProvider',
        ]
    }
)
