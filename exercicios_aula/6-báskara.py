ax = float(input("Digite o numero de ax:"))
bx= float(input("Digite o numero de bx:"))
c= float(input("Digite o numero de c:"))

delta = (bx** 2) - 4 * ax * c


x1 = (-bx + delta ** (1 / 2)) / (2 * ax)
x2 = (-bx - delta ** (1 / 2)) / (2 * ax)

print("x1: {}, x2: {}".format(x1, x2))