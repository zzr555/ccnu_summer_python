# Python类与继承作业：计算机父类 + 笔记本子类
class Computer:
    # 类属性：所有设备共享
    category = "电子计算设备"

    # 初始化方法：设置实例属性
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # 方法：自我介绍
    def introduce(self):
        print(f"这是{self.brand} {self.model}，售价{self.price}元。")

    # 方法：涨价（修改属性）
    def increase_price(self, money):
        if money < 0:
            print("涨价金额不能为负数")
            return
        self.price += money
        print(f"{self.brand}{self.model} 涨价{money}元，现价{self.price}元")

    # 方法：降价
    def decrease_price(self, money):
        if money < 0:
            print("降价金额不能为负数")
            return
        if self.price - money < 0:
            print("降价后价格不能低于0元")
            return
        self.price -= money
        print(f"{self.brand}{self.model} 降价{money}元，现价{self.price}元")


# 子类：笔记本电脑，继承Computer父类
class Laptop(Computer):
    # 子类初始化：继承父类属性 + 新增属性
    def __init__(self, brand, model, price, weight, battery):
        super().__init__(brand, model, price)
        self.weight = weight
        self.battery = battery

    # 方法重写（多态）
    def introduce(self):
        super().introduce()
        print(f"它是笔记本，重{self.weight}kg，续航{self.battery}小时。")

    # 子类独有方法
    def show_portable(self):
        if self.weight < 1.5:
            print("机身很轻，随身携带无压力")
        else:
            print("机身偏重，更适合固定场所使用")


# 测试运行代码
if __name__ == "__main__":
    print("===== 父类测试：台式机 =====")
    desktop = Computer("联想", "拯救者台式机", 6999)
    print(f"设备类别：{Computer.category}")
    desktop.introduce()
    desktop.increase_price(300)
    print()

    print("===== 子类测试：笔记本 =====")
    macbook = Laptop("苹果", "MacBook Air", 8999, 1.24, 18)
    macbook.introduce()
    macbook.show_portable()
    macbook.decrease_price(500)
    print()

    print("===== 多态演示 =====")
    device_list = [desktop, macbook]
    for dev in device_list:
        dev.introduce()
        print("---")
