'''Create a tuple coordinates = (10, 20) and print both elements.
Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.'''

coordinate = (10,20)
print(coordinate)
#coordinate[0] = 50 immutable
lists = list(coordinate)
lists[0] = 50
coordinate = tuple(lists)
print(coordinate)