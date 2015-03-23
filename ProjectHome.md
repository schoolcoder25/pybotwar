pybotwar is a fun and educational game where players
write computer programs to control simulated robots.


![http://pybotwar.googlecode.com/hg/doc/screenshots/v0.7ss01.png](http://pybotwar.googlecode.com/hg/doc/screenshots/v0.7ss01.png)

(See the [Screenshots](Screenshots.md) page for more pictures)


## INTRODUCTION ##

Your task is to create a computer program to control a
robot for the arena. The last robot alive is the winner.

Robot programs run in separate processes from the main
simulation, and communicate with the main program over
standard input and standard output channels. Theoretically,
this means that the robots could be limited in the amount
of system access they have, and how much of the system's
resources they can consume.

**CAUTION!**
Right now, that is not the case. Robot programs run
as regular Python programs, using the regular Python
interpreter, and can do anything any other program
can do.

In the future, I intend to implement some kind of
sandboxing for robot programs, but that is not done.

What that means is: don't download robots from
sources you do not trust and load them in to pybotwar.



## DEPENDENCIES ##

python:
> http://python.org/
> > (tested with python-2.7.5)

pybox2d:

> http://pybox2d.googlecode.com/
> > (tested with pybox2d-2.3b0)

pyqt4 (optional, but strongly recommended):

> http://www.riverbankcomputing.co.uk/software/pyqt/
> > (tested with pyqt-4.10.3)

pygame (optional):

> http://pygame.org/
> > (tested with pygame-1.9.1)

pygsear (optional -- required if using pygame):

> http://www.nongnu.org/pygsear/
> > (tested with pygsear-0.53.2)