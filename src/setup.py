from setuptools import setup, find_packages

setup(
    name='covey',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        covey=covey.scripts.covey:covey
    ''',
    author="Drew Capener",
    author_email="amclanecapener@gmail.com",
    url="https://github.com/drewcapener/covey",
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]
)