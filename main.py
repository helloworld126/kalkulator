
# Kalkulator

### Opcje:

## int = jedynie liczby
## string (albo bez int) = liczby i litery 

a = int(input("Podaj Pierwszą Liczbę: "))
b = int(input("Podaj Drugą Liczbę: "))
c = input("Podaj Działanie (+,-,*,/): ")


##### funkcje

def dodaj(p,d):
	return p+d

def odejmij(p,d):
	return p-d
	
def pomnoz(p,d):
	return p*d
	
def podziel(p,d):
	return p/d
	
##### skrypt


if c == "+":
	print(a,c,b,"=",dodaj(a,b))
elif c == "-":
	print(a,c,b,"=",odejmij(a,b))
elif c == "*":
	print(a,c,b,"=",pomnoz(a,b))
elif c == "/":
	print(a,c,b,"=",podziel(a,b))
	
#### zakończenie 

print("Kalkulator stworzony przez GRZEGORZ BARTOSZ!")
