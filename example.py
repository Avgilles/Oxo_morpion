#!/usr/bin/env python
# coding: utf-8

if __name__ == "__main__":
    list_var = [ 0, 1, 2, 3, 0]
    tuple_var = ( 0, 1, 2, 3, 0)
    set_var = { *list_var }

    print(f"list_var = {list_var}")
    print(f"tuple_var = {tuple_var}")
    print(f"set_var = {set_var}")
    list_var[0] = 12
    # tuple_var[0] = 12
    # set_var[0] = 12

    dict1 = {
        "key1": 1,
        "key2": 2,
    }

    dict2 = {
        "key3": 3,
        "key4": 4
    }

    dict3 = {**dict1, **dict2}

    print(f"dict3 = {dict3}")