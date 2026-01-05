def tic(one, two):
    difference = one - two
    return difference


def tac(exp):
    product = 1
    for n in range(exp):
        product *= 5
    return product


def toe():
    print(tic(3,5))
    print(tac(4))
print(toe())