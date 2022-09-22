import time

a = 49
b = 234
a+b

print("Sestevek je " + str(a+b))

if a > b:
    print("a je vecji od b")
elif a < b:
    print("a je manjse od b")
else:
    print("noben pogoj ni izpolnjen")

while True:
    a += 1
    print("a je " + str(a))
    #time.sleep(0.01)
    if a > b:
        break

vhod  =  input("Vnesi najljubso st.:")
print("vasa st. je: " + str(vhod))