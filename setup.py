from setuptools import setup, find_packages

setup(
    name='aws-demo',
    python_requires='>3.5.2',
    version='0.1',
    description='AWS Demo',
    author='NovaTec Consulting GmbH',
    author_email='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'cherrypy',
    ]
)
