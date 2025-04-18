import pytest
import paramiko
import os

from api.btfs_service import read_commands

# Configuration
HOST = "54.151.1.17"
USERNAME = "ec2-user"
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
COMMANDS_FILE = ("../data/btfs_daemon_commands.yml")


@pytest.fixture
def ssh_connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_PATH, password="1234")
    ssh.connect(HOST, username=USERNAME, pkey=private_key)
    yield ssh
    ssh.close()


def test_btfs_service_started(ssh_connection):
    commands = read_commands(COMMANDS_FILE)
    if commands:
        start_daemon_command = commands['btfs']['start_daemon']
        if start_daemon_command:
            stdin, stdout, stderr = ssh_connection.exec_command(start_daemon_command)
            output = stdout.read().decode('utf-8')
            print(output)
            assert 'peer' in output


# def test_btfs_service_started(ssh_connection):
#     command = "ps -ef | grep btfs | grep -v grep"
#     stdin, stdout, stderr = ssh_connection.exec_command(command)
#     output = stdout.read().decode('utf-8')
#     assert output, "BTFS service is not running."
