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

        thewriter.writerow({'password': passw, 'length': length})
        
def list_by_vals(total_dict, term):
    key_list = []
    items = total_dict.items()
    for item in items:
        if item[1] == term:
            key_list.append(item[0])
    return key_list


def generate(total_len):

    # with open("sorted.json") as json_file:
    data = json.load(open("sorted.json"))
    
    # avg_choices = (total_len - 6) / 2
    first_rand_choice = ""
    second_rand_choice = ""
    rand_bin = random.randint(0,1)

    sort_time = time.perf_counter()

    # TODO: unittest the following
    first_len = random.randrange(3, total_len - 6)
    second_len = total_len - 6 - first_len
    
    find_time = time.perf_counter()
    first_rand_choice = random.choice(list_by_vals(data, first_len))
    second_rand_choice = random.choice(list_by_vals(data, second_len))
    # print(f"found in: {round(time.perf_counter()-find_time,2)}")

    # print(f"total: {total_len}\tcorrect: {(len(first_rand_choice) + len(second_rand_choice) + 6) == total_len}")

    # print(f"1st: {first_rand_choice}\t1st len: {len(first_rand_choice)}\tcheck: {len(first_rand_choice) == first_len}")
    # print(f"2nd: {second_rand_choice}\t2nd len: {len(second_rand_choice)}\tcheck: {len(second_rand_choice) == second_len}")

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

    # writer(passw, len(passw))
    
    clipboard_set(passw)

    # print("\npassword: {}\t len: {}".format(passw, len(passw)))
    stop = time.perf_counter()
    # print("\ndone in: {}".format(round(stop - start, 2)))

    print("password saved to clipboard for next 20 seconds... \n")
    time.sleep(20)
    clipboard_set("")

    
if __name__ == "__main__":
    main()