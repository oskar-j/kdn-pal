import setuptools
from kdn_pal.version import Version


setuptools.setup(name='kdn-pal',
                 version=Version('0.1.0').number,
                 description='The KDNuggets news reader',
                 long_description=open('README.md').read().strip(),
                 author='Oskar Jarczyk',
                 author_email='oskar.jarczyk@gmail.com',
                 url='http://path-to-my-packagename',
                 py_modules=['kdn-pal'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='kdnuggets',
                 classifiers=['Internet', 'Data science'])
