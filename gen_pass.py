from pandas.io.clipboard import clipboard_set
from io import StringIO
import concurrent.futures
import random
import json
import time
import csv
import argparse
import signal
import sys

def handler(x, frame):
    clipboard_set("")
    print()
    sys.exit(0)

def writer(passw, length):
    with open(args.file, 'a', newline='') as f:
        fieldnames = ['password', 'length']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)

        thewriter.writerow({'password': passw, 'length': length})
        
def list_by_vals(total_dict, term):
    key_list = []
    items = total_dict.items()
    for item in items:
        if item[1] == term:
            key_list.append(item[0])
    return random.choice(key_list)


def generate(total_len):
    load_time = time.perf_counter()        
    data = json.load(open("sorted.json"))

    if args.verbose:
        print(f"load time: {round(time.perf_counter() - load_time, 2)}")

    first_rand_choice = ""
    second_rand_choice = ""
    rand_bool = bool(random.getrandbits(1))

    rand_true_range = random.randrange(6, total_len - 2)
    rand_false_range = random.randrange(7, total_len - 3)

    if rand_bool:
        first_len = random.randrange(random.randint(1,2), total_len - rand_true_range)
    else:
        first_len = random.randrange(random.randint(2,3), total_len - rand_false_range)
    second_len = total_len - 6 - first_len
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        first_rand_choice = executor.submit(list_by_vals, data, first_len)
        second_rand_choice = executor.submit(list_by_vals, data, second_len)

    first_rand_choice = first_rand_choice.result()

    if args.caps == 1:
        first_rand_choice = first_rand_choice[0].upper() + first_rand_choice[1:]

    second_rand_choice = second_rand_choice.result()

    if args.caps == 2:
        second_rand_choice = second_rand_choice[0].upper() + second_rand_choice[1:]

    rand_num = random.choice(range(10000, 99999))

    specs = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\',
                                '|', '}', '{', '~', ':', ']', '+', '=', '.', ',', '`', ';','\'']
    rand_spec = random.choice(specs)

    return first_rand_choice + str(rand_num) + rand_spec + second_rand_choice


def main():

    passw = ''
    start = time.perf_counter()

    try:
        passw = generate(args.length)

        if args.verbose:
            print(f"done in: {round(time.perf_counter() - start, 2)}")

        if args.show:
            print(f"password:\t{passw}\n")

        if args.file:
                writer(passw, len(passw))
        
        if not args.show and not args.file:
            clipboard_set(passw)

            for i in range(args.time, 0, -1):
                sys.stdout.write("\r{:2d} secs remaining".format(i))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\r   --- done ---  \n")
            sys.stdout.flush()
            clipboard_set("")

    except:
            print("\nerror in main\n")
            signal.signal(signal.SIGTSTP, handler)
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generates \"foo55555!bar\" passwords (replaces deprecated option in 'keychain') "
                                                    "Default action: copy to clipboard, no write to file or print to terminal.")
    parser.add_argument("-l", "--length", type=int, default=15, choices=range(12, 33), help="Specify length of password")
    parser.add_argument("-c", "--caps", type=int, choices=(1, 2), help="Capitalize first letter or either first word or "
                                                                                            "second word, word; '-c 2' will be second word's first char")
    parser.add_argument("-s", "--show", action="store_true", help="Print password to terminal")
    parser.add_argument("-f", "--file", type=str, help="File to write to (default: 'password.csv') or specify."
                                                                                "Caution: mainly used for testing, not a secure write or store")
    parser.add_argument("-t", "--time", type=int, default=20, help="Set time to keep on clipboard (countdown)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output for analysis")

    args = parser.parse_args()

    signal.signal(signal.SIGTSTP, handler)

    print(args)

    main()