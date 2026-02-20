class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key): 
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range (len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        keys_list = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    keys_list.append(self.data_map[i][j][0])
        return keys_list
    
    def print(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

hash_table = HashTable()
hash_table.set_item('A', 1)
hash_table.set_item('B', 2)
hash_table.set_item('C', 3)
hash_table.set_item('D', 4)
hash_table.set_item('E', 5)
hash_table.set_item('F', 6)
hash_table.set_item('G', 7)
hash_table.set_item('H', 8)
hash_table.set_item('I', 9)
hash_table.set_item('J', 10)
hash_table.set_item('K', 11)
hash_table.print()
print("_"*50)
# print("A is at index: ", hash_table.get_item('A'))
# print("C is at index: ", hash_table.get_item('C'))
# print("E is at index: ", hash_table.get_item('E'))
# print("H is at index: ", hash_table.get_item('H'))
# print("Z is at index: ", hash_table.get_item('Z'))

print(hash_table.keys())