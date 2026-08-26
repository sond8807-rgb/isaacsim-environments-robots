# How To Set Up The OS1 sensor's ROS2 Point Cloud in Isaac Sim (5.1.0) 

Requirements: Isaac Sim, ros2, rviz2 (for visualization).

<img width="3280" height="1472" alt="spot_lidar_os1" src="https://github.com/user-attachments/assets/5b3d9527-60ea-47cd-b4b3-491a4a9b2f3b" />

**1. Place the sensor on the robot**

* **OS1-64: There is currently no OS1-64 sensor in Isaac Sim.** Instructions on how to add one here: https://github.com/sond8807-rgb/isaacsim-environments-robots/tree/main/Sensors/OS1/os1_64_sensor_package

OS1-32 and OS1-128: Isaac Sim already has both the OS1-32 and OS1-128 in the asset browser. To Add the OS1-128 sensor to the scene: Create > Sensors > RTX Lidar > Ouster > OS1. Make sure to move the sensor under the robot's body prim so that the sensor becomes attached to it. For example, on the spot robot, I have the "OS1" prim under the "body" prim.

The different variants of the sensor can also be chosen in the property tab, under Variants.

**2. Set up the Action Graphs (point cloud publisher and TF publisher)** 

**First**, create the RTX Lidar action graph: Tools > Robotics > ROS 2 Omnigraphs > RTX Lidar. Add the "Lidar Prim" by navigating to the lidar sensor's prim (indicated by a sensor icon with a blue arrow on it). For "Frame ID", write the name of the sensor prim. In the OS1's case, it should be "sensor". Uncheck the "Laser Scan" box and check the "Point Cloud" box (Laser Scan only works for 2D Lidars). Click OK.

To have **full scans** instead of partial ones, click on the PointCloudPublish node and check "Publish Full Scan" under "Inputs" in the Property window:
<img width="1139" height="602" alt="Screenshot from 2026-08-26 14-12-47" src="https://github.com/user-attachments/assets/6a0ab014-ed13-4cbe-be35-70af15a9e408" />


When you run the simulation, the point cloud data should now be sent through the ROS2 "/point_cloud" topic.  

**Secondly**, create the TF Publisher action graph: Tools > Robotics > ROS 2 Omnigraphs > TF Publisher. For "Target Prim", add the path to the sensor prim (ex: for spot, it is "/spot/body/OS1/sensor"). For "Parent Prim", add the path to the root prim of your robot (ex: for spot, it is "/spot"). Press OK. 

To see the point cloud, open rviz2. In your terminal:

```
rviz2
```

In rviz2, go under Displays > Global Options > Fixed Frame, and select "sensor" (or your sensor name) from the list.

Then add the point cloud: Add > By topic > /point_cloud > PointCloud2.

Make sure to run the simulation, and your rviz2 visualization should look something like this: <img width="3280" height="1472" alt="spot_lidar_os1" src="https://github.com/user-attachments/assets/5b3d9527-60ea-47cd-b4b3-491a4a9b2f3b" />

