# Password Generator

## Recreating the passward generator from "keychain"

Output is "word + digits(5) + special character + word" 
  ```
  ex. foo55555!bar
  ```

## How To Use

In terminal run:
```
python3 gen_pass.py {password length}
```
<dl>
  <dt>Note </dt>
  <dd>If no argument {password length} provided, default set to 15</dd>
  <dd>Password saved to clipboard for 20 seconds</dd>
</dl>

## Future Modifications

1. ~~Argument parsing to replace the current "input"~~
2. Hashing: storing and checking against to make sure password isn't used more than once
3. ~~Clean up "word_list.json," not all words (i.e. "a" and "aa") need to be in list~~
4. ~~Save to clipboard (goal will be time-limiting save)~~
5. Compliance with specified framework (i.e NIST)
6. ~Argparsing: print to screen, save to file, capitalization (first or second word)~
7. Number of digits determined by overall length of password (i.e. 12 char password has between 3 and 5 digits)
8. Allow for leading zeros in digits