#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < my_list[0]:
        return None
    if idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]
