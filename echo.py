def echo():
    message = input("Type anything: ")  # conflict-branch 分支的修改
    print(message)
if __name__ == "__main__":
    echo()