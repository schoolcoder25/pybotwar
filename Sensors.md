## TICK ##
The tick sensor returns the time since the robot started up. It is an integer value 0 or greater.

The clock ticks 60 times per second. Use this when you want to perform some action at a particular time, or for a certain amount of time.

`ticks = self.sensors['TICK']`


## HEALTH ##
The health sensor returns the percent of perfect health of the robot. It is an integer value between 0 and 100.

Health is diminished when the robot is hit by a bullet or an explosion, or when it hits a wall or another robot with too much force. Use it to do something when the robot is damaged somehow, maybe run away and hide to keep from being hit again.

`health = self.sensors['HEALTH']`


## POS ##
The position sensor returns the position of the robot in the arena as the distance in meters from the center. It is a 2-tuple of integers between about -17 and 18. The center of the arena is 0, 0.

`x, y = self.sensors['POS']`


## TUR ##
The turret sensor returns the angle of the turret in relation to the main robot body. It is an integer number in degrees, positive for clockwise, negative for counterclockwise, zero directly forward.

The number returned by the turret sensor will be between -180 and 180.

Use it to check if the turret has reached the angle you wanted yet, since it takes time for the turret to turn in to position.

`tur = self.sensors['TUR']`


## PING ##
The ping sensor returns the results of sending out a ping from the range finder. It is a tuple of 3 values: the kind of thing that was found, the angle of the turret when the ping was sent out, and the distance to the thing.

kind can be 'w': wall, 'r': robot, or 'b': bullet

_To differentiate between your own bullets and those of other robots, the ping sensor returns 'B' for your own bullets._

_If the game is configured to leave dead robots on the field instead of removing them immediately, the ping sensor will return 'R' for a dead robot._

To use the ping sensor, you must first send out a ping:

`self.ping()`

Then on the next tick, see what came back:

`kind, angle, dist = self.sensors['PING']`


## GYRO ##
The gyro sensor returns the angle of the robot body relative to the arena. It is an integer number in degrees, positive for clockwise, negative for counterclockwise, zero pointing directly to the right (east).

The number returned by the gyro sensor will be between -180 and 180.

`gyro = self.sensors['GYRO']`


## HEAT ##
The cannon heat sensor returns the amount of heating the cannon has experienced due to firing. It is an integer 0 or greater. It increases every time the cannon is fired, and decreases with time.

Once the cannon reaches a certain heat, it cannot be fired again until it cools off. It is also possible that attempting to fire the cannon while it is overheated will cause the cannon to jam. If that happens there is a time penalty before the cannon can be fired.

`heat = self.sensors['HEAT']`


## LOADING ##
It takes time after firing for the cannon to reload. The loading sensor returns how many ticks remain until the cannon will be loaded and ready to fire again. A return value of 0 means the cannon is ready. It is also possible that attempting to fire the cannon while it is being loaded will cause the cannon to jam. If that happens there is a time penalty before the cannon can be fired.

`loading = self.sensors['LOADING']`