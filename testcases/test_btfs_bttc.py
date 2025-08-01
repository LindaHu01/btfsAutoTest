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
COMMANDS_FILE = project_root / 'data' / 'btfs_bttc_commands.yml'
global access_key


@allure.suite("BTFS Bttc Tests")
class TestBtfsBttc:
    @pytest.fixture(scope="class")
    def btfs_handler(self):
        """Fixture to manage BtfsHandler setup and teardown."""
        handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
        handler.connect()
        yield handler
        # handler.disconnect()

    # def test_btfs_bttc_btt2wbtt(self, btfs_handler):
    #     """
    #     Test the 'test_btfs_bttc_btt2wbtt ' command.
    #     """
    #     # Read the command and parameters from YAML
    #     command_template = btfs_handler.commands['btfs']['btfs_bttc_btt2wbtt']
    #     key1 = btfs_handler.commands['version_path']['value']
    #     key2 = btfs_handler.commands['BTFS_PATH']['value']
    #     key3 = btfs_handler.commands['test_cases'][0]['params']['key']
    #     # Execute the command
    #     stdout, stderr = btfs_handler.execute_command(command_template, key1=key1, key2=key2, key3=key3)
    #     print("标准输出1:", stdout)
    #     print("错误输出2:", stderr)
    #     # 查看输出内容是否包含 key
    #     if "transaction" not in stdout:
    #         print("输出不包含 'transaction'，实际输出:", stdout)
    #     # Assert the command output
    #     assert "transaction" in stdout


    # def test_btfs_bttc_send_btt_to(self, btfs_handler):
    #     """
    #     Test the 'test_btfs_bttc_send_btt_to ' command.
    #     """
    #     # Read the command and parameters from YAML
    #     command_template = btfs_handler.commands['btfs']['btfs_bttc_send_btt_to']
    #     key0 = btfs_handler.commands['test_cases'][1]['params']['key0']
    #     key1 = btfs_handler.commands['test_cases'][1]['params']['key1']
    #     # Execute the command
    #     stdout, stderr = btfs_handler.execute_command(command_template, key0=key0, key1=key1)
    #     print("标准输出1:", stdout)
    #     print("错误输出2:", stderr)
    #     # 查看输出内容是否包含 key
    #     if "validate" not in stdout:
    #         print("输出不包含 'validate'，实际输出:", stdout)
    #     # Assert the command output
    #     assert "validate" in stdout




