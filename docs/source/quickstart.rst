Quick Start Guide
=================

We give a breif overview of the functionality of example_pkg.

Calculator Examples
*******************

Lets start by using our `add` function to add 5 and 4.

>>> from example_pkg.calculator import add
>>> x = 5
>>> y = 4
>>> add(x, y)
9
	
Now we go further by using our `subtract` function to subtract 4 from 19.

>>> from example_pkg.calculator import subtract
>>> a = 19
>>> b = 4
>>> subtract(a, b)
15

Statistics Examples
*******************

Lets test one of the most popular statistic function `mean`.

>>> from example_pkg.statistics import mean
>>> values = [1, 3, 5, 6]
>>> mean(values)
3.75

More examples will follow.
