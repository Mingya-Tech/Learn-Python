def currency_converter():
    rmb = int(input("请输入人民币数额："))
    dollar = str(6.8217*rmb)
    print("对应的美元数额为：" + dollar )

while True:
    currency_converter()
