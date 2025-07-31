import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from utils.report_util import get_test_results
from utils.telegram_bot import TelegramBot

# 配置Telegram机器人
TELEGRAM_TOKEN = "7108929540:AAGhGbpcVjEFss34OLoZErz8_WtHxbReeGc"
TELEGRAM_CHAT_ID = "-1002612587832"
REPORT_URL = ""

# 获取项目根目录
PROJECT_ROOT = Path(__file__).parent.absolute()


def main():
    global report_dir
    start_time = datetime.now()
    test_failed = False

    try:
        print("Starting test execution...")
        # 在项目根目录下运行pytest
        result = subprocess.run(
            [
                "pytest",
                "-v",
                "--alluredir=allure-results",
                "testcases"
            ],
            cwd=PROJECT_ROOT,
            capture_output=True,  # 捕获输出
            text=True  # 以文本形式返回
        )

        # 打印测试输出
        print("Test Output:")
        print(result.stdout)
        print("Test Errors:")
        print(result.stderr)

        # 检查返回码
        if result.returncode != 0:
            print(f"测试执行失败，返回码: {result.returncode}")
            test_failed = True

    except Exception as e:
        print(f"测试执行发生异常: {str(e)}")
        test_failed = True
        # 2. 生成Allure报告
        print("Generating Allure report...")
        report_dir = f"allure-report-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        subprocess.run([
            "allure",
            "generate",
            "allure-results",
            "-o",
            report_dir,
            "--clean"
        ], check=True)

        # 获取测试结果
        test_results = get_test_results()
        print(f"Test results: {test_results}")

        # 生成报告摘要
        duration = datetime.now() - start_time
        summary = generate_text_report(test_results, duration, REPORT_URL, test_failed)

        # 发送报告到Telegram
        bot = TelegramBot(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID)
        response = bot.send_message(summary)
        # 发送完整报告(ZIP压缩包)
        zip_report = f"{report_dir}.zip"
        subprocess.run(["zip", "-r", zip_report, report_dir], check=True)
        bot.send_message(zip_report)

        if response:
            print(f"报告已发送到Telegram。总测试数: {test_results['total']}")
        else:
            print("发送报告到Telegram失败")


    def generate_text_report(results, duration, report_url, test_failed):
        """生成简洁的文本报告"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        duration_str = str(duration).split('.')[0]

        status_emoji = "❌" if test_failed else "✅"
        status_text = "失败" if test_failed else "成功"

        # 添加失败详情
        failure_details = ""
        if results['failed'] > 0:
            failure_details = f"\n🔴 失败测试: {results['failed']}"

        return f"""
Hi, BTFS v4.0自动化测试报告~~
⏰时间: {timestamp}
📊测试结果: ✅成功: {results['passed']} ❌失败: {results['failed']} ⚠️跳过: {results['skipped']}
📋总数: {results['passed'] + results['failed'] + results['skipped']}
"""


if __name__ == "__main__":
    main()
