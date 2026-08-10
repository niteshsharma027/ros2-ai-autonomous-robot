from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    model = PathJoinSubstitution([
        FindPackageShare('robot_description'), 'urdf', 'robot.urdf.xacro'
    ])

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': Command(['xacro ', model]),
                'use_sim_time': LaunchConfiguration('use_sim_time'),
            }],
            output='screen',
        ),
    ])
