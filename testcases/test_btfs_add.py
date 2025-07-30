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
COMMANDS_FILE = project_root / 'data' / 'btfs_add_commands.yml'


@allure.suite("BTFS Add Tests")
class TestBtfsAdd:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("BTFS Add Tests")
    @allure.title("test_btfs_add")
    def test_btfs_add(btfs_handler):
        """
        Test the 'btfs add' command.
        """
        # Start the BTFS daemon
        # btfs_handler.start_daemon()

        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_add']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "added" in stdout

    @allure.story("BTFS Add r Test")
    @allure.title("test_btfs_add_r")
    def test_btfs_add_r(btfs_handler):
        """
        Test the 'btfs add' command.
        """
        # Start the BTFS daemon
        # btfs_handler.start_daemon()

        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_add_r']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][1]['params']['key']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "added" in stdout