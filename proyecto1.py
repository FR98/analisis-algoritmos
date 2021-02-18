"""
---------------------------------------------------------------------------------------------------
	Author
	    Francisco Rosal 18676
---------------------------------------------------------------------------------------------------
"""

f = lambda x: x + 1
g = lambda x: x * 2
h = lambda x, y: pow(x, 2) + pow(y, 2)
cero = lambda f, x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: b(a(f))(x)

x = 5
y = 2
n = 1
a = 1
b = 2

resA = f(x)
resB = g(x)
resC = h(x, y)
resD = cero(f, x)
resE = uno(f)(x)
resF = dos(f)(x)
resG = tres(f)(x)
resH = sucesor(uno)(f)(x)
resI = suma(uno)(dos)(f)(x)
resJ = multiplicacion(uno)(dos)(f)(x)

print("\n𝑓(𝑥)=𝑥+1\t\t\t\t, 𝑥={}: ".format(x), resA)
print("\n𝑔(𝑥)=2𝑥\t\t\t\t\t, 𝑥={}: ".format(x), resB)
print("\nℎ(𝑥,𝑦)=𝑥2+𝑦2\t\t\t\t, 𝑥={}, 𝑦={}: ".format(x, y), resC)
print("\n𝑐𝑒𝑟𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑥\t\t\t, 𝑥={}: ".format(x), resD)
print("\n𝑢𝑛𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑥\t\t\t, 𝑥={}: ".format(x), resE)
print("\n𝑑𝑜𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑥\t\t\t, 𝑥={}: ".format(x), resF)
print("\n𝑡𝑟𝑒𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑓𝑥\t\t\t, 𝑥={}: ".format(x), resG)
print("\n𝑠𝑢𝑐𝑒𝑠𝑜𝑟(𝑛,𝑓,𝑥)=𝜆𝑛.𝜆𝑓.𝜆𝑥(𝑓(𝑛𝑓(𝑥)))\t, 𝑥={}, 𝑛={}: ".format(x, n), resH)
print("\n𝑠𝑢𝑚𝑎(𝑎,𝑏,𝑓,𝑥)\t\t\t\t, 𝑥={}, 𝑎={}, 𝑏={}: ".format(x, a, b), resI)
print("\n𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑐𝑎𝑐𝑖o𝑛(𝑎,𝑏,𝑓,𝑥)\t\t\t, 𝑥={}, 𝑎={}, 𝑏={}: ".format(x, a, b), resJ)
