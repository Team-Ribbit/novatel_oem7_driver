from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    pkg_name = "novatel_oem7_driver"

    launch_file_path = PathJoinSubstitution([FindPackageShare(pkg_name),
                                             "launch",
                                             "oem7_net.launch.py"])

    launch_source = PythonLaunchDescriptionSource([launch_file_path])

    arguments = {
        "oem7_port_name": "/dev/ttyS1",
        "oem7_port_baud": "57600",
        "oem7_if": "Oem7ReceiverUdp",
        "oem7_ip_addr": "10.1.0.212",
        "oem7_port": "3001",
        "oem7_position_source" : "",
    }.items()

    return LaunchDescription([
        IncludeLaunchDescription(launch_source,
                                 launch_arguments=arguments)
    ])