class Coffee:
    def __init__(self):
        self.machine_money = 550
        self.machine_water = 400
        self.machine_milk = 540
        self.machine_beans = 120
        self.machine_cups = 9

    def __str__(self):
        return f'{self.machine_water, self.machine_milk, self.machine_beans, self.machine_cups, self.machine_money}'

    def action(self, action):
        if action == '1':
            if self.check_amounts(water=250, milk=0, beans=16, cups=1):
                self.machine_water -= 250
                self.machine_beans -= 16
                self.machine_cups -= 1
                self.machine_money += 4
        elif action == '2':
            if self.check_amounts(water=350, milk=75, beans=20, cups=1):
                self.machine_water -= 350
                self.machine_milk -= 75
                self.machine_beans -= 20
                self.machine_cups -= 1
                self.machine_money += 7
        elif action == '3':
            if self.check_amounts(water=200, milk=100, beans=12, cups=1):
                self.machine_water -= 200
                self.machine_milk -= 100
                self.machine_beans -= 12
                self.machine_cups -= 1
                self.machine_money += 6
                print()
        elif action == 'back':
            pass

    def check_amounts(self, water, milk, beans, cups):
        if self.machine_water < water:
            print(self.machine_water, water)
            print(f"Sorry, not enough water")
            return False
        if self.machine_milk < milk:
            print(f"Sorry, not enough milk")
            return False
        if self.machine_beans < beans:
            print(f"Sorry, not enough beans")
            return False
        if self.machine_cups < cups:
            print(f"Sorry, not enough cups")
            return False
        return True

    def selection(self, option):
        print()
        if option == 'buy':
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            task.action(input())
        elif option == 'fill':
            self.fill()
        elif option == 'take':
            self.take()
        elif option == 'remaining':
            self.status()
        elif option == 'exit':
            exit()

    def fill(self):
        self.machine_water += int(input('Write how many ml of water do you want to add:'))
        self.machine_milk += int(input('Write how many ml of milk do you want to add:'))
        self.machine_beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.machine_cups += int(input('Write how many disposable cups of coffee do you want to add:'))
        print()

    def status(self):
        print("The coffee machine has:")
        print(f'{self.machine_water} of water')
        print(f'{self.machine_milk} of milk')
        print(f'{self.machine_beans} of coffee beans')
        print(f'{self.machine_cups} of disposable cups')
        print(f'${self.machine_money} of money')
        print()

    def take(self):
        print(f'I gave you ${self.machine_money}')
        print()
        self.machine_money = 0


task = Coffee()
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    task.selection(input())