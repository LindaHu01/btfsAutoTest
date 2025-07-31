from pathlib import Path

import pytest
import os

from api.BtfsHandler import BtfsHandler

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
# 获取项目根目录
project_root = Path(__file__).parent.parent
COMMANDS_FILE = project_root / 'data' / 'btfs_backup_commands.yml'
global access_key

@pytest.fixture(scope="class")
def btfs_handler(self):
    """Fixture to manage BtfsHandler setup and teardown."""
    handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
    handler.connect()
    yield handler
    # handler.disconnect()

# def test_btfs_backup(self, btfs_handler):
#     """
#     Test the 'test_btfs_backup ' command.
#     """
#     # Read the command and parameters from YAML
#     command_template = btfs_handler.commands['btfs']['btfs_backup']
#     key = btfs_handler.commands['test_cases'][0]['params']['key']
#     # Execute the command
#     stdout, stderr = btfs_handler.execute_command(command_template, key=key)
#     print("标准输出1:", stdout)
#     print("错误输出2:", stderr)
#     # 查看输出内容是否包含 key
#     if "Backup successful" not in stdout:
#         print("输出不包含 'Backup successful'，实际输出:", stdout)
#     # Assert the command output
#     assert "Backup successful" in stdout




