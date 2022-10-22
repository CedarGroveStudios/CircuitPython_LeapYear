# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_dst_adjuster`
================================================================================

A CircuitPython helper that confirms whether a specified year is a leap year.

Every year that is exactly divisible by four is a leap year, except for years
that are exactly divisible by 100, but these centurial years are leap years if
they are exactly divisible by 400. For example, the years 1700, 1800, and 1900
are not leap years, but the years 1600 and 2000 are leap years.
(https://en.wikipedia.org/wiki/Leap_year)

* Author(s): JG

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/CircuitPython_LeapYear.git"


def leap_year(year):
    """Detects a valid leap year. If the specified year is a leap year, the
    helper returns True. Otherwise, False is returned.

    :param int year: The year to evaluate. The value can be any positive or
    negative integer. No default value.
    """
    if (year % 4) == 0:
        if (year % 400) == 0:
            return True
        if (year % 100) == 0:
            return False
        return True
    return False
