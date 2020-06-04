from pandas.io.clipboard import clipboard_set
import random
import json
import time
import csv
import argparse

parser = argparse.ArgumentParser(description="Generates \"foo55555!bar\" passwords (replaces deprecated option in 'keychain') Default action: copy to clipboard, no write to file or print to terminal.")
group = parser.add_mutually_exclusive_group()
parser.add_argument("-l", "--length", type=int, default=15, choices=range(12,33) ,help="Specify length of password")
parser.add_argument("-s", "--show", action="store_true", help="Print password to terminal")
parser.add_argument("-w", "--write", action="store_true", help="Write to file 'password.csv'")
group.add_argument("-a", "--all", action="store_true", help="All: Clipboard, Show, and Write are used")
group.add_argument("-nc", "--noclip", action="store_true", help="Do not copy password to clipboard")
args = parser.parse_args()


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

    data = json.load(open("sorted.json"))
    
    first_rand_choice = ""
    second_rand_choice = ""
    rand_bin = random.randint(0,1)

    # TODO: unittest the following
    first_len = random.randrange(3, total_len - 6)
    second_len = total_len - 6 - first_len
    
    first_rand_choice = random.choice(list_by_vals(data, first_len))
    second_rand_choice = random.choice(list_by_vals(data, second_len))

    rand_num = random.choice(range(10000, 99999))

    specs = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(',')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':', ']', '+', '=', '.', ',', '`', ';','\'']
    rand_spec = random.choice(specs)


    return first_rand_choice + str(rand_num) + rand_spec + second_rand_choice



def main():
    
    passw = ''

    passw = generate(args.length)

    if args.all:
        writer(passw, len(passw))
        print(f"password:\t{passw}\n")
        args.noclip = False
    
    if args.noclip:
        args.show = True

    if args.write:
        writer(passw, len(passw))
        args.noclip = True

    if args.show:
        print(f"password:\t{passw}\n")
        args.noclip = True

    if not args.noclip:
        clipboard_set(passw)

        print("password saved to clipboard for next 20 seconds... \n")
        print("|--------|15|------|10|------|5|--------|")
        print("|", end="", flush=True)
        for i in range(1,40):
            if (i % 10 == 0):
                time.sleep(0.5)
                print("+", end="", flush=True)
            else:
                time.sleep(0.5)
                print("-", end="", flush=True)
        
        print("|")
        clipboard_set("")

        print()

    
if __name__ == "__main__":
    main()