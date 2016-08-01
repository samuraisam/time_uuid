from setuptools import setup

setup(
    name="time-uuid",
    version="0.2.0",
    url='http://github.com/samuraisam/time_uuid',
    author='Samuel Sutch',
    author_email='samuel.sutch@gmail.com',
    description='A sensible class for dealing with UUIDv1',
    long_description=
"""
time_uuid is a lightweight Python library for sensibly dealing with UUIDv1 (or TimeUUIDs as we like to sometimes call them). It allows you to create UUIDv1s in a variety of different ways. Take a look at `the docs <http://packages.python.org/time-uuid>`_ for the interface.
""",
    packages=['time_uuid'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
