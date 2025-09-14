num = input("请输入一个 5 位数：")
if len(num) != 5 or not num.isdigit():
    print("输入不是有效的 5 位数！")
else:
    if num == num[::-1]:
        print(f"{num} 是回文数")
    else:
        print(f"{num} 不是回文数")
