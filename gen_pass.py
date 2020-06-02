from pandas.io.clipboard import clipboard_set
import random
import json
import time
import math
import csv
import sys


total = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


def writer(passw, length):

    with open('random.csv', 'a', newline='') as f:
        fieldnames = ['password', 'length']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)

        thewriter.writerow({'password' : passw, 'length' : length})


def generate(total_len):

    with open("sorted.json") as json_file:
        data = json.load(json_file)
    
    avg_choices = (total_len - 6) / 2

    rand_bin = random.randint(0,1)

    for i in range(29):
        for k, v in data.items():
            if (v == i):
                total[i].append(k)
    
    if ((total_len % 2) == 1):
        # print("avg: {}\tbin: {}\n1st: {}\t\t2nd: {}".format(avg_choices, rand_bin,
        #                                                 math.ceil(avg_choices), math.floor(avg_choices)))
        if (rand_bin == 0):
            first_rand_choice = random.choice(total[math.ceil(avg_choices)])
            second_rand_choice = random.choice(total[math.floor(avg_choices)])
        else:
            first_rand_choice = random.choice(total[math.floor(avg_choices)])
            second_rand_choice = random.choice(total[math.ceil(avg_choices)])

    rand_num = random.choice(range(10000, 99999))

    specs = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(',')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':', ']', '+', '=', '.', ',', '`', ';','\'']
    rand_spec = random.choice(specs)

    #combine
    password = first_rand_choice + str(rand_num) + rand_spec + second_rand_choice

    return password


def main():

    if (len(sys.argv) <= 1):
        pass_len = 15
        print("default password length set: 15")
    else:
        pass_len = int(sys.argv[1])
    

    start = time.perf_counter()
    
    passw = ''

    passw = generate(pass_len)

    writer(passw, len(passw))
    
    clipboard_set(passw)

    print("\npassword: {}\t len: {}".format(passw, len(passw)))
    stop = time.perf_counter()
    print("\ndone in: {}".format(round(stop - start, 2)))

    print("password saved to clipboard for next 20 seconds... \n")
    time.sleep(20)
    clipboard_set("")

    
if __name__ == "__main__":
    main()