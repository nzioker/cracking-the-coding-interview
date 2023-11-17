# my solution
def unique_string(string):
    unique_list = []
    for i in string:
        if i not in unique_list:
            unique_list.append(i)

    if len(unique_list) == len(string):
        return True
    return False


# New way to solve this after researching on SO.
def unique_string_so(string):
    return len(set(string)) == len(string)


# replace the list with a set in the first solution
def unique_string_replaced(string):
    unique_set= set()
    for i in string:
        if i not in unique_set:
            unique_set.add(i)

    if len(unique_set) == len(string):
        return True
    return False

if __name__ == '__main__':
    print(unique_string_so("Waterr"))