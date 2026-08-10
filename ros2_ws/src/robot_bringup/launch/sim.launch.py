from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg = FindPackageShare('robot_bringup')
    desc = FindPackageShare('robot_description')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])
        ),
        launch_arguments={'gz_args': PathJoinSubstitution([pkg, 'worlds', 'empty.world.sdf'])}.items(),
    )

    robot_description = Command([
        'xacro ', PathJoinSubstitution([desc, 'urdf', 'robot.urdf.xacro'])
    ])

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description, 'use_sim_time': True}],
        output='screen',
    )

    spawn = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-name', 'ai_robot', '-topic', 'robot_description', '-x', '0', '-y', '0', '-z', '0.1'],
        output='screen',
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{'config_file': PathJoinSubstitution([pkg, 'config', 'bridge.yaml'])}],
        output='screen',
    )

    return LaunchDescription([gazebo, rsp, spawn, bridge])
