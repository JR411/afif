# No 1
def no1():
    x=int(input('x = '))
    y=int(input('y = '))

    if(x>y):
        print("y harus lebih besar dari x")
        exit()
    
    for i in range (y):
        i += 1
        print(i,end=" ")
        if(i%x == 0):
            for j in range (1):
                print('')

no1()

# No 2
from datetime import date, datetime, time, timedelta

def no2():
    M = float(input("M(0-360) = "))  
    waktu = datetime.combine(date.today(), time(6,0,0)) + timedelta(seconds=240*M)

    if 0 <= M < 90 or M == 360:
        print("Selamat Pagi")
        print(waktu.time().replace(microsecond=0))
    elif(90 <= M < 135):
        print("Selamat Siang")
        print(waktu.time().replace(microsecond=0))
    elif(135 <= M < 180):
        print("Selamat Sore")
        print(waktu.time().replace(microsecond=0))
    elif(180 <= M < 360):
        print("Selamat Malam")
        print(waktu.time().replace(microsecond=0))
    else:
        print("Inputan Salah")

no2()

# No 3
def no3():
    harga = int(input("Harga Barang = "))
    bayar = int(input("Dibayar = "))
    
    if(harga > bayar):
        print("Uang anda tidak cukup")
        exit()
    
    kembali = bayar - harga
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0

    if(kembali >= 100000):
        for a in range(kembali):
            a = a + 1
            kembali = kembali - 100000
            if(kembali < 100000):
                break
    if(kembali >= 50000):
        for b in range(kembali):
            b = b + 1
            kembali = kembali - 50000
            if(kembali < 50000):
                break
    if(kembali >= 20000):
        for c in range(kembali):
            c = c + 1
            kembali = kembali - 20000
            if(kembali < 20000):
                break
    if(kembali >= 10000):
        for d in range(kembali):
            d = d + 1
            kembali = kembali - 10000
            if(kembali < 10000):
                break
    if(kembali >= 5000):
        for e in range(kembali):
            e = e + 1
            kembali = kembali - 5000
            if(kembali < 5000):
                break
    if(kembali >= 2000):
        for f in range(kembali):
            f = f + 1
            kembali = kembali - 2000
            if(kembali < 2000):
                break
    if(kembali >= 1000):
        for g in range(kembali):
            g = g + 1
            kembali = kembali - 1000
            if(kembali < 1000):
                break

    print(a,"uang Rp. 100.000")
    print(b,"uang Rp. 50.000")
    print(c,"uang Rp. 20.000")
    print(d,"uang Rp. 10.000")
    print(e,"uang Rp. 5.000")
    print(f,"uang Rp. 2.000")
    print(g,"uang Rp. 1.000")

no3()