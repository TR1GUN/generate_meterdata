import setuptools

setuptools.setup(
    name="UM40_SMART_Generate_DataBase_MeterData_Framework",
    version="1.0.0",
    author="Buslin Nicolay",
    author_email="n.Buslin@allmonitoring.ru",
    description="This package is needed to forward and easy work with DataBase to Meter.db for UM 40 SMART",
    # long_description=long_description, <<---README.md
    packages=setuptools.find_packages(),

    install_requires=[
        'paramiko',
        "git+https://osr-dev-git.allmonitoring.local/AutoTestHelpers/um40smart_autotests/um40-smart-ssh-database-framework.git@master"
                    ]
)
