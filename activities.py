def tuples(a_tuple):
    print(len(a_tuple))
    print(a_tuple)
    for element in a_tuple:
        print(element)

    # Attempting to change 1 of the index
    a_tuple[2] == 5

def packer():
    return "a", 1 , "b", 2

def lists():
    some_list = ["1", True, 3.1, None]
    for index in range(len(some_list)):
        print(some_list[index])
    some_list[1] = False
    return some_list

def make_list(a_sequence):
    a_list = []
    for element in a_sequence:
        a_list.append(element)
        print(a_list)
    return a_list

def scale(a_list, scalar):
    for index in range(len(a_list)):
        a_list[index] = a_list[index] * scalar
    return a_list

def mutater(a_list, an_int):
    print(a_list)
    print(an_int)
    an_int = an_int * 5
    a_list[0] = a_list[0] * 5
    print(a_list)
    print(an_int)
    return

def main():
    # some_tuple = (1,2,3,4,5)
    # another_tuple = tuple("abcdef")
    # tuples(another_tuple)
    # packed = packer()
    # print(packed[0])
    # print(packed[1])
    # print(packed[2])
    # print(packed[3])
    # print(lists())
    # some_seq = [1,2,3,4,5]
    # print(make_list(some_seq))
    # new_list = make_list(range(1,5))
    # print(new_list)
    # print(scale(new_list, 3))
    var_1 = 5
    list_1 = [2,5,6]
    mutater(list_1, var_1)
    print(var_1)
    print(list_1)

if __name__ == "__main__":
    main()