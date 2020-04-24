from textwrap import dedent
import math

input_list1 = [2,4,6,8]
new_input_element1 = 5
input_list2 = [4,8,15,23,42]
new_input_element2 = 16

def get_length(input_list):
    list_counter=0
    for items in input_list: 
        list_counter = list_counter +1
    return list_counter


def custom_print(print_input, item, listNumber):
    if listNumber != "NONE":
        print(dedent(f"""
        ====================================================================
                            {listNumber}
        ====================================================================
        """))
    print(dedent(f"""
    *******************************
    {item} : {print_input}
    *******************************
    """))

def insert_shift_list(source_list, new_element, size):
    middle_index = math.ceil(size / 2)
    target_list = [None] * (size + 1)
    for idx, val in enumerate(source_list):
        new_idx = idx
        if idx == middle_index:
            target_list[new_idx] = new_element
            new_idx = new_idx + 1
            target_list[new_idx] = source_list[idx]      
            middle_index = 0
        else:
            if idx > middle_index:
                new_idx = new_idx + 1
            target_list[new_idx] = source_list[idx]
    return target_list


if __name__ == '__main__':
    list1_size = get_length(input_list1)
    print(f"list1_size: {list1_size}")
    custom_print(input_list1,"Original List 1", "Shift List 1")
    custom_print(list1_size,"List 1 Size", "NONE")
    custom_print(new_input_element1,"Element to be inserted", "NONE")
    custom_print(insert_shift_list(input_list1, new_input_element1, list1_size), "Shifted List 1", "NONE")


    list2_size = get_length(input_list2)
    print(f"list2_size: {list2_size}")
    custom_print(input_list2,"Original List 2", "Shift List 2")
    custom_print(list2_size,"List 2 Size", "NONE")
    custom_print(new_input_element2,"Element to be inserted", "NONE")
    custom_print(insert_shift_list(input_list2, new_input_element2, list2_size), "Shifted List 2", "NONE")