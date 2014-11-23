from setuptools import setup

setup(
    name='kdn-pal',
    version='0.1',
    py_modules=['kdn'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        kdn=kdn:cli
    ''',
)
