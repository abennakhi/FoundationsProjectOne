####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Ahmad and Mariam's Boutique"#complete me!
signature_flavors = ["Pistachio", "Peanut Butter", "Almond"]
order_list = []


def print_menu():
    print("Our menu:" )
    for flavor in menu:
        print("- \"" + flavor +"\" " +"(KD" + str(menu[flavor]) + ")")
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for flavor in original_flavors:
        print("- \"" + flavor +"\" ")
    # your code goes here!


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for flavor in signature_flavors:
        print("- \"" + flavor +"\" ")
    # your code goes here!


def is_valid_order(order):
    status = False
    for item in menu:
      if(order == item):
        status = True
    for item in original_flavors:
      if(order == item):
        status = True
    for item in signature_flavors:
      if(order == item):
        status = True
    return status
    """
    Check if an order exists in the shop.
    """
    # your code goes here!


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order = ""
    order_list = []
    print("What's your order?(Enter the exact spelling of the item you want. Type 'Exit' to end your order.)")
    while(order != "Exit"):
        order = str(input('>> '))
        if( order != 'Exit' and is_valid_order(order)):
          order_list.append(order)
    # your code goes here!
    #print(order_list)
    return order_list


def accept_credit_card(total):
    if(total >= 5):
        print("This order is eligible for credit card payment.")
    else:
        print("This order is not eligible for credit card payment.")
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    price = 0
    # your code goes here!
    for order in order_list:
      for item in menu:
          if(order == item):
            price = menu[item]
            total += price
      for item in original_flavors:
          if(order == item):
            price = original_price
            total += price
      for item in signature_flavors:
        if(order == item):
            price = signature_price
            total += price
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print("Your order is: " + str(order_list))
    print("That will be KD "+str(get_total_price(order_list)))
    print("Thank you for shopping at Cake and Baker")
    # your code goes here!
