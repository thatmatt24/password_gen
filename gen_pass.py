import random
import json
import sys
import os
import time
import csv

NUM_RUNS = 1000

def writer(two, three):

    # print(one, two, three)

    with open('random.csv', 'a', newline='') as f:
        fieldnames = ['password', 'length']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)

        # thewriter.writeheader()
        thewriter.writerow({'password' : two, 'length' : three})



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
    specs = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':', ']', '+', '=', '.', ',', '`', ';','\'']
    rand_spec = random.choice(specs)

    #combine
    password = first_rand_choice + str(rand_num) + rand_spec + second_rand_choice
    # print(password)

    return password


# def checker(min=15,max=21):
def checker():

    passw = ''
    runs = 0

    while True:

        passw = generate()
        # print("{}, {}".format(passw, len(passw)))
        writer(passw, len(passw))
        runs += 1
        if (runs == NUM_RUNS): break


def main():

    # checker(sys.argv[1], sys.argv[2])
    start = time.perf_counter()

    checker()
        # os.system("python3 gen_pass.py {} {}".format(sys.argv[1], sys.argv[2]))
    stop = time.perf_counter()

    print("done in:", round(stop - start, 2))
    print("threads: {}\nruns per: {}".format(0, NUM_RUNS))

    
if __name__ == "__main__":
    main()