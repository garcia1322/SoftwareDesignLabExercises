# Function to display hashtable
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


# Creating Hashtable as
# a nested list.
HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


# Driver Code
insert(HashTable, 10, 'Lance')
insert(HashTable, 25, 'Mark')
insert(HashTable, 20, 'Lawrence')
insert(HashTable, 9, 'Martin')
insert(HashTable, 21, 'Garcia')
insert(HashTable, 21, 'AG')

display_hash(HashTable)
