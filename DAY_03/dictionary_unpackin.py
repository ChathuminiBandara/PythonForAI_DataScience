person = {
    "name": "Ian",
    "Age": 27,
}

# ------------- 1st way ----------
# {name, Age} = person

# print(name, Age)

# ------------- 2nd way ----------

for key, value in person.items():
    print(key, value)

# ------------- only keys ----------
for key in person.items():
    print(key)

# ------------- only values ----------
for value in person.values():
    print(value)