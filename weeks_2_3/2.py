"""
Project: Basta Fazoolin'
You’ve started a position as the lead programmer for the family-style Italian restaurant 
Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen 
a lot of growth lately. You’ve been hired to keep things organized.
"""
from os import name
from symtable import Class


# --- Making the Menus ---

# 1. Create a Menu class.
class Menu:

# 2. Give Menu a constructor with the five parameters: 
# self, name, items, start_time, and end_time.


    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

#7. Give the Menu class a string representation method that returns the name
# of the menu and its availability.
    def __str__(self):
        return f'{self.name} menu available from {self.start_time} to {self.end_time}'

# 9. Give Menu a method .calculate_bill() that takes self and purchased_items
# (a list of item names) and returns the total price.
    def calculate_bill (self, purchased_items):
        total_price = 0
        for item in purchased_items:
            total_price += self.items[item]
        return total_price
# 3. Create the brunch menu object.
# Name: 'brunch'
# Time: 11am to 4pm
# Items: {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}BRINHC
brunch = Menu(name= 'brunch', items= {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                                      'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},
                                       start_time= 11, end_time= 16)
# 4. Create the early_bird menu object.
# Name: 'early_bird'
# Time: 3pm to 6pm
# Items: {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
# 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
# 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu(name= 'early_bird',
                  items= {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                        'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                        'coffee': 1.50, 'espresso': 3.00},
                        start_time= 15, end_time= 18)

# 5. Create the dinner menu object.
# Name: 'dinner'
# Time: 5pm to 11pm
# Items: {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
# 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu(name= 'dinner',
                  items= {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
                        'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00},
                        start_time= 17, end_time= 23)


# 6. Create the kids menu object.
# Name: 'kids'
# Time: 11am to 9pm
# Items: {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu(name= 'kids',
                  items= {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00},
                        start_time= 11, end_time= 21)

# 7. Give the Menu class a string representation method that returns the name 
# of the menu and its availability.


# 8. Test the string representation by printing the brunch menu.
print(brunch)


# 9. Give Menu a method .calculate_bill() that takes self and purchased_items 
# (a list of item names) and returns the total price.


# 10. Test .calculate_bill() on the brunch menu with: 
# ['pancakes', 'home fries', 'coffee']
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))


# 11. Test .calculate_bill() on the early_bird menu with: 
# ['salumeria plate', 'mushroom ravioli (vegan)']
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# --- Creating the Franchises ---

# 12. Create a Franchise class.
class Franchise:


# 13. Give Franchise a constructor that takes an address and a list of menus.
    def __init__(self, address, list_of_menus):
        self.address = address
        self.list_of_menus = list_of_menus
    def __str__(self):
        return f'Address: {self.address}'
    def available_menus(self, time):
        available_menus = [ ]
        for menu in self.list_of_menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus.append(menu)
        return available_menus



# 14. Create the first two franchises:
# flagship_store: "1232 West End Road" (all four menus)
# new_installment: "12 East Mulberry Street" (all four menus)
flagship_store = Franchise(address="1232 West End Road",
                           list_of_menus=[brunch, early_bird, dinner, kids])
new_installment = Franchise(address="12 East Mulberry Street",
                           list_of_menus=[brunch, early_bird, dinner, kids])


# 15. Give Franchise a string representation that returns the address.
print(flagship_store)


# 16. Give Franchise an .available_menus() method that takes a time and 
# returns a list of Menu objects available at that hour.
availible_menu = flagship_store.available_menus(12)
print('manu at 12')
for menu in availible_menu:
    print(menu.name)


# 17. Test .available_menus() at 12 noon (12) and print the results.


# 18. Test .available_menus() at 5pm (17) and print the results.
availible_menu_17 = flagship_store.available_menus(17)
print('meny at 17')
for menu in availible_menu_17:
    print(menu.name)


# --- Creating Businesses ---

# 19. Define a Business class.
class Business:


# 20. Give Business a constructor that takes a name and a list of franchises.
    def __init__(self, name, list_of_Franchises ):
        self.name = name
        self.list_of_Franchises = list_of_Franchises


# 21. Create the first Business:
# Name: "Basta Fazoolin' with my Heart"
# Franchises: [flagship_store, new_installment]


# 22. Create the arepas_menu object.
# Name: 'take_a_arepa'
# Time: 10am to 8pm
# Items: {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}


# 23. Create the arepas_place franchise.
# Address: "189 Fitzgerald Avenue"
# Menus: [arepas_menu]


# 24. Create the new Business object.
# Name: "Take a' Arepa"
# Franchises: [arepas_place]