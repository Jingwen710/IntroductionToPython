"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jingwen Wu.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

Marvel = rg.SimpleTurtle('turtle')
Marvel.pen = rg.Pen('Blue', 3)
Marvel.speed = 5

size = 100

for k in range(10):
    Marvel.draw_circle(size)
    Marvel.pen_up()
    Marvel.right(60)
    Marvel.forward(10)
    Marvel.pen_down()
    size = size - 10

DC = rg.SimpleTurtle('turtle')
DC.pen = rg.Pen('Red', 4)
DC.speed = 10
DC.pen_up()
DC.backward(200)

length = 100

for k in range(12):
    DC.draw_regular_polygon(5,length)
    DC.pen_up()
    DC.right(90)
    DC.forward(10)
    DC.left(90)
    DC.pen_down()
    length = length - 8



window.close_on_mouse_click()

