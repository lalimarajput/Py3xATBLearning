def make_pizza(*topings, base):  # topings and base is an argument defined by user
    print(topings, base)
    for n in topings:
        print(n)
Lalima = make_pizza("tomato", "onion", "corn", base="thin crust")
    # calling user defined arguments
