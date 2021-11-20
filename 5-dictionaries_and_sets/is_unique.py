def is_unique(dict):
    values = []
    for key in dict:
        # print(key)
        if dict[key] in values:
            return False
        else:
            values.append(dict[key])
            # print(values)
    return True

dict_1 = {
    "sde": "Jerry",
    "accountant": "Gerry",
    "manager": "Horace",
    "analyst": "Joe",
}

dict_2 = {
    "analyst": "Jerry",
    "paralegal": "Gerry",
    "sde": "Horace",
    "ste": "Joe",
    "ux_designer": "Gerry"
}

print(is_unique(dict_1))
print(is_unique(dict_2))
        