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
COMMANDS_FILE = "../data/btfs_stats_bitswap.yml"

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_stats_bitswap(btfs_handler):
    """
    Test the 'test_btfs_stats_bitswap' command.
    """
    # Read the command and parameters from YAML
    # 操作元数据（metadata）的前提条件需要pin
    command_rm_template = btfs_handler.commands['btfs']['btfs_stats_bitswap']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "status" not in stdout:
        print("输出不包含 'status'，实际输出:", stdout)
    # Assert the command output
    assert "status" in stdout

def test_btfs_stats_bw(btfs_handler):
    """
    Test the 'test_btfs_stats_bw' command.
    """
    # Read the command and parameters from YAML
    # 操作元数据（metadata）的前提条件需要pin
    command_rm_template = btfs_handler.commands['btfs']['btfs_stats_bw']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "Bandwidth" not in stdout:
        print("输出不包含 'Bandwidth'，实际输出:", stdout)
    # Assert the command output
    assert "Bandwidth" in stdout
def test_btfs_stats_repo(btfs_handler):
    """
    Test the 'test_btfs_stats_repo' command.
    """
    # Read the command and parameters from YAML
    # 操作元数据（metadata）的前提条件需要pin
    command_rm_template = btfs_handler.commands['btfs']['btfs_stats_repo']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_rm_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    if "NumObjects" not in stdout:
        print("输出不包含 'NumObjects'，实际输出:", stdout)
    # Assert the command output
    assert "NumObjects" in stdout

