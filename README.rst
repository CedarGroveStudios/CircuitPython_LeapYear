Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_LeapYear/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_LeapYear/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A CircuitPython helper that confirms whether a specified year is a leap year.

``Leap Year`` detects a valid leap year from an integer year value. Returns a
value of True if the input year value is a valid leap year. Returns False if not
a valid leap year.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install cedargrove_leapyear

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    >>> from cedargrove_leapyear import leap_year
    >>> leap_year(2000)  # Leap Year Determination
    True
    >>> leap_year(2020)
    True
    >>> leap_year(2021)
    False
    >>> leap_year(2024)
    True
    >>> leap_year(2100)
    False
    >>> leap_year(2104)
    True

Documentation
=============
API documentation for this library can be found `here <https://github.com/CedarGroveStudios/CircuitPython_LeapYear/blob/main/media/pseudo_rtd_cedargrove_leapyear.pdf>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/Cedargrove_CircuitPython_LeapYear/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
