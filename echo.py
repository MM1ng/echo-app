import sys
def echo():
    shout = "-s" in sys.argv  # 检测是否传入 -s 参数
    message = input("Please enter a message: ")  # 统一的输入提示
    print(message.upper() if shout else message)  # 大写输出
if __name__ == "__main__":
    echo()