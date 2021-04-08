def boredom(staff):
    #your code here
    bore={"accounts":1,"finance":2,"canteen":10,"regulation":3,"trading":6,"change":6,"IS":8,"retail":5,"cleaning":4,"pissing about":25}
    total = sum(bore[staff[name]] for name in staff.keys()) 
    if total<=80:
        return "kill me now"
    elif total <100:
        return 'i can handle this'
    else:
        return 'party time!!'
