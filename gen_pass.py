import random
import json

def generate():

    with open("word_list.json") as json_file:
        data = json.load(json_file)

    first_rand_choice = random.choice(list(data.keys()))

    rand_num = random.choice(range(10000,99999))
    # print(rand_num)

    second_rand_choice = random.choice(list(data.keys()))
    if second_rand_choice == first_rand_choice:
        second_rand_choice = random.choice(list(data.keys()))

    # print(second_rand_choice)

    #spec
    specs = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':', ']','+','=','.',',']
    rand_spec = random.choice(specs)

    #combine
    password = first_rand_choice + str(rand_num) + rand_spec + second_rand_choice
    # print(password)

    return password

passw = ''
runs = 0

min = raw_input("Enter min: ")
max = raw_input("Enter max: ")

if min == "":
    min = 30
if max == "":
    max = 31

while True:
    runs += 1
    print(runs)
    passw = generate()
    if (min <= len(passw) <= max):
        break

print(passw)
print('length: {}'.format(len(passw)))
