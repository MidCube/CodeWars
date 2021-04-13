def digital_root(n):
    # change the number into a word so 123 is "123"
    n = str(n)
    # now we can get each number on their own using a loop
    total=0
    for letter in n:
        #turn the 'letter' back into a number and add it to total
        total+=int(letter)
    # you did all this great but the next step is something called recursion,
    # that means that if the number is more than 1 digit (we can check with
    # len(str(total))) then we want to run digital root on the total and return
    # the result (If the number isn't one digit the function to execute is the one 
    # we just did!)
    if len(str(total))>1:
        return digital_root(total)
    else:
        return total
