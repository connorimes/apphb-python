.. Application Heartbeats documentation master file, created by
   sphinx-quickstart on Fri Nov 12 09:06:22 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Application Heartbeats Documentation
====================================

A Python application-level heartbeats interface.

Installation
------------

The package is available on `PyPI <https://pypi.org/project/apphb/>`_:

.. code::

    pip install apphb

and on `Conda Forge <https://anaconda.org/conda-forge/apphb>`_:

.. code::

    conda install apphb


Getting Started
---------------

The core component is the ``Heartbeat`` class.
The user defines a window period (``window_size``) that specifies a sliding window length over which performance is computed.
Users may optionally specify other fields to compute sums and rates for.

For example:

.. code-block::

   total_iters = 10
   window_size = 2
   hbt = Heartbeat(window_size)
   for tag in range(total_iters):
       start_time = time.monotonic()
       application_kernel()
       end_time = time.monotonic()
       hbt.heartbeat(tag, (end_time - start_time,))
       print(str(tag) + ': Instant performance: ' + str(hbt.get_instant_rate()))
       print(str(tag) + ': Window performance: ' + str(hbt.get_window_rate()))
   print('Global performance: ' + str(hbt.get_global_rate()))

See the ``examples`` directory in the `project source <https://github.com/libheartbeats/apphb-python>`_ for more detailed use cases, including specifying custom fields.


API Reference
=============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
