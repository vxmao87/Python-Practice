def is_1_to_1(dict):
    phone_numbers = set()
    for name in dict:
        if dict[name] in phone_numbers:
            return False
        else:
            phone_numbers.add(dict[name])
    return True

dict_1 = {
    "Marty" : "206-9024",
    "Hawking" : "123-4567",
    "Smith" : "949-0504",
    "Newton" : "123-4567",
}

dict_2 = {
    "Marty" : "206-9024",
    "Hawking" : "555-1234",
    "Smith" : "949-0504",
    "Newton" : "123-4567",
}

print(is_1_to_1(dict_1))
print(is_1_to_1(dict_2))