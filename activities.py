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

def main():
    # some_tuple = (1,2,3,4,5)
    # another_tuple = tuple("abcdef")
    # tuples(another_tuple)
    # packed = packer()
    # print(packed[0])
    # print(packed[1])
    # print(packed[2])
    # print(packed[3])
    print(lists())

if __name__ == "__main__":
    main()