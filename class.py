class VendingMachine:
    count = 0

    def __init__(self, model, location):
        VendingMachine.count = VendingMachine.count + 1
        self.model = model
        self.location = location
        self.balance = 0

    def increaseBalance(self, amount):
        self.balance += amount

    def setInventory(self, inventory):
        self.inventory = inventory

    def setPrice(self, prices):
        self.prices = prices

    def withdrawItem(self, item):
        if self.inventory[item] == 0:
            print("재고가 없습니다.")
            return

        if self.balance < self.prices[item]:
            print("잔액이 부족합니다.")
            return

        self.inventory[item] -= 1
        self.balance -= self.prices[item]

        print("%s 상품이 나왔습니다." % item)

    def showBalance(self):
        print("잔액 : %d" % self.balance)



v1 = VendingMachine("v1-1", "dangri")
inv = {"can1": 3, "can2": 6, "can3": 7}
price = {"can1": 1000, "can2": 1500, "can3": 1200}

v1.setInventory(inv)
v1.setPrice(price)
v1.increaseBalance(1300)

v1.withdrawItem("can1")
v1.showBalance()

v1.increaseBalance(2000)
v1.showBalance()


v1.withdrawItem("can2")
v1.showBalance()


v1.withdrawItem("can3")
v1.showBalance()


v1.increaseBalance(1300)
v1.showBalance()
