from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    
    print('Cofee Machine Switched On!')

    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    
    
    is_on = True
    menu = Menu()

    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? {options} : ")

        if choice == 'off':
            is_on  = False
            print('Cofee Machine Switched OFF!')
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)





    # print('Cofee Machine Switched Off!')

