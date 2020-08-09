class CoffeeMachine:
    supplies_names = ["water", "milk", "coffee beans", "disposable cups", "money"]
    supplies = [400, 540, 120, 9, 550]

    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]

    stage = "start"

    def __init__(self):
        self.end = False

    # общение с пользователем
    def communication(self, stage):
        self.stage = stage
        if stage == "menu":
            command = str(input("Write action (buy, fill, take, remaining, exit):"))
            self.menu(command)
        if stage == "buy":
            coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.buy(coffee_type)
        if stage == "fill":
            water = int(input("Write how many ml of water do you want to add:"))
            milk = int(input("Write how many ml of milk do you want to add:"))
            beans = int(input("Write how many grams of coffee beans do you want to add:"))
            cups = int(input("Write how many disposable cups of coffee do you want to add:"))
            self.fill(water, milk, beans, cups)

    # основное меню
    def menu(self, command):
        if command == "remaining":
            self.remaining()
        if command == "take":
            self.take()
        if command == "exit":
            self.end = True
        else:
            stage = command
            self.communication(stage)

    # показать запасы
    def remaining(self):
        print("The coffee machine has:")
        for r in range(5):
            print(self.supplies[r], "of", self.supplies_names[r])
        print()

    # покупка
    def buy(self, coffee_type):
        ready = True
        if coffee_type == "back":
            self.communication("menu")
        if coffee_type == "1":
            for r in range(4):
                if self.supplies[r] >= self.espresso[r]:
                    self.supplies[r] = self.supplies[r] - self.espresso[r]
                    print(self.supplies)
                else:
                    print("Sorry, not enough:", self.supplies_names[r] + "!")
                    ready = False
                    break
            if ready:
                self.supplies[4] += self.espresso[4]
                print("I have enough resources, making you a coffee!")
        if coffee_type == "2":
            for r in range(4):
                if self.supplies[r] >= self.latte[r]:
                    self.supplies[r] -= self.latte[r]
                else:
                    print("Sorry, not enough:", self.supplies_names[r] + "!")
                    ready = False
                    break
            if ready:
                self.supplies[4] += self.latte[4]
                print("I have enough resources, making you a coffee!")
        if coffee_type == "3":
            for r in range(4):
                if self.supplies[r] >= self.cappuccino[r]:
                    self.supplies[r] -= self.cappuccino[r]
                else:
                    print("Sorry, not enough:", self.supplies_names[r] + "!")
                    ready = False
                    break
            if ready:
                self.supplies[4] += self.cappuccino[4]
                print("I have enough resources, making you a coffee!")

    # пополнение
    def fill(self, water, milk, beans, cups):
        self.supplies[0] += water
        self.supplies[1] += milk
        self.supplies[2] += beans
        self.supplies[3] += cups

    # забрать деньги
    def take(self):
        print("I gave you, $" + str(self.supplies[4]))
        self.supplies[4] = 0


while True:
    coffee = CoffeeMachine()
    coffee.communication("menu")
    if coffee.end:
        break
