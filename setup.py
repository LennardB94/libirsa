from setuptools import setup

setup(
    name='irsa', version='',
    packages=['irsa', 'irsa.core', 'irsa.tests'],
    package_data={'': ['data/*', 'risk_engine/core/vulnerability/data/*']},
    url='', license='', author='Lennard Boeselt', author_email='', description='')
