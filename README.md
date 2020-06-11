# Password Generator

Generates "foo55555!bar" passwords (replaces deprecated option in 'keychain')
<br>Default action: copy to clipboard, no write to file or print to terminal.

## How To Use

```
usage: gen_pass.py [-h]
                   [-l {12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32}]
                   [-c {1,2}] [-s] [-f FILE] [-t TIME] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -l {12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32}, --length {12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32}
                        Specify length of password
  -c {1,2}, --caps {1,2}
                        Capitalize first letter or either first word or second
                        word, word; '-c 2' will be second word's first char
  -s, --show            Print password to terminal
  -f FILE, --file FILE  File to write to (default: 'password.csv') or
                        specify.Caution: mainly used for testing, not a secure
                        write or store
  -t TIME, --time TIME  Set time to keep on clipboard (countdown)
  -v, --verbose         Verbose output for analysis
```

## Future Modifications

1. ~~Argument parsing to replace the current "input"~~
2. ~~Save to clipboard (time-limited)~~
3. Compliance with specified framework (i.e NIST)
4. ~Argparsing: print to screen, save to file, capitalization (first or second word), time on clipboard~
5. ~Number of digits determined by overall length of password (i.e. 12 char password has between 1 and 3 digits)~
6. Allow for leading zeros in digits
7. More than 2 words, dependent on length (e.g. length = 25, 3 words totaling to max of 23 letters, then one number and one spec)
9. ~Passphrases! (Defualt 4 words ~23-39 characters incl. spaces long)~