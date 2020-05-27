import threading
import random
import json
import time
import csv
import sys
import os

NUM_THREADS = 10
NUM_RUNS_PER_THREAD = 100

def writer(password, length):

    with open('test.csv', 'a', newline='') as f:
        fieldnames = ['password', 'length']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)

        # thewriter.writeheader()
        thewriter.writerow({'password' : password, 'length' : length})


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

def main():

    threads = []

    start = time.perf_counter()
    for num in range(NUM_THREADS):
        t = threading.Thread(target=run, args=(num,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    
    stop = time.perf_counter()

    print("done in:  {}".format(round(stop - start, 2)))
    print("threads:  {}\nruns per: {}".format(NUM_THREADS, NUM_RUNS_PER_THREAD))
    
def run(num):

    # print(f'thread {num}')

    for i in range(NUM_RUNS_PER_THREAD):
        password = generate()
        writer(password, len(password))

    # print(f"ending thread {num}")

if __name__ == "__main__":
    main()