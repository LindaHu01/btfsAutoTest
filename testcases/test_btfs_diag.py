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
COMMANDS_FILE = project_root / 'data' / 'btfs_diag_commands.yml'


@allure.suite("BTFS Diag Test")
class TestBtfsDiag:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("BTFS Diag cmd")
    @allure.title("test_btfs_diag_cmds")
    def test_btfs_diag_cmds(btfs_handler):
        """
        Test the 'test_btfs_diag_cmds ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_diag_cmds']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            # 查看输出内容是否包含 key
            if "diag/cmds" not in stdout:
                print("输出不包含 'diag/cmds'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "diag/cmds" in stdout

    @allure.story("BTFS Diag sys")
    @allure.title("test_btfs_diag_sys")
    def test_btfs_diag_sys(btfs_handler):
        """
        Test the 'test_btfs_diag_sys ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_diag_sys']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            # 查看输出内容是否包含 keys
            if "btfs_version" not in stdout:
                print("输出不包含 'btfs_version'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "btfs_version" in stdout


