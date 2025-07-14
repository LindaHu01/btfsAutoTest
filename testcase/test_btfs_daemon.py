# import os
#
# import pytest
#
# from api.BtfsHandler import BtfsHandler
# # Configuration
# HOST = "54.151.1.17"
# USERNAME = "ec2-user"
# PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
# COMMANDS_FILE = ("../data/btfs_daemon_commands.yml")
#
# @pytest.fixture(scope="module")
# def btfs_handler():
#     """Fixture to manage BtfsHandler setup and teardown."""
#     handler = BtfsHandler(HOST, USERNAME, PRIVATE_KEY_PATH, COMMANDS_FILE)
#     handler.connect()
#     yield handler
#     # handler.disconnect()
#
# def test_btfs_daemon(btfs_handler):
#     """
#     Test the 'test_btfs_daemon' command.
#     """
#     try:
#         stdout, stderr = btfs_handler.start_daemon()
#
#         # Assert the command output
#         assert "go-btfs version" in stdout, f"Failed to start BTFS daemon. Output: {stdout} Error: {stderr}"
#
#     except Exception as e:
#         pytest.fail(f"Test failed due to exception: {e}")
