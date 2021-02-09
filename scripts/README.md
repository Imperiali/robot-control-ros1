## Resume

This is the repository of the code in the lesson 09/02/2021

## Must have

```
roscore
```

## Install

Create package

```
$ catkin_create_pgk <pkg_name> rospy

$ chmod +x turtle_control.py goal.py
```

## Run

Terminal 1

```
$ roscore
```

Terminal 2

```
$ rosrun turtlesim turtlesim_node
```

Terminal 3

```
$ rosrun <pkg_name> goal.py <position x> <position y> <position theta>
```

Terminal 2

```
$ rosrun <pkg_name> turtle_control.py
```

## Issues?

Open one [issue](https://github.com/Imperiali/robot-control-ros1/issues)

## Have an idea?

Open one [Pull Request](https://github.com/Imperiali/robot-control-ros1/pulls)
