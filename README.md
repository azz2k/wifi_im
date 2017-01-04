# Description of wifi_im

ROS package for some wifi mapping and navigation experiments

This package was used as the robot controller for the paper 
[Active exploration of sensor networks from a robotics perspective](https://arxiv.org/abs/1511.05488).

## Requirements

* It is assumed that you are using a turtlebot
* ROS package [wifi_sensor](https://github.com/azz2k/wifi_sensor)
* The area for the experiment has been mapped using
  [gmapping](http://wiki.ros.org/gmapping) and the map is being published


## Parameters

* `string` target_mac
