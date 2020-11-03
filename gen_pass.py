from random import randint, randrange
from pandas.io.clipboard import clipboard_set
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
        
def list_by_vals(ddata, term):
    key_list = []

    for item in ddata.items():
        if item[1] == term:
            key_list.append(item[0])
    return random.choice(key_list)


def phrase(ddata, num_words):
    words = []
    for _ in range(num_words):
        words.append(list_by_vals(ddata,random.randrange(5,10)))

    return " ".join(words)

def gen_digits(num):
    digits = ""
    for _ in range(num):
        digits += str(random.randint(0, 10))
    return digits

def generate(ddata, total_len):
    dig_length_range = []
    dig_length_min_option = 1
    dig_length_max_option = 4

    dig_length_range.append(dig_length_min_option)
    if total_len >= 18:
        dig_length_range.append(dig_length_max_option)
    dig_length_range.append(round(total_len * .25) - 2)
    dig_length_range.append(round(total_len * .25) - 1)

    rand_digits = gen_digits(random.choice(dig_length_range))
    first_rand_choice = ""
    second_rand_choice = ""

    if bool(random.getrandbits(1)):
        first_len = random.randrange(random.randint(1,2), total_len - random.randrange(6, total_len - 2))
    else:
        first_len = random.randrange(random.randint(2,3), total_len - random.randrange(7, total_len - 3))
    second_len = total_len - len(rand_digits) - 1 - first_len
    
    if args.verbose:
        print(args)
        print(f"fir len: {first_len}\tsec len: {second_len}")
        print(f"dig len: {len(rand_digits)}\tpas len: {total_len}")

    first_rand_choice = list_by_vals(ddata,  first_len)
    second_rand_choice = list_by_vals(ddata, second_len)

    if args.caps == 1:
        first_rand_choice = first_rand_choice[0].upper() + first_rand_choice[1:]

    if args.caps == 2:
        second_rand_choice = second_rand_choice[0].upper() + second_rand_choice[1:]

    specs = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\',
                                '|', '}', '{', '~', ':', ']', '+', '=', '.', ',', '`', ';','\'']
    rand_spec = random.choice(specs)

    return first_rand_choice + str(rand_digits) + rand_spec + second_rand_choice


def main():
    passw = ''
    start = time.perf_counter()

    try:
        load_time = time.perf_counter()
        data = json.load(open("/Users/mattmcmahon/Desktop/repos/password_gen/sorted.json"))
        if args.verbose:
            print(f"load time: {round(time.perf_counter() - load_time, 2)}")

        if args.passphrase:
            passw = phrase(data, args.passphrase)
        else:
            passw = generate(data, args.length)

        if args.show:
            print(f"password:\t{passw}\n")
            print(len(passw))

        if args.file:
                writer(passw, len(passw))

        if args.verbose:
            print(f"done in: {round(time.perf_counter() - start, 2)}")

        if not args.show and not args.file:
            clipboard_set(passw)
            print("password copied...\n")
            for i in range(args.time, 0, -1):
                sys.stdout.write("\r\t{:2d} secs remaining".format(i))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\r   --- done ---             \n\n")
            sys.stdout.flush()
            clipboard_set("")
        
    except Exception as e:
            print(f"\nerror in main\n{e}")
            signal.signal(signal.SIGTSTP, handler)
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generates \"foo55555!bar\" passwords (replaces deprecated option in 'keychain'). "
                                                    "Default action: copy to clipboard, no write to file or print to terminal. Passphrases optional as well (5 random words, no digits).")
    parser.add_argument("-l", "--length", type=int, default=15, choices=range(12, 33), help="Specify length of password")
    parser.add_argument("-c", "--caps", type=int, choices=(1, 2), help="Capitalize first letter or either first word or "
                                                                                "second word, word; '-c 2' will be second word's first char")
    parser.add_argument("-p", "--passphrase", type=int, help="Create a passphrase with given number of words ")
    parser.add_argument("-s", "--show", action="store_true", help="Print password to terminal")
    parser.add_argument("-f", "--file", type=str, help="File to write to (default: 'password.csv') or specify."
                                                                                "Caution: mainly used for testing, not a secure write or store")
    parser.add_argument("-t", "--time", type=int, default=20, help="Set time to keep on clipboard (countdown)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output for analysis")

    args = parser.parse_args()

    signal.signal(signal.SIGTSTP, handler)

    main()
