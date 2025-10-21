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
COMMANDS_FILE = project_root / 'data' / 'btfs_swarm.yml'

@allure.suite("BTFS Swarm Tests")
class TestBtfsSwarm:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("Standard BTFS swarm")
    @allure.title("Test standard BTFS swarm addrs")
    def test_btfs_swarm_addrs(self, btfs_handler):
        """
        Test the 'test_btfs_swarm_addrs' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_swarm_addrs']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']

        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "4001" not in stdout:
                print("输出不包含 '4001'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "4001" in stdout

    @allure.story("BTFS swarm test")
    @allure.title("Test BTFS swarm")
    def test_btfs_swarm_addrs_listen(self, btfs_handler):
        """
        Test the 'test_btfs_swarm_addrs_listen' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_swarm_addrs_listen']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "4001" not in stdout:
                print("输出不包含 '4001'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "4001" in stdout

    @allure.story("BTFS swarm addrs local test")
    @allure.title("test_btfs_swarm_addrs_local")
    def test_btfs_swarm_addrs_local(self, btfs_handler):
        """
        Test the 'test_btfs_swarm_addrs_local' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_swarm_addrs_local']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "4001" not in stdout:
                print("输出不包含 '4001'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "4001" in stdout

    @allure.story("BTFS swarm connect test")
    @allure.title("test_btfs_swarm_connect")
    @pytest.mark.skip(reason="SP 替代，暂时不执行")
    def test_btfs_swarm_connect(self, btfs_handler):
        """
        Test the 'test_btfs_swarm_connect' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_swarm_connect']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "success" not in stdout:
                print("输出不包含 'success'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "success" in stdout



