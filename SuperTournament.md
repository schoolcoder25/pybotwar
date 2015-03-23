# Introduction #

A Super Tournament runs tournaments with all possible combinations of robots.


# Details #

A Super Tournament takes a given set of robots and runs tournaments with all possible combinations of those robots. In other words, it takes them 2-at-a-time, 3-at-a-time, etc.

So, for example if you ran a Super Tournament with robots robot1, robot2, robot3, and robot4, tournaments would be run with:

  * robot1, robot2
  * robot1, robot3
  * robot1, robot4
  * robot2, robot3
  * robot2, robot4
  * robot3, robot4
  * robot1, robot2, robot3
  * robot1, robot2, robot4
  * robot1, robot3, robot4
  * robot2, robot3, robot4
  * robot1, robot2, robot3, robot4



# Results #

Using example robots from version 0.8 gives the following results:

```
robot07 : 251 wins : 1028 outlasted : 68025 dmg caused : 520 kills
robot05 : 195 wins : 1156 outlasted : 57200 dmg caused : 474 kills
robot06 : 180 wins :  955 outlasted : 61438 dmg caused : 421 kills
robot09 : 170 wins :  870 outlasted : 68061 dmg caused : 449 kills
robot04 : 162 wins :  753 outlasted : 37430 dmg caused : 425 kills
robot03 : 137 wins :  847 outlasted : 54120 dmg caused : 366 kills
robot02 : 102 wins : 1108 outlasted : 45620 dmg caused : 535 kills
```



Running --supertournament with the default configuration will run a long series of 5-battle tournaments with all combinations of the 7 default robots. It may take several hours to complete.

```
Tournament Results
5 battles between 7 robots

robot07 : 142 wins : 550 outlasted : 37502 dmg caused : 306 kills
robot06 : 113 wins : 550 outlasted : 34375 dmg caused : 277 kills
robot09 : 99 wins : 464 outlasted : 41034 dmg caused : 293 kills
robot05 : 91 wins : 569 outlasted : 23660 dmg caused : 205 kills
robot04 : 73 wins : 350 outlasted : 20560 dmg caused : 183 kills
robot03 : 51 wins : 380 outlasted : 23700 dmg caused : 140 kills
robot02 : 31 wins : 497 outlasted : 17650 dmg caused : 185 kills
```