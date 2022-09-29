product_list = [
    ("HUAWEI_Mate_2", 4999),
    ("HUAWEI_nava_3", 2799),
    ("HUAWEI_nava_3i", 1899),
    ("HUAWEI_麦芒7", 2199),
    ("华为畅享_MAX", 1699),
]

saving = input("请输入账号金额：")
shopping_car = []
if saving.isdigit():
    saving = int(saving)
    print("********请选择商品序号*********")
    while True:
        for i, v in enumerate(product_list, 1):
            print(i, '>>>>', v[0], v[1])
        print("*" * 20)
        choice = input("选择购买商品编号[退出请输入q]:")
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(product_list):
                choice_item = product_list[choice - 1]
                if choice_item[1] < saving:
                    saving -= choice_item[1]
                    shopping_car.append(choice_item)
                else:
                    print('账户余额不足,还剩%d元' % saving)
                print(choice_item)
            else:
                print('编码对应的商品不存在')
        elif choice == 'q':
            print('---------您已经选择如下商品--------')
            for i, v in enumerate(shopping_car, 1):
                print(i, '>>>>', v[0], v[1])
                print('您还剩%d元' % saving)
            break
        else:
            print('无效输入，请重新输入！！')
