import time


def main():
    """
    sum = 0
    l1 = [1, 2, 3, 5, 6, 6, 3]
    for num in l1:
        sum = sum + num
        #print(sum)

    #for i in range(2, 10, 3): #od 2 do 10 s korakom po 3
    #for i in range(len(l1)):
    """

    """
    l2 = [vred for vred in l1 if vred > 5]
    print(l2)

    d1 = {1:"a", 2:"b", 3:"c", 4:"d"}

    for k, v in d1.items(): #k = kljuc, v = vrednost
        print(v)

    for v in d1.items(): #v je v tem primeru enak kljucu in vrednosti skupaj
        print(v)
    """

    try:
        d0 = 1/0
    except Exception as e:
        print("ni ratalo napaka = " + str(e))

    finally: #lahko uporabimo tudi brez excepta npr. za zapiranje dilav,
            #ker ga moramo v vsakem primeru zepreti da ga lahko vindows se prebere
        print("zakljuceno")


    # elegantno zapiranje programa
    try:
        while True:
            print("neki")
            time.sleep(1)

    except KeyboardInterrupt:
        print("exiting...")



if __name__ == "__main__":
    main()