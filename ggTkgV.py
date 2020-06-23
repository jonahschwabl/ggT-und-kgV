a = 3
b = 4


def ggT(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


print("ggT: %s" % ggT(a, b))

print("kgV: %s" % (a*b/ggT(a, b)))
