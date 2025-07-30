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
COMMANDS_FILE = project_root / 'data' / 'btfs_stats_bitswap.yml'

@allure.suite("BTFS Stats Tests")
class TestBtfStats:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("BTFS Stats bitswap tests")
    @allure.title("test_btfs_stats_bitswap")
    def test_btfs_stats_bitswap(btfs_handler):
        """
        Test the 'test_btfs_stats_bitswap' command.
        """
        # Read the command and parameters from YAML
        # 操作元数据（metadata）的前提条件需要pin
        with allure.step("Prepare command parameters"):
            command_rm_template = btfs_handler.commands['btfs']['btfs_stats_bitswap']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_rm_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "status" not in stdout:
                print("输出不包含 'status'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "status" in stdout

    @allure.story("BTFS stats bw")
    @allure.title("test_btfs_stats_bw")
    def test_btfs_stats_bw(btfs_handler):
        """
        Test the 'test_btfs_stats_bw' command.
        """
        # Read the command and parameters from YAML
        # 操作元数据（metadata）的前提条件需要pin
        with allure.step("Prepare command parameters"):
            command_rm_template = btfs_handler.commands['btfs']['btfs_stats_bw']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_rm_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "Bandwidth" not in stdout:
                print("输出不包含 'Bandwidth'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "Bandwidth" in stdout

    @allure.story("BTFS stats repo")
    @allure.title("test_btfs_stats_repo")
    def test_btfs_stats_repo(btfs_handler):
        """
        Test the 'test_btfs_stats_repo' command.
        """
        # Read the command and parameters from YAML
        # 操作元数据（metadata）的前提条件需要pin
        with allure.step("Prepare command parameters"):
            command_rm_template = btfs_handler.commands['btfs']['btfs_stats_repo']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_rm_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "NumObjects" not in stdout:
                print("输出不包含 'NumObjects'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "NumObjects" in stdout

