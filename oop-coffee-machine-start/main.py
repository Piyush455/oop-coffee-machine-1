from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

print(coffee.resources)

choice = input("Enter drink name you want ")
drink = menu.find_drink(choice)
print(coffee.is_resource_sufficient(drink))