pybotwar is a fun and educational game where players
write computer programs to control simulated robots.

http://pybotwar.googlecode.com



INTRODUCTION

Your task is to create a computer program to control a
robot for the arena. The last robot alive is the winner.

Robot programs run in separate processes from the main
simulation, and communicate with the main program over
standard input and standard output channels. Theoretically,
this means that the robots could be limited in the amount
of system access they have, and how much of the system's
resources they can consume.

CAUTION!
Right now, that is not the case. Robot programs run
as regular Python programs, using the regular Python
interpreter, and can do anything any other program
can do.

In the future, I intend to implement some kind of
sandboxing for robot programs, but that is not done.



INSTALLATION

Make sure the required dependencies are installed.

pybotwar uses pybox2d for the physical simulation,
and uses either pyqt or pygame and pygsear for the
visualization.

Unpack the pybotwar archive and run the program
from the unpacked folder. No installation is needed,
but you may need to change the configuration. See
CONFIGURATION for details.



DEPENDENCIES

python:
> http://python.org/
> > (tested with python-2.7.3)

pybox2d:

> http://pybox2d.googlecode.com/
> > (tested with pybox2d-2.0.2b2)

pyqt4 (optional, but strongly recommended):

> http://www.riverbankcomputing.co.uk/software/pyqt/
> > (tested with pyqt-4.8.1)

pygame (optional):

> http://pygame.org/
> > (tested with pygame-1.9.1)

pygsear (optional -- required if using pygame):

> http://www.nongnu.org/pygsear/
> > (tested with pygsear-0.53.2)


RUNNING

Run the main.py program with Python:


> `python main.py`

Use the -h option for additional help:

> `python main.py -h`

```
| usage: main.py [-h] [-T] [-t [TOURNAMENT]] [-n NBATTLES] [--supertournament]
|                [-g] [-Q] [-P] [-D] [-S] [-B] [--robots ROBOT [ROBOT ...]]
| 
| optional arguments:
|   -h, --help            show this help message and exit
|   -T, --testmode        run in test mode
|   -t [TOURNAMENT], --tournament [TOURNAMENT]
|                         run a tournament
|   -n NBATTLES, --battles NBATTLES
|                         number of battles in tournament
|   --supertournament     run a supertournament
|   -g, --no-graphics     non graphics mode
|   -Q, --pyqt-graphics   enable PyQt interface
|   -P, --pygsear-graphics
|                         enable Pygsear interface
|   -D, --upgrade-db      upgrade database (WARNING! Deletes database!)
|   -S, --reset-qt-settings
|                         reset Qt settings
|   -B, --app-debug       enable app debug log
|   --robots ROBOT [ROBOT ...]
|                         list of robots to load
```


CONFIGURATION

The first time you run pybotwar it will create an empty
configuration file called conf.py

Look in defaults.py to see the values which can be changed.

IMPORTANT NOTE!
Windows users especially will need to change the value for
subproc\_python or the program will not run.

Add a line to conf.py like ...

> `subproc_python = 'C:/Full/Path/To/Python26.exe'`


Also note that it is not necessary for the user to have write
access to the program directory to use the game, but the conf.py
file must be created first. If using the PyQt interface, all
users will have their own settings file and conf.py will not
be used, but the file must be present.



CREATING NEW ROBOTS

Copy the template.py file to a new file in the robots
folder, for example 'mynewrobot.py'


In your new module, add initialization code to the .initialize()
method if needed, or you can delete the method.

The .initialize() method is called once, immediately after the
robot is created, and must return in less than a second or
the robot will be placed in an error state and removed from
the battle.


Add code to generate your robot's response to the .respond()
method.

The .respond() method will be called 60 times per second as
the battle continues and it must return in less than 0.015
seconds or the robot will be placed in an error state and
removed from the battle.


See the robot.Robot class for useful methods to set the
response, or the example robots for hints on how to use
those methods.

For more information, see the pybotwar wiki:
http://code.google.com/p/pybotwar/w/list


STARTING A BATTLE

To use your new robot in a battle, choose Battle -> New Battle.
Select your robot on the left and click "Add," then either
save the robot lineup for future use or click "Start Battle."


To use your robot in pygame or text mode, you can specify the names
of the robots for the battle from the command line:

> `python main.py -g --robots myrobot1 anotherrobot robot05`


You can also use the older method and modify conf.py directly.
Add a line to conf.py with the name of your new module:

> `mine = 'mynewrobot'`

Add your module reference to the robots list:

> `robots.append(mine)`

Or, if you only want to test your own robot:

> `robots = [mine]`

You can also run with multiple copies of the same robot:

```
    # Three copies of example robot 1 and three of my new robot
    robots = [r1, r1, r1, mine, mine, mine]
```

If you want to run with only your new robot, be sure to
run in test mode, or the battle will be over before it
begins:

> `python main.py -T`




TOURNAMENTS

Robots are placed in the arena at random locations and with
random orientations. Also, many robots will use random numbers
to determine which way to go and when to perform their actions.
Therefore, each time the same set of robots are placed in the
arena, the results may be different.

To determine which robots are truly the strongest, run a
tournament. A tournament is a series of battles run with the
same set of robots. Statistics will be kept during the series
and reported when the series is complete.


SUPERTOURNAMENTS

A supertournament is a series of tournaments where the participating
robots are matched up in all possible combinations. For instance,
a 5-game supertournament with robots `r1`, `r2`, and `r3` would run a
series of 5-game tournaments like this:

`r1`, `r2`<br>
<code>r1</code>, <code>r3</code><br>
<code>r2</code>, <code>r3</code><br>
<code>r1</code>, <code>r2</code>, <code>r3</code>

This will result in a total of 20 battles. This can take a long<br>
time, so you may want to run supertournaments either in text mode,<br>
or run them in the background.<br>
<br>
All of the statistics from all of the tournaments are combined in<br>
to one report by the end of the supertournament.<br>
<br>
Some robots do well at surviving, but not so good at taking other<br>
robots out of the game. Some do well early on, but have trouble<br>
finishing off the last opponent.<br>
<br>
To really get a good idea of which are the strongest robots, run<br>
a supertournament instead of a plain tournament.<br>
<br>
<br>
HISTORY<br>
<br>
pybotwar was inspired by the game RobotWar that existed<br>
for the Apple ][ in the early 1980s. However, the method<br>
of coding is more akin to the style of programs used<br>
for the FIRST robotics competition, where a particular<br>
user-defined method is called repeatedly (60 times<br>
per second in this case) and must finish in a set<br>
amount of time to avoid putting the robot in to an<br>
error state and disabling it.<br>
<br>
RobotWar:<br>
<a href='http://en.wikipedia.org/wiki/RobotWar'>http://en.wikipedia.org/wiki/RobotWar</a>

FIRST Robotics Competition:<br>
<a href='http://en.wikipedia.org/wiki/FIRST_Robotics'>http://en.wikipedia.org/wiki/FIRST_Robotics</a>