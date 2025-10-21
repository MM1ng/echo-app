import sys
def echo():
    shout = "-s" in sys.argv
    message = input("Please enter a message: ")
    print(message.upper() if shout else message)
    print(f"Message length: {len(message)}")  # 新增：显示输入长度
if __name__ == "__main__":
    echo()