import subprocess
import pytest
import time
import os
import signal

# 设定环境变量和路径
BTFS_PATH = "/home/ec2-user/btfs/.btfs.staging600"
BTFS_CMD_PATH = "/home/ec2-user/go/src/github.com/bittorrent/3.3.0_new/go-btfs/cmd/btfs"


# 启动 btfs daemon 的函数
def start_btfs_daemon():
    # 设置环境变量
    env = os.environ.copy()
    env["BTFS_PATH"] = BTFS_PATH

    # 启动 btfs daemon
    process = subprocess.Popen(
        ["btfs", "daemon"],
        cwd=BTFS_CMD_PATH,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return process


# 检测 btfs 是否正常运行
def check_btfs_running():
    # 通过 ps aux | grep btfs 检测进程
    result = subprocess.run(
        ["ps", "aux"],
        capture_output=True,
        text=True
    )
    return "btfs daemon" in result.stdout


# 终止 btfs 进程
def stop_btfs_daemon():
    subprocess.run(["killall", "btfs"])


# 测试用例
