from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory
from os.path import join
import sys

def generate_launch_description():
    config_dir_, config_basename_ = join(get_package_share_directory('cartographer_ros'), 'configuration_files'), ""
    occupancy_grid_resolution_ = '0.05'

    for arg in sys.argv:
        if arg.startswith("configuration_directory:="): config_dir_ = arg.split(':=')[1]
        if arg.startswith("configuration_basename:="): config_basename_ = arg.split(':=')[1]
        if arg.startswith("occupancy_grid_resolution:="): occupancy_grid_resolution_ = arg.split(':=')[1]
    
    return LaunchDescription([
        Node(
	        package = 'cartographer_ros',
            executable = 'cartographer_node',
            name = 'cartographer_node',
            output = 'screen',
            arguments=[ '-configuration_directory=' + config_dir_, '-configuration_basename=' + config_basename_ ]
	    ),

        Node(
            package = 'cartographer_ros',
            executable = "occupancy_grid_node",
            name = "cartographer_occupancy_grid_node",
            output = 'screen',
            arguments=[ "-resolution " + occupancy_grid_resolution_ ]
        )
    ])