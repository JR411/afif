# Nomor 1
def no1():
    n = int(input("Banyak Element Array : "))
    list = []
    for i in range(0,n):
        element = int(input("- "))
        list.append(element)

    print("Sebelum diurut : ",list)
    
    for i in range(0,n):
        for j in range(0,n):
            if list[i]<list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

    print("Setelah diurut : ",list)

# Nomor 2
def no2():
    n = int(input("Bilangan Bulat : "))
    for i in range(2,n):
        if n % i == 0:
            print("Ini bukan Bilangan Prima")
        else:
            print("Ini Bilangan Prima")
        break

# Nomor 3
def no3():
    n = int(input("Bilangan Bulat : "))
    faktorial = 1
    for i in range(1, n+1):
        faktorial *= i
    
    print(f"{n}! = {faktorial}")

no1()
no2()
no3()