from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get the cartographer_ros package's share directory
    cartographer_config_dir = os.path.join(
        get_package_share_directory('cartographer_demo'), 'config'
    )

    # Define the path to the configuration file
    configuration_basename = 'config.lua'

    return LaunchDescription([
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[
                {'use_sim_time': False}  # Set to True if using simulation time
            ],
            remappings=[
                ('/scan', '/laser')  # Remap your laser scan topic if necessary
            ],
            arguments = [
                '-configuration_directory', FindPackageShare('cartographer_ros').find('cartographer_ros') + '/configuration_files',
                '-configuration_basename', 'backpack_2d.lua'],

        ),
    ])

