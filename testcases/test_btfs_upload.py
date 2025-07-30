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
COMMANDS_FILE = project_root / 'data' / 'btfs_upload.yml'

@allure.suite("BTFS Upload Tests")
class TestBtfsUpload:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("Standard BTFS Upload")
    @allure.title("Test standard BTFS upload")
    def test_btfs_upload(btfs_handler):
        """
        Test the 'test_btfs_upload' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_upload']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key3']

        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "ID" not in stdout:
                print("输出不包含 'ID'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "ID" in stdout

    @allure.story("SP Upload with Copy")
    @allure.title("Test BTFS SP upload with copy")
    def test_btfs_upload_sp(btfs_handler):
        """
        Test the 'test_btfs_upload_sp' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_upload_sp']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
            key4 = btfs_handler.commands['test_cases'][0]['params']['key4']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3, key4=key4)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "ID" not in stdout:
                print("输出不包含 'ID'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "ID" in stdout

    @allure.story("SP Upload with Copy1")
    @allure.title("Test BTFS SP upload with copy1")
    def test_btfs_upload_sp_copy1(btfs_handler):
        """
        Test the 'test_btfs_upload_sp_copy1' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_upload_sp_copy1']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", command_template)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "ID" not in stdout:
                print("输出不包含 'ID'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "ID" in stdout

    @allure.story("SP Upload with Copy3")
    @allure.title("Test BTFS SP upload with copy3")
    def test_btfs_upload_sp_copy3(btfs_handler):
        """
        Test the 'test_btfs_upload_sp_copy3' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_upload_sp_copy3']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", command_template)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "ID" not in stdout:
                print("输出不包含 'ID'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "ID" in stdout

    @allure.story("SP Upload with Copy5")
    @allure.title("Test BTFS SP upload with copy5")
    def test_btfs_upload_sp_copy5(btfs_handler):
        """
        Test the 'test_btfs_upload_sp_copy5' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_upload_sp_copy5']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key3']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出1:", command_template)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "ID" not in stdout:
                print("输出不包含 'ID'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "ID" in stdout

    @allure.story("btfs_upload_token_usdd")
    @allure.title("Test BTFS SP upload token usdd")
    def test_btfs_upload_token_usdd(btfs_handler):
        """
        Test the 'test_btfs_upload_token_usdd' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_upload_token_usdd']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key5 = btfs_handler.commands['test_cases'][0]['params']['key5']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key5=key5)
            print("标准输出1:", command_template)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "ID" not in stdout:
                print("输出不包含 'ID'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "ID" in stdout

    @allure.story("btfs_upload_token_usdt")
    @allure.title("Test BTFS SP upload token usdt")
    def test_btfs_upload_token_usdt(btfs_handler):
        """
        Test the 'test_btfs_upload_token_usdt' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_upload_token_usdt']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key6 = btfs_handler.commands['test_cases'][0]['params']['key6']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key6=key6)
            print("标准输出1:", command_template)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            if "ID" not in stdout:
                print("输出不包含 'ID'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "ID" in stdout


