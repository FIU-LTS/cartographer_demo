import os #for Python to interact w/ OS
import launch_ros.actions

from ament_index_python.packages import get_package_share_directory #finds path to pkg share files
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    cartographer_pkg = get_package_share_directory('cartographer_demo')


    rplidar_launch = os.path.join(cartographer_pkg, 'launch', 'rplidar_a2m8_launch.py')
    rf2o_launch = os.path.join(cartographer_pkg, 'launch', 'rf2o_laser_odometry.launch.py')
    cartographer_launch = os.path.join(cartographer_pkg, 'launch', 'cartographer.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
                PythonLaunchDescriptionSource(rplidar_launch)
        ),
        IncludeLaunchDescription(
                PythonLaunchDescriptionSource(rf2o_launch)
        ),
        IncludeLaunchDescription(
                PythonLaunchDescriptionSource(cartographer_launch)
        )



    ])