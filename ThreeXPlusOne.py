import matplotlib.pyplot as plt

def odd_even (num):
    if (num % 2 == 0):
        return "even"
    else:
        return "odd"

x = []
step_count = 0

num = int (input ("Enter a number: "))
print ()

file1 = open ('Results.txt', 'w')

while True:
    step_count += 1
    if (num == 1):
        print (num)
        file1.writelines (str (num) + '\n')
        x.append (num)
        break
    else:
        if (odd_even (num) == "odd"):
            print (num)
            file1.writelines (str (num) + '\n')
            x.append (num)
            num = 3 * num + 1
        elif (odd_even (num) == "even"):
            print (num)
            file1.writelines (str (num) + '\n')
            x.append (num)
            num = int (num / 2)

file1.close()

print ("\nTotal number of steps =", step_count)
print ("Largest number =", max (x))

plt.plot (x)
plt.show ()