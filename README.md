# Random Password Generator

A simple command-line tool to generate secure random passwords using Python.  
Supports adjustable length, multiple password generation, and includes input validation.

---

## Features
- Generate one or more passwords
- Adjustable password length (`--length`)
- Adjustable number of passwords (`--number`)
- Input validation (no negative or zero lengths)
- Uses letters, digits, and punctuation
- Clean argparse-based command-line interface

---

## Usage

### Generate a password with the default length (12 characters)
```bash
python password_generator.py
```

### Generate a password of custom length
```bash
python password_generator.py --length 16
```

### Generate multiple passwords at once
```bash
python password_generator.py --length 20 --number 5
```

### Help menu
```bash
python password_generator.py --help
```

---

## Example Output
```
kH7!sP2@Gm#4
u1@Pk9$DqT%N
```

---

## Requirements
- Python 3.7+

---

## License
MIT License
