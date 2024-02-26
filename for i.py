# i want to print the multiplication table for 1 to 10
for i in range(1,11):
    for j in range (1,11):
        print(i, "x", j,"=", i*j)
    print()

for i in range(1, 11):
    for j in range(1, 11):  # Starting from 1 for a complete table
        print(i, "x", j, "=", i*j)
    print()  # This prints a newline to separate each multiplication table
