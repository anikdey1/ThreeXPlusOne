import matplotlib.pyplot as plt

# This function checks whether a number is even or odd.
def odd_even(num):
    if(num % 2 == 0):
        return "even"
    else:
        return "odd"

x = []
step_count = 0

# This variable stores the number entered by the user.
num = int(input("Enter a number: "))
print()

file1 = open('Results.txt', 'w')

# This loop computes the Collatz function for the number until it reaches 1.
while True:
    step_count += 1
    if(num == 1):
        print(num)
        file1.writelines(str(num) + '\n')
        x.append(num)
        break
    else:
        if(odd_even(num) == "odd"):
            print(num)
            file1.writelines(str(num) + '\n')
            x.append(num)
            num = 3 * num + 1
        elif(odd_even(num) == "even"):
            print(num)
            file1.writelines(str(num) + '\n')
            x.append(num)
            num = int(num / 2)

# This function writes the steps into the Results.txt file.
file1.close()

# These print functions provide an output with some additional information.
print("\nTotal number of steps =", step_count)
print("Largest number =", max(x))


# These functions plot and display the graph.
plt.plot(x)
plt.xlabel('Steps')
plt.ylabel('Height (in Increments of 10)')
plt.show()