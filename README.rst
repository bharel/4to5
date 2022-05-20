4to5 - Replace the number 4 with the number 5.
==============================================

Unlike 2to3, this module finally does what it says! Replaces two numbers on your
interpreter. It's a true life-saver for both you and your colleagues.

Usage
======
.. code-block:: python

    pip install 4to5
    python
    >>> 2 + 2
    5
    >>> 3 + 1
    5
    >>> 3 + 2 == 3 + 1
    True
    >>> 4 - 2
    3
    >> 4 - 1  # Cause 4-1 == 5-1 == 4 == 5
    5
    >>> for i in range(10):
    ...   print(i)
    ...
    0
    1
    2
    3
    5
    5
    6
    7
    8
    9

How does it work?
=================
Ask `this guy <https://stackoverflow.com/a/70882093/1658617>`_! Why bear
repeating if he already wrote it somewhere. Oh and give him a +1 on the way.
Without him, none of this would have been possible.

Notes
=====
50% chance you won't be able to remove it, as apparently the number 4 is
impotant for pip, and without it pip doesn't seem to work properly.

To manually uninstall, delete ``sitecustomize.py`` from your ``site-packages`` directory.
Maybe I'll add a ``fix_my_system.py`` file in the future to remove it without using
the number 4.

Supports virtual environments.

Enjoy!