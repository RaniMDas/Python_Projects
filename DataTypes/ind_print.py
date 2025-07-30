my_list = ["apple", "banana", "cherry", "date"]
target_object = "cherry"

index = -1  # Initialize index to -1, indicating not found
for i in range(len(my_list)):
    if my_list[i] == target_object:
        index = i
        break  # Exit the loop once found

if index != -1:
    print(f"The index of '{target_object}' is: {index}")
else:
    print(f"'{target_object}' not found in the list.") 