"""
Registers this package's lidar_configs/ folder with Isaac Sim's RTX lidar
config search path, so the OS1_REV6_64ch*.json profiles resolve without
copying anything into the Isaac Sim install itself.

Call register_os1_64_configs() once, early in your script/extension --
before any IsaacSensorCreateRtxLidar command that references an
"OS1_REV6_64ch..." config name.
"""

import os

import carb.settings

_PROFILE_KEY = "/app/sensors/nv/lidar/profileBaseFolder"


def register_os1_64_configs() -> None:
    package_dir = os.path.dirname(os.path.abspath(__file__))
    os1_folder = os.path.join(package_dir, "lidar_configs", "Ouster", "OS1") + "/"

    settings = carb.settings.get_settings()
    current_paths = list(settings.get(_PROFILE_KEY) or [])

    if os1_folder not in current_paths:
        settings.set(_PROFILE_KEY, current_paths + [os1_folder])
        carb.log_info(f"Registered custom lidar config folder: {os1_folder}")
