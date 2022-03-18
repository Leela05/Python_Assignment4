# Using while loop and an if statement write a function named name_ adder
# which appends all the elements in a list to a new list unless the element
# is an empty string: "".

list1=["Joe", "thara", "Adhi", "Amu", "", "Elena"]
def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        i = i+1
    return new_list
print(name_adder(list1))