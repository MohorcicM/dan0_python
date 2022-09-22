
def main():

    imenik =  { "Ana P": 241765546, "Marko K": 565546789, "Janez N": 514548532, "Neza J": 443989632, "Anamarija J": 654879684}

    im_za_klic = [(ime, st) for ime, st in imenik.items() if ime[0] == 'A']
    
    for ime, st in im_za_klic:
        print("Klicem " + ime + " na tel st. " + str(st))

if __name__ == "__main__":
    main()