# validate if answer is Y = Yes or N = No for multiple inputs and print valid inputs


# validates inputs if Yes = Y or No = N
def m(u, i, o, p):
    # reference
    isvalid = ['Y', 'N']

    # comparator
    if u in isvalid and i in isvalid and o in isvalid and p in isvalid:
        print("Correct inputs entered")
        print("tired: ", u, "; hungry: ", i, "; sleepy: ", o, "; bored: ", p)

    else:
        print("Invalid inputs entered try again")
        print('\n')
        g()

    
# inputs and calling comparator
def g():
    h = input("tired = Y or N: ").upper()
    j = input("hungry = Y or N: ").upper()
    k = input("sleepy = Y or N: ").upper()
    z = input("bored = Y or N: ").upper()
    m(h, j, k, z)


if __name__ == "__main__":
    g()
