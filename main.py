tausch = True
liste = [16, 4, 9, 17, 13, 23]
print(liste)
while tausch:
    tausch= False
    for i in range(0,len(liste)-1):
        if liste[i] >= liste[i+1]:
            temp = liste[i]
            liste[i] = liste[i+1]
            liste[i+1] = temp
            tausch = True
print(liste)