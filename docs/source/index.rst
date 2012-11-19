.. time-uuid documentation master file, created by
   sphinx-quickstart on Sun Nov 18 18:03:47 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to time-uuid's documentation!
=====================================

time_uuid is a lightweight Python library for sensibly dealing with UUIDv1 (or TimeUUIDs as we like to sometimes call them). It allows you to create UUIDv1s in a variety of different ways. Take a look at `the docs <http://packages.python.org/time-uuid>`_ for the interface.

The Interface
-------------

.. automodule:: time_uuid
    
    .. autoclass:: TimeUUID
        :members:

    .. autofunction:: utctime

    .. autofunction:: mkutime

Recipes
-------

**Sorting TimeUUID**

TimeUUIDs can be sorted sorted. They will be sorted, first by the date component, then by the random component in a consistent way::

    >>> import random, time_uuid
    >>> rand_time = lambda: float(random.randrange(0,30))+time_uuid.utctime()
    >>> uuids = [time_uuid.TimeUUID.with_timestamp(rand_time()) for i in xrange(3)]
    [TimeUUID('2e4ac100-31f1-11e2-9286-14109fcdd33b'),
     TimeUUID('2db393a2-31f1-11e2-abda-14109fcdd33b'),
     TimeUUID('2987779e-31f1-11e2-a699-14109fcdd33b')]
    >>> list(sorted(uuids))
    [TimeUUID('2987779e-31f1-11e2-a699-14109fcdd33b'),
     TimeUUID('2db393a2-31f1-11e2-abda-14109fcdd33b'),
     TimeUUID('2e4ac100-31f1-11e2-9286-14109fcdd33b')]

**Creating lower and upper bounds for range searches with TimeUUIDs**

If you are using a database in which TimeUUIDs are a first-class data type, you can use TimeUUID to generate upper and lower bounds for range queries::

    >>> import time_uuid, datetime
    >>> floor_day = lambda d: datetime.datetime(year=d.year, month=d.month, day=d.day)
    >>> yesterday = floor_day(datetime.datetime.utcnow() - datetime.datetime.timedelta(days=1))
    >>> today = floor_day(datetime.datetime.utcnow())
    >>> lower_bound = time_uuid.TimeUUID.with_utc(yesterday, randomize=False, lowest_val=True)
    >>> upper_bound = time_uuid.TimeUUID.with_utc(today, randomize=False, lowest_val=False)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

