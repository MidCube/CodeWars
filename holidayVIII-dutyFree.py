def duty_free(price, discount, holiday_cost):
    savedPerSale = price*discount/100
    num = int(holiday_cost/savedPerSale)
    return num
