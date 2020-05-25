import json

# reformats:
#        https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json
# into values containing the length of the word (possibly faster for indexing for password generation)

def generate():
    
    with open("word_list.json", "r") as json_list:
        data = json.load(json_list)

    count = 0
    max = int(input("Max: "))
    out = input("print? (y or n) ")
    total = len(data)
    for k, v in data.items():
        data[k] = len(k)
        if len(k) > max:
            if out == "y":
                print("-", k, "-", data[k])
            count = count + 1
    print(f"greater than {max - 1}: {count}")
    print(f"total remaining: {total - count}")

    # saving formated list to "word_count.json"
    with open("word_count.json", "w") as counts:
        counts.write(json.dumps(data, sort_keys=True, indent=4))
                
generate()


def group():

    with open("word_count.json", "r") as json_list:
        data = json.load(json_list)

    ones = twos = threes = fours = fives = sixes = sevens = eights = nines = tens = elevens = twelves = list()
    thirteens = fourteens = fifteens = sixteens = seventeens = eighteens = nineteens = twenties = list()

    num_list = [ones, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, elevens, twelves, thirteens, fourteens, fifteens, sixteens, seventeens, eighteens, nineteens, twenties]
    print(f"# Items: {len(num_list)}\n")

    iterate = 1

    for i in num_list:

        for k, v in data.items():

            if v <= 19:

                i.append(k)

            else:

                i.append(k)
            # if v >= 20:
                
            #     print(f"v: {v}\t k: {k}")
            #     i.append(k)

            # elif v == iterate:
                
            #     print(f"iterate: {iterate}")
            #     i.append(k)
            #     iterate = iterate + 1
                
    total = 0
    for i, el in enumerate(num_list):

        print(f"Group {i} ():      {len(el)}")
        total = total + len(el)

    print("----------------------------")
    print(f"Total:                {len(data)}")

    # print(f"Overall list: {num_list}")


group()




