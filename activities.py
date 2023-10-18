import random
import arrays
import array_utils

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

def cat(a_list, b_list):
    return a_list + b_list

def extender(a_list, b_list):
    a_list += b_list
    return a_list

def inserter(a_list, value):
    mid_point = len(a_list)//2
    a_list.insert(mid_point, value)

def popper(a_list):
    if len(a_list) <= 0:
        return
    else:
        randomizer = random.randrange(0, len(a_list))
        a_list.pop(randomizer)
        print(a_list)
        return popper(a_list)
    
def array_insert(an_array, index, value):
    new_arr = arrays.Array(len(an_array)+1)
    for i in range(index):
        new_arr[i] = an_array[i]
    new_arr[index] = value
    for i in range(index, len(an_array)):
        new_arr[i+1] = an_array[i]
    return new_arr

def array_pop(an_array, index):
    new_arr = arrays.Array(len(an_array)-1)
    for i in range(index):
        new_arr[i] = an_array[i]
    popped = new_arr[index]
    for i in range(index+1, len(an_array)):
        new_arr[i-1] = an_array[i]
    return new_arr, popped

def rgb_tuple():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)

def tuple_equality(a_tuple, b_tuple):
    print(a_tuple, b_tuple, end="\n")
    if a_tuple is b_tuple:
        print("is equality operator executed")
    if a_tuple == b_tuple:
        print("== equality operator executed")

def slices():
    quote = list("you get what you give")
    start = 0
    end = 0
    for letter in quote:
        if letter == " ":
            print(quote[start:end])
            start = end + 1
            end = start
        else:
            end += 1

def dices(a_list):
    while a_list != []:
        index = random.randrange(len(a_list))
        print(a_list[index:index+1])
        a_list = a_list[:index] + a_list[index+1:]

def comprehension():
    foobar_list = [letter for letter in "foobar"]
    print(foobar_list)
    num_list = [0 for _ in range(15)]
    print(num_list)
    int_list = [int(x) for x in range(0,13)]
    print(int_list)
    even_list = [int(x) for x in range(0, 22) if x % 2 == 0]
    print(even_list)
    div_list = [int(x) for x in range(50) if (x % 3 == 0) or (x % 5 == 0)]
    print(div_list)

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
    # var_1 = 5
    # list_1 = [2,5,6]
    # mutater(list_1, var_1)
    # print(var_1)
    # print(list_1)
    # l_1 = [1,2,3]
    # l_2 = [4,5,6]
    # print(cat(l_1,l_2)+[7,8,9])
    # l_3 = extender(l_1,l_2)
    # print(l_1, l_2, l_3, end="\n")
    # empty_arr = []
    # for i in range(5):
    #     inserter(empty_arr, i)
    #     print(empty_arr)
    # popper(empty_arr)
    # some_arr = array_utils.range_array(0,10)
    # print(array_insert(some_arr, 3, 40))
    # new_arr, popped = array_pop(some_arr, 5)
    # print(new_arr, popped)
    # print(rgb_tuple())
    # list_1 = ["abc"]
    # tup_list_1 = tuple(list_1)
    # tup_list_2 = tuple(list_1)
    # tup_list_3 = tuple([2,1,3])
    # tuple_equality(tup_list_1, tup_list_2)
    # tuple_equality(tup_list_1, tup_list_3)
    # tuple_equality(tup_list_2, tup_list_3)
    # slices()
    # dices(list("abc"))
    comprehension()




if __name__ == "__main__":
    main()