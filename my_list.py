# WEEK TWO ASSIGNMENT
# DATA STRUCTURES

# Create an empty list
my_list = []

# Appends empty list with the following values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserts 15 at position 2 [index 1]
my_list.insert(1, 15)

# Extends list to include list
my_list.extend([50, 60, 70])

# Deletes the last element in the list
my_list.pop(-1)

# Sorts the list the ascending order
i = 0
for i in range(len(my_list) - 1):
    if (my_list[i] >  my_list[i+1]):
        holder = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = holder
        i = i + 1

# Print the index of the value 30 in my_list
print(my_list.index(30))