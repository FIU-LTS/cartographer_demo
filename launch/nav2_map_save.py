#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from datetime import datetime as dt

def generate_launch_description():

    timestamp = dt.now().strftime('%Y%m%d_%H%M%S')
    facility = 'fiu-arc'
    filename = f"/home/administrator/map/{timestamp}_{facility}"
    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_saver_cli',
            name='map_saver_cli',
            arguments=['-f', filename],
            parameters=[{'save_map_timeout':10000.0,
                         'free_thresh_default': 0.5,
                         'occupied_thresh_default': 0.5}]
            )
        ])
