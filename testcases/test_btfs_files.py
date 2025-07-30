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
COMMANDS_FILE = project_root / 'data' / 'btfs_files_commands.yml'


@allure.suite("BTFS Files Tests")
class TestBtfsFiles:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("BTFS Files chcid Test")
    @allure.title("test_btfs_files_chcid")
    def test_btfs_files_chcid(btfs_handler):
        """
        Test the 'test_btfs_files_chcid ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_files_chcid']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
            key3 = btfs_handler.commands['test_cases'][0]['params']['key']
            print("标准输出:", key3)
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
            print("标准输出:", command_template)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            # 查看输出内容是否包含 key
            if "bafyb4ictm4q" not in stdout:
                print("输出不包含 'bafyb4ictm4q'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "bafyb4ictm4q" in stdout


