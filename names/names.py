import time
from doubly_linked_list import DoublyLinkedList

start_old = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_old = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_old - start_old} seconds")


start_new = time.time()

def make_DLL(arr):
    new_DLL = DoublyLinkedList()
    for i in arr:
        new_DLL.add_to_tail(i)
    return new_DLL

new_names_1 = make_DLL(names_1)
new_names_2 = make_DLL(names_2)
duplicates = []

node_1 = new_names_1.head
node_2 = new_names_2.head

for i in range(new_names_1.length):
    for j in range(new_names_2.length):
        if node_1.value is node_2.value:
            duplicates.append(node_1.value)
        if node_2.next is None:
            break
    if node_1.next is None:
        break
    node_1 = node_1.next







end_new = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_new - start_new} seconds")
