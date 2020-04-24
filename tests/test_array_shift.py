from array_shift import __version__
from array_shift.array_shift import get_length
from array_shift.array_shift import insert_shift_list

def test_version():
    assert __version__ == '0.1.0'

def test_get_length0():
    source_list1 = []
    expected = 0
    actual = get_length(source_list1)
    assert expected == actual

def test_get_length1():
    source_list1 = [2,4,6,8]
    expected = 4
    actual = get_length(source_list1)
    assert expected == actual

def test_get_length2():
    source_list2 = [4,8,15,23,42]
    expected = 5
    actual = get_length(source_list2)
    assert expected == actual

def test_insert_shift_list1():
    source_list1 = [2,4,6,8]
    new_input_element1 = 5
    size = 4
    expected = [2,4,5,6,8]
    actual = insert_shift_list(source_list1, new_input_element1, size)
    assert expected == actual

def test_insert_shift_list2():
    source_list2 = [4,8,15,23,42]
    new_input_element2 = 16
    size = 5
    expected =  [4,8,15,16,23,42]
    actual = insert_shift_list(source_list2, new_input_element2, size)
    assert expected == actual

def test_insert_shift_list_length1():
    source_list1 = [2,4,6,8]
    new_input_element1 = 16
    size = 4
    expected =  5
    actual = get_length(insert_shift_list(source_list1, new_input_element1, size))
    assert expected == actual

def test_insert_shift_list_length2():
    source_list2 = [4,8,15,23,42]
    new_input_element2 = 16
    size = 5
    expected =  6
    actual = get_length(insert_shift_list(source_list2, new_input_element2, size))
    assert expected == actual