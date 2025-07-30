import json
import random
import re
import shlex
from pathlib import Path

import allure
import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
project_root = Path(__file__).parent.parent
COMMANDS_FILE = project_root / 'data' / 'btfs_refs_local_commands.yml'


@allure.suite("BTFS Refs Tests")
class TestBtfsRefs:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("BTFS Refs Tests")
    @allure.title("test_btfs_refs_local")
    def test_btfs_refs_local(btfs_handler):
        """
        Test the 'test_btfs_refs_local ' command.
        """
        # Read the command and parameters from YAML
        # 操作元数据（metadata）的前提条件需要pin
        with allure.step("Prepare command parameters"):
            command_pin_template = btfs_handler.commands['btfs']['btfs_refs_local']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_pin_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            # 查看输出内容是否包含 key
            if stdout is not None and stdout == "":
                print("btfs refs local 结果为空，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert stdout is not None and stdout != ""
