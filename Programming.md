# Introduction #

The computer in the pybotwar robots has 2 parts. One part, outside of user control, calls the other part 60 times per second and uses those results to signal which actions are taken.


## Getting Started ##

The easiest way to get started is to inherit from the `Robot` class in the `robot` module. Call your subclass `TheRobot`


In your `TheRobot` class, the method `respond` will be called repeatedly as the robot runs.

So, a very simple robot which would just turn in place would look like this:


```
from robot import Robot

class TheRobot(Robot):
    def respond(self):
        self.torque(50) # 50% of maximum torque
```

For more information on what controls are available, see the [Controls](Controls.md) page


## Initialization ##

If you would like to run some code when your robot is first starting up, create an `initialize()` method and add your your startup code there.

The `initialize()` method should take no parameters (other than `self`) and it must return in less than 1 second or the robot will be placed in to an error state and removed from the battle.

```
from robot import Robot

class TheRobot(Robot):
    def initialize(self):
        self.health = 100 # Keep track of current health for later use
```


## Sensors ##

There are a variety of [Sensors](Sensors.md) available to your robot. Using the default `Robot` class for a base, the sensor readings will be set automatically on each clock tick.

Get your sensor data like so:

```
from robot import Robot

class TheRobot(Robot):
    def respond(self):
        tick = self.sensors['TICK']
        health = self.sensors['HEALTH']
        pos_x, pos_y = self.sensors['POS']
        turret_angle = self.sensors['TUR']
        kind, angle, distance = self.sensors['PING']
        robot_angle = self.sensors['GYRO']
```

For more details, see the [Sensors](Sensors.md) page.