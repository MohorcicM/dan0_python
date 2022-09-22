def main():
    test = 1
    l1 = [0, "Matej", True, 1.04, test, [2, 0.4]] #list
    print(l1[5])
    l1[2] = False
    l1.append(1111) #dodamo vrednost na konec
    l1.pop() #odstranimo vrednost
    l1.insert(3, "test") #npr. na indeks 3 dodamo nek string
    print(l1)

    d1 = {"ABC":123, 17:"Nekaj"} #dictionary
    print(d1[17]) #iscemo glede na kljuc (ABC, 17)


    t1 = () #tupl je imutable(nespremenljiva)

if __name__ == "__main__":
    main()