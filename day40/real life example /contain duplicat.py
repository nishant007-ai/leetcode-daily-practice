  def remove_duplicates(items):
    # Convert list to a set (removes duplicates)
    unique_items = list(set(items))
    return unique_items

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(numbers)
print("Original list:", numbers)
print("Without duplicates:", result)
