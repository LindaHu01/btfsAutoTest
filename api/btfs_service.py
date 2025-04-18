import os
import paramiko
import yaml


class SSHConnection:
    def __init__(self, host, username, private_key_path):
        self.host = host
        self.username = username
        self.private_key_path = private_key_path
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            private_key = paramiko.RSAKey.from_private_key_file(self.private_key_path)
            self.ssh.connect(self.host, username=self.username, pkey=private_key)
            print("Connected to the server.")
        except Exception as e:
            print(f"Failed to connect: {e}")

    def execute_command(self, command):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                output = stdout.read().decode('utf-8')
                return output
            else:
                error = stderr.read().decode('utf-8')
                print(f"Command execution failed: {error}")
                return None
        except Exception as e:
            print(f"Error executing command: {e}")
            return None

    def close(self):
        self.ssh.close()
        print("Connection closed.")


def read_commands(file_path):
    try:
        with open(file_path, 'r') as file:
            commands = yaml.safe_load(file)
        return commands
    except Exception as e:
        print(f"Error reading commands file: {e}")
        return None


if __name__ == "__main__":
    # Configuration
    HOST = "54.151.1.17"
    USERNAME = "ec2-user"
    PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa")  # Update with your private key path
    COMMANDS_FILE = "../data/btfs_daemon_commands.yml"

    ssh = SSHConnection(HOST, USERNAME, PRIVATE_KEY_PATH)
    ssh.connect()

    commands = read_commands(COMMANDS_FILE)
    if commands:
        start_daemon_command = commands['btfs']['start_daemon']
        if start_daemon_command:
            ssh.execute_command(start_daemon_command)

    ssh.close()
