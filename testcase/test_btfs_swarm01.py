import json
import random
import re
import shlex

import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = "../data/btfs_swarm.yml"
#
@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_swarm_addrs(btfs_handler):
    """
    Test the 'test_btfs_swarm_addrs' command.
    """
    # Read the command and parameters from YAML
    command_rm_template = btfs_handler.commands['btfs']['btfs_swarm_addrs']
    key = btfs_handler.commands['version_path']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "4001" not in stdout:
        print("输出不包含 '4001'，实际输出:", stdout)
    # Assert the command output
    assert "4001" in stdout


def test_btfs_swarm_addrs_listen(btfs_handler):
    """
    Test the 'test_btfs_swarm_addrs_listen' command.
    """
    # Read the command and parameters from YAML
    command_rm_template = btfs_handler.commands['btfs']['btfs_swarm_addrs_listen']
    key = btfs_handler.commands['version_path']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "4001" not in stdout:
        print("输出不包含 '4001'，实际输出:", stdout)
    # Assert the command output
    assert "4001" in stdout


def test_btfs_swarm_addrs_local (btfs_handler):
    """
    Test the 'test_btfs_swarm_addrs_local' command.
    """
    # Read the command and parameters from YAML
    command_rm_template = btfs_handler.commands['btfs']['btfs_swarm_addrs_local']
    key = btfs_handler.commands['version_path']['value']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key=key)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "4001" not in stdout:
        print("输出不包含 '4001'，实际输出:", stdout)
    # Assert the command output
    assert "4001" in stdout



