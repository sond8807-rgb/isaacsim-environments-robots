# OS1-64 RTX Lidar Package

```python
import sys
sys.path.append("/path/to/os1_64_sensor_package")
from register_lidar_configs import register_os1_64_configs
register_os1_64_configs()   # run before creating the sensor or referencing a .usd that uses it

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

Beam angles are resampled from Ouster's real REV6 32-channel calibration, not an actual OS1-64 factory dump.
