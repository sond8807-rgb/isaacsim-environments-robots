# OS1-64 RTX Lidar Package
This package adds a OS1_64 lidar sensor to Isaac Sim. Beam angles are resampled from Ouster's real REV6 32-channel calibration, not an actual OS1-64 factory dump.

Install this package, then do the following.

**1. Append the package. Modify the second line according to your installation path and run the following python script:**

```python
import sys
sys.path.append("/path/to/os1_64_sensor_package") 
from register_lidar_configs import register_os1_64_configs
register_os1_64_configs()   # run before creating the sensor or referencing a .usd that uses it
```

**2. Either,**

* Add the lidar sensor and action graphs manually. 

In Isaac Sim's script editor (Window > Script Editor), run the following.
```python
import omni.kit.commands
from pxr import Gf

_, sensor = omni.kit.commands.execute(
    "IsaacSensorCreateRtxLidar",
    path="/World/os1_64",
    config="OS1_REV6_64ch10hz512res",  # or 10hz1024res / 10hz2048res / 20hz512res / 20hz1024res
    translation=(0, 0, 1.0),
    orientation=Gf.Quatd(1.0, 0.0, 0.0, 0.0),
    force_camera_prim=True,
)
```
Then, add the required Action Graphs (See step 2: https://github.com/sond8807-rgb/isaacsim-environments-robots/blob/main/Sensors/OS1/setup.md)

**Or alternatively,**
* Import the OS1_64.usd file which contains the sensor, and required action graphs.

Add it as a reference into Isaac Sim (Drag and drop it onto the scene from the Content window).
To change the config, go under the Property tab and change "Sensor config" to your liking: OS1_REV6_64ch10hz512res, or 10hz1024res / 10hz2048res / 20hz512res / 20hz1024res

The ros domain ID is modifiable in the "Context" nodes.
