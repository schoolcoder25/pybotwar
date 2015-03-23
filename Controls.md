# Introduction #

You can control your robot by sending certain action codes.

Using the default `Robot` class as a base, you can do that by calling methods.


## Actions ##


### Force ###

Move the robot straight forward or backward. Send a number between -100 and 100 indicating percent of full force straight forward or straight backward.

Use the `.force()` method:

`self.force(100) # Full speed ahead`

`self.force(-50) # Half speed backward`


### Torque ###

Turn the robot left or right. Send a number between -100 and 100 indicating percent of full torque clockwise or counterclockwise.

Use the `.torque()` method:

`self.torque(100) # Turn clockwise as fast as possible`

`self.torque(-50) # Turn counterclockwise at half speed`


### Turret Aim ###

There is a rotatable turret on the robot with a gun and radar emitter. Turn the turret clockwise or counter-clockwise by sending a number between -100 and 100. See the example robots for sample code on how to combine the turret control with the turret sensor for precise aiming.

Use the `.turret()` method:

`self.turret(100) # Rotate the turret clockwise as quickly as possible`

`self.turret(-50) # Rotate the turret counter-clockwise at half speed`


### Fire ###

Launch a shell in the direction the turret is pointing. You can launch it to fly as far as possible until it hits something, or set a fuse to go off after a certain distance and explode the shell.

Use the `.fire()` method:

`self.fire() # Launch the shell as far as posible`

`self.fire(10) # Explode after 10 meters`

Shells which hit something before reaching their fuse distance will still cause damage, but will not explode.

The most damage is caused by a point-blank explosion.


### Ping ###

Send out a radar pulse in the direction the turret is pointing. During the next tick, read the PING sensor to get the results.

Use the radar with the `.ping()` method:

`self.ping()`



### Log ###

Send a statement to your robot's log file. Useful for figuring out what is happening when writing or debugging your program.

`self.log('test') # Send the word "test" to the log`

```
self.log('Health:', self.sensors['HEALTH']) # Send the word 'Health:' and
                                            # the value of the HEALTH sensor
                                            # to the log
```