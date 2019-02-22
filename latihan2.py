print(" Program menampilkan bilangan terbesar dari n buah data yang diinputkan ")
print(" ...Masukan angka 0 untuk berhenti... ")

list1=[]
a=int (input("Masukkan bilangan: "))
list1.append(a)
while (a != 0):
    a=int(input("Masukkan bilangan: "))
    list1.append(a)
print("Bilangan terbesar adalah ",max(list1))
