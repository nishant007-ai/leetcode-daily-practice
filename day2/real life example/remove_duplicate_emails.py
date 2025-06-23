# Example usage
names = [
    "Nishant",
    "Nishant",
    "Prashant",
    "Sushant",
    "Sushant",
    "Yash"
]

def remove_duplicate_names(name_list):
    if not name_list:
        return 0
    
    unique_index = 1
    for i in range(1, len(name_list)):
        if name_list[i] != name_list[i - 1]:
            name_list[unique_index] = name_list[i]
            unique_index += 1
    
    return name_list[:unique_index
                     

Unique Names: ['Nishant', 'Prashant', 'Sushant', 'Yash']
