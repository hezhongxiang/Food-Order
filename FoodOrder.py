from tabulate import tabulate


Foods = [

    ["","MENUS OF 6'OCLOCK RESTAURANT",""],

    ["No.","Food Item", "Price"],

    ["1","Mohinga (Fish Noodle Soup)", 3000],

    ["2","Shan Noodle (Simple)", 4500],

    ["3.","Nan Gyi Thoke (Noodle Salad)",5000],

    ["4.","Fried Rice with Egg/Chicken",6000],

    ["5.","Burmese Oily Pork Curry (Si Byan)",6500],

    ["6.","Oily Chicken Curry (Si Byan)",5500],

    ["7.","Plain Steamed Rice (per serving)",1000],

    ["8.","Tea Leaf Salad (Laphet Thoke)",5000],

    ["9.","Coconut Milk Noodle (Ohn No Khao Swe)",4500],

    ["10.","Stir-Fried Water Spinach (In Bay)",7500],

]


headers = Foods[0]

rows = Foods[1:]


print(tabulate(rows, headers=headers, tablefmt="fancy_grid", stralign="left", numalign="center"))

print("\n")


class Ordertable():

    menus = {

        "Mohinga (Fish Noodle Soup)":3000,

        "Shan Noodle (Simple)":4500,

        "Nan Gyi Thoke (Noodle Salad)":5000,

        "Fried Rice with Egg/Chicken":6000,

        "Burmese Oily Pork Curry (Si Byan)":6500,

        "Oily Chicken Curry (Si Byan)":5500,

        "Plain Steamed Rice (per serving)":1000,

        "Tea Leaf Salad (Laphet Thoke)":5000,

        "Coconut Milk Noodle (Ohn No Khao Swe)":4500,

        "Stir-Fried Water Spinach (In Bay)":7500

    }


    def __init__(self):
        self.total = 0
        self.orders = []
      
    def jls_extract_def(self, order):
        return order

    def add_order(self, order):
        if order not in self.menus:
            print(f"'{order}' is not on the menu.")
            return

        self.orders.append(order)
        self.total += self.menus[order]
        print(f"Added: {order} - {self.menus[self.jls_extract_def(order)]}")

    def print_bill(self):
        if not self.orders:
            print("No orders placed.")
            return

        print('\n')
        print("Bill")

        orderlist = [["Order", "Price"]]
        for o in self.orders:
            orderlist.append([o, self.menus[o]])

        headers = orderlist[0]
        rows = orderlist[1:]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid", stralign="left", numalign="center"))

        print('Total: ', self.total)
        

def start_program():
    order = Ordertable()

    while True:
        order_input = input('Order: ')
        order.add_order(order_input)
        another = input('Order again (y/n):')

        if another == 'y':
            continue
        if another == 'n':
            order.print_bill()
            break
start_program()