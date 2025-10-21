import sys
def echo():
    shout = "-s" in sys.argv  # 检测是否传入 -s 参数
    message = input("Enter something: ")
    print(message.upper() if shout else message)  # 大写输出
if __name__ == "__main__":
    echo()