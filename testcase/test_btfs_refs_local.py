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
COMMANDS_FILE = "../data/btfs_refs_local_commands.yml"

@pytest.fixture(scope="module")
def btfs_handler():
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

def test_btfs_refs_local(btfs_handler):
    """
    Test the 'test_btfs_refs_local ' command.
    """
    # Read the command and parameters from YAML
    # 操作元数据（metadata）的前提条件需要pin
    command_pin_template = btfs_handler.commands['btfs']['btfs_refs_local']
    # Execute the command
    stdout, stderr = btfs_handler.execute_command(command_pin_template, key=None)
    print("标准输出1:", stdout)
    print("错误输出2:", stderr)
    # 查看输出内容是否包含 key
    if stdout is not None and stdout == "":
        print("btfs refs local 结果为空，实际输出:", stdout)
    # Assert the command output
    assert stdout is not None and stdout != ""
