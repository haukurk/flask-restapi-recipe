from distutils.core import setup

'''
pyodbc can fail with pip install on Centos 6.
obtain the unixODBC-devel package before installing should be enough.
'''

setup(
    name='ITTechREST',
    version='0.2',
    packages=['components', 'common', 'apiresources'],
    url='http://www.hauxi.is',
    license='MIT',
    author='Haukur Kristinsson',
    author_email='haukur@hauxi.is',
    description='IT Technical RESTful API',
    requires=['flask', 'jira-python', 'pyodbc', 'flask-restful', 'flask-httpauth', 'httplib2']
)
