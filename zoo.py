zoo = ("monkey", "zebra", "giraffe", "penguin", "lion", "tiger", "bear", "cougar", "lynx", "donkey")
print(zoo.index("penguin"))
animal_to_find = "penguin"
if animal_to_find in zoo:
    print(f'{animal_to_find} was found!')

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(ninth_animal)
print(tenth_animal)

zoo_list = list(zoo)

print(type(zoo_list))
print(zoo_list)

zoo_list.extend(["bat", "chimp", "sloth"])
zoo = tuple(zoo_list)

print(type(zoo))
print(zoo)