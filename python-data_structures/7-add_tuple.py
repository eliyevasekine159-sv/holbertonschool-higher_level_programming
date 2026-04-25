#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Hər iki tuple-ı ən azı 2 elementli edirik
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # İlk iki elementi toplayıb yeni tuple yaradırıq
    return (a[0] + b[0], a[1] + b[1])
