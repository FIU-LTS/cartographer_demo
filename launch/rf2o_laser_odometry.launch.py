import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

             Node(
            package='rtabmap_odom', executable='icp_odometry', output='screen',
            parameters=[{
              'frame_id':'base_link',
              'odom_frame_id':'odom',
              'publish_tf': False, 
              'wait_for_transform':0.4,
              'expected_update_rate':25.0,
              'use_sim_time': False,
            }],
            remappings=[
              ('scan_cloud', '/points'),
              ('imu', '/imu'),
              ('odom', '/icp/odometry'),
            ],
            arguments=[
              'Icp/PointToPlane', 'true',
              'Icp/Iterations', '10',
              'Icp/VoxelSize', '0.1',
              'Icp/Epsilon', '0.001',
              'Icp/PointToPlaneK', '20',
              'Icp/PointToPlaneRadius', '0',
              'Icp/MaxTranslation', '2',
              'Icp/MaxCorrespondenceDistance', '1',
              'Icp/Strategy', '1',
              'Icp/OutlierRatio', '0.7',
              'Icp/CorrespondenceRatio', '0.01',
              'Odom/ScanKeyFrameThr', '0.4',
              'Odom/ResetCountdown', '1',
              'OdomF2M/ScanSubtractRadius', '0.1',
              'OdomF2M/ScanMaxSize', '60000',
              'OdomF2M/BundleAdjustment', 'false',
            ])
    ])
