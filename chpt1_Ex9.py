print("Would you like to continue? (Yes/No)")

cont = input()

num_loops = 0

while cont == "Y":
    num_loops += 1
    print("Would you like to continue? (Yes/No)")
    cont = input()

print("The loop executed " + str(num_loops) + " times")