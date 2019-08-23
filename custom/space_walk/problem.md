# Space walk

On December 27 2013, astronauts Alexander Misurkin and Flight Engineer Anton Shkaplerov of the Russian space agency Roscosmos set a new world record for the longest single space walk at 8 hours and 13 minutes outside there spacecraft. During a spacewalk astronauts are equiped with jetpacks to propel themselves through the vacuum of space incase they get separated from the ship. They can also be a lot of fun to play with as well...Oh dear.

A bored astronaut has had a little bit too much fun and has drifted away from the station. He's become disoriented and lost sight of the space station. Fortunately for him, metrics from his onboard accelerometer are constantly beamed back to the space station. With some processing we should be able to reconstruct his movements.

# Input

Each line in the file are acceleration readings, taken from the astronauts on board accelerometer at a rate of 10 times per second, representing accelerations in the X, Y and Z axis relative to the space station

Data from sensors are normalized to an idealized cartesian coordinate system relative to the stations frame of reference. In this frame of reference the station is located at origin (0, 0, 0).

Conveniently the astronauts orientation is also normalized such that a positive reading in the Z column would represent the astronaut accelerating "upwards", in a positive Z direction relative to the space station regardless of the astronauts orientation.

You may use the following formula's for calculating the astronauts distance and velocity from one point in time to the next.

`d = (vi + vf) / * 0.5 * t`

`vf = vi + a * t`

Here's an example of how the astronaut's velocity and displacement change from one point in time to the next, in one dimension in space.

|Time (s)|Acceleration (m/s/s)|Velocity (m/s)|Distance (m)|
|---|---|---|---|
|0.0|1.000|0.000|0.000|
|1.0|1.000|1.000|0.500|
|2.0|1.000|2.000|2.000|
|3.0|1.000|3.000|4.500|

## Output

The output should be a single line representing the astronauts distance from his starting point along the X, Y and Z coordinates

## Example

```
    0.0 -0.254  -1.06
    0.0   2.23  -2.08
    0.0    0.0  0.613
 -0.682 -0.812    0.0
    0.0  -2.34  0.659
 -0.644  -2.18    0.0
  0.977   1.63 -0.214
   2.36    0.0  -2.42
  0.169  0.869   -1.8
```

**Output**
```
0.0 -0.1 -0.5
```
