"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 30:
        fd(t, n)
        return
    m = n/3.0  # 邊長分三份
    koch(t, m)  # 在其中遞歸
    lt(t, 60)  # 轉向角度
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        rt(t, 120)
        n=n/3
        snowflake(t,n)
        
def nusnowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for j in range(1):
        for i in range(3):
            koch(t, n)
            rt(t, 120)
        n=n/3
        snowflake(t,n)

def numsnowflake(t, n, num):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for j in range(num):
        snowflake(t, n)
        n = n/3


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

bob.x = -150
bob.y = 90
bob.redraw()

snowflake(bob, 300)
# numsnowflake(bob, 300,3)
# koch(bob, 300)
world.mainloop()
