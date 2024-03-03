import sys

#
# a = 21
# print(a)
# print(type(a))
# b = 4.2
# print(b)
# print(type(b))
# tekst = 'habababa'
# print(tekst)
# print(type(tekst))
#
# a = 4
# b = 6
# f = a / b
# print(f)
# i = 6 ** (1 / 2)
# j = 6 ** 0.5
# print(i)
# print(j)
#
# a = 6
# b = 3
# print('liczba a jest rowna {}, liczba b jest rowna {}'.format(a, b))
#
# a = input('Wprowadz liczbe: ')
# a = int(a)
# print(a*5)
# print(type(a))
#
#  sys.stdout.write("Wprwadz liczbe:")
#  b = sys.stdin.readline()
#  print(b)
#  print(type(b))

# lista = [5, 6, 7, 8, 9,'a','b','c','d',[2,3,4],'ab']
# print(lista)
# lista.append(47)
# print(lista)
# lista.insert(2,'c')
# print(lista)
# lista.extend([20,21,22])
# print(lista)
# lista.pop()
# print(lista)
# lista.pop()
# print(lista)
# lista.remove([2,3,4])
# print(lista)
# del lista[1]
# print(lista)
# lista.reverse()
# print(lista)
#
# slownik = {'klucz': 'wartosc', 1:2, 'a':5, 4:'b'}
# print(slownik)
# print(slownik[4])
# slownik[6] = 45
# print(slownik)
# slownik.pop(1)
# print(slownik)
# del slownik[6]
# print(slownik)

# a = 6
# b = 7
#
# if a > b:
#     print('a is greater than b')
# elif a == b:
#     print('a is equal to b')
# else:
#     print('b is greater than a')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if (a > b) & (c > d):
#     print(a, c)
# else:
#     print(b, d)

# for i in lista:
#     print(i)
#
# for i in range(0,5):
#     for j in range(0,5):
#         result = i+j
#         print(result)
#     print('')
# licznik = 0
# while licznik < len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print('koniec petli')
# licznik = 0
# while licznik != 10:
#     if licznik == 7:
#         print(licznik)
#         break
#     else:
#         licznik += 1
# else:
#     print('licznik')

lista = [1,5,7,9,14,15,17,26]
licznik = 0
a = int(input('Wpisz liczbe: '))
while licznik < len(lista):
    if lista[licznik] - a == 0:
        print('Twoja liczba jest na liscie')
        break
    else:
        licznik += 1
else:
    print('Twojej liczby nie ma na liscie')