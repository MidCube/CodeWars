def mango(quantity, price):
    return (((quantity-quantity%3)/3*2)+quantity%3)*price
