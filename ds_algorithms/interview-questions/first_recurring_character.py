def first_recurring_character(items):
    hashtable = {}
    for item in items:
        if item in hashtable:
            return item
        hashtable[item] = item
    return None


items = [2, 5, 1, 2, 1, 6, 8, 4, 9]
print(first_recurring_character(items))
