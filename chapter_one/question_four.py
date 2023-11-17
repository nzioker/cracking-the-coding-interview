# my solution.
# in hindsight, it's better to use a hash map than a list because you can use the hash map 
# to store the number of times an elemt appears.
def check_anagram(string_one, string_two):
    string_one_list = [x for x in string_one]
    string_two_list = [x for x in string_two]
    print(string_two_list)
    print(string_one_list)

    for i in string_one_list:
        for j in string_two_list:
            if j == i:
                string_one_list.remove(i)
                string_two_list.remove(j)
    print(string_one_list)
    print(string_two_list)
    if len(string_one_list) == 0 and len(string_two_list) == 0:
        return True
    return False


# Geeks for Geeks. Very sneaky and easy
def check_anagram_two(string_one, string_two):
    return sorted(string_one) == sorted(string_two)


# Using a dictionary

def check_anagram_three(string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    
    string_holder = {}

    for i in range(len(string_one)):
        if string_one[i] in string_holder:
            string_holder[string_one[i]] += 1
        else:
            string_holder[string_one[i]] = 1

    for i in range(len(string_two)):
        if string_two[i] in string_holder:
            string_holder[string_two[i]] -= 1
        else:
            return False

    map_keys = string_holder.keys()
    for key in map_keys:
        if string_holder[key] != 0:
            False

    return True

if __name__ == '__main__':
    print(check_anagram_three("mane", "name"))
