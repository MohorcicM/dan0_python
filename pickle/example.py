import pickle

if __name__ == "__main__":
    l1 = [1, 2, 2, 6, 6, 7]

    h = open("tocka2.pkl", 'wb') #b dodamo zato, ker je pkl bitna datoteka in zelimo zapisovati bitno ne textovno
    pickle.dump(l1, h, pickle.HIGHEST_PROTOCOL)

    h.close()

    with open("tocka2.pkl", 'wb') as h:
        pickle.dump(l1, h, pickle.HIGHEST_PROTOCOL)