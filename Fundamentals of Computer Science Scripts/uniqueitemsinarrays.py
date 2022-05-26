#This program reads an array, and tells the user the total amount of items in it along with the amount of unique items.
fruits = ["apple", "pear", "orange", "banana", "pear", "grape", "apple"]
print(fruits)
print(f"In this array of strings, there are {len(fruits)} fruits.")
print(f"In this array of strings, there are {len(set(fruits))} unique fruits.")