# Password Generator

## Recreating the passward generator from "keychain"

Output is "word + digits(5) + special character + word" 
```
  ex. foo55555!bar
  ```

Input for overall password length (minimum and maximum)
Default (no entry, just hit enter) set to 30 minimum and 31 maximum

A running tally for number of loops is displayed, along with the password itself followed by the length of the password for reference. 


## How To Use

In terminal run:
```
python3 gen_json.py
```
```
python3 gen_pass.py
```
Note: 'gen_json.py' only needs to run once unless updates to "word_list.json" are made. 


## Future Modifications

1. Argument parsing to replace the current "input"
2. Hashing: storing and checking against to make sure password isn't used more than once
3. Clean up "word_list.json," not all words (i.e. "a" and "aa") need to be in list
4. "Acceptance" or "Rejection" for password
5. Save to clipboard (goal will be time-limiting save) 

