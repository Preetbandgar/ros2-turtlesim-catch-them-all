from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    number_publisher= Node(
        package="my_py_pkg_1",
        executable="number_publisher",
    )

    number_counter = Node(
        package="my_py_pkg_1",
        executable="number_counter",
    )

    ld.add_action(number_publisher)
    ld.add_action(number_counter)

    return ld