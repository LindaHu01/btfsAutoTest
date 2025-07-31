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
COMMANDS_FILE = project_root / 'data' / 'btfs_id_commands.yml'

@allure.suite("BTFS ID Tests")
class TestBtfsId:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    @allure.story("BTFS id Test")
    @allure.title("test_btfs_id")
    def test_btfs_id(self, btfs_handler):
        """
        Test the 'test_btfs_id ' command.
        """
        # Read the command and parameters from YAML
        with allure.step("Prepare command parameters"):
            command_template = btfs_handler.commands['btfs']['btfs_id']
            key1 = btfs_handler.commands['version_path']['value']
            key2 = btfs_handler.commands['BTFS_PATH']['value']
        # Execute the command
        with allure.step("Execute command"):
            stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2)
            print("标准输出1:", stdout)
            print("错误输出2:", stderr)
            # 查看输出内容是否包含 key
            if "ID" not in stdout:
                print("输出不包含 'ID'，实际输出:", stdout)
        # Assert the command output
        with allure.step("Validate output"):
            assert "ID" in stdout
