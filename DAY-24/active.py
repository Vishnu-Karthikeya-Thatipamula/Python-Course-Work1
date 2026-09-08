'''
import random

# =====================================================================
#  RANDOM PASSWORD GENERATOR
#  Generates a random password based on the user's NAME and DATE OF
#  BIRTH, following the password constraints used by modern
#  authentication systems.
#
#  NOTE: `random` is fine for learning. Real production systems should
#  use `secrets` (cryptographically secure randomness).
# =====================================================================

ALPHABET   = "abcdefghijklmnopqrstuvwxyz"
DIGITS     = "0123456789"
SPECIALS   = "!@#$%&*?"                  # special characters allowed
MIN_LENGTH = 8                           # NIST recommends at least 8
MAX_LENGTH = 12

# easy-to-guess sequences that modern systems reject
SEQ_AZ = ALPHABET          # abcdef...
SEQ_ZA = ALPHABET[::-1]    # zyxwvu...
SEQ_09 = DIGITS            # 012345...
SEQ_90 = DIGITS[::-1]      # 987654...


def get_user_details():
    """Read the name and date of birth from the user."""
    name = input("Enter your name: ").strip()
    dob = input("Enter your date of birth (dd-mm-yyyy): ").strip()
    return name, dob


def contains_sequence(pwd):
    """True if the password contains 3 rising/falling neighbours,
       e.g. 'abc', 'cba', '123', '321'  ->  these are banned."""
    low = pwd.lower()
    for i in range(len(low) - 2):
        triple = low[i:i + 3]
        if (triple in SEQ_AZ or triple in SEQ_ZA or
                triple in SEQ_09 or triple in SEQ_90):
            return True
    return False


def check_constraints(pwd, name, dob):
    """Return the list of broken constraints.
       An EMPTY list means the password satisfies all of them."""
    problems = []
    raw_dob = "".join(ch for ch in dob if ch.isdigit())   # e.g. 15082005

    if len(pwd) < MIN_LENGTH:
        problems.append("too short")

    if pwd == pwd.lower():
        problems.append("no UPPERCASE letter")

    if pwd == pwd.upper():
        problems.append("no lowercase letter")

    if not any(ch.isdigit() for ch in pwd):
        problems.append("no digit")

    if not any(ch in SPECIALS for ch in pwd):
        problems.append("no special character")

    for i in range(len(pwd) - 1):          # ban 'aa', '11', '%%'
        if pwd[i] == pwd[i + 1]:
            problems.append("repeating character")
            break

    if contains_sequence(pwd):             # ban 'abc' / '321' ...
        problems.append("sequence like 'abc' or '123'")

    for word in name.split():              # never embed the name
        if word.lower() in pwd.lower():
            problems.append("contains part of the name")

    if raw_dob and raw_dob in pwd:         # never embed the date of birth
        problems.append("contains the date of birth")

    return problems


def generate_password(name, dob):
    """Seed the random generator with name + DOB and keep building a
       password until every modern constraint is satisfied."""
    random.seed((name + dob).lower())      # same input -> same password

    while True:                            # retry until fully valid
        length = random.randint(MIN_LENGTH, MAX_LENGTH)
        pool = ALPHABET + ALPHABET.upper() + DIGITS + SPECIALS
        chars = random.choices(pool, k=length)

        # force at least one character from each required group
        chars[0] = random.choice(ALPHABET.upper())   # uppercase
        chars[1] = random.choice(ALPHABET)           # lowercase
        chars[2] = random.choice(DIGITS)             # digit
        chars[3] = random.choice(SPECIALS)           # special

        random.shuffle(chars)
        pwd = "".join(chars)

        if not check_constraints(pwd, name, dob):    # empty list -> valid
            return pwd


def strength_rating(pwd):
    """Simple 1..5 score, like the strength meter on websites."""
    score = 0
    if len(pwd) >= 8:
        score += 1
    if len(pwd) >= 12:
        score += 1
    if pwd != pwd.lower() and pwd != pwd.upper():
        score += 1
    if any(ch.isdigit() for ch in pwd):
        score += 1
    if any(ch in SPECIALS for ch in pwd):
        score += 1
    return max(1, score)


def main():
    print("=" * 47)
    print("  PASSWORD GENERATOR  (based on name & date of birth)")
    print("=" * 47)

    name, dob = get_user_details()

    if not any(ch.isalpha() for ch in name):
        print("\nPlease enter a valid name.")
        return
    if not any(ch.isdigit() for ch in dob):
        print("\nPlease enter a valid date of birth.")
        return

    pwd = generate_password(name, dob)
    rating = strength_rating(pwd)

    print("\nGenerated password :", pwd)
    print("Strength           :", "#" * rating + "-" * (5 - rating),
          f"({rating}/5)")

    print("\nAll modern constraints are satisfied:")
    print("- minimum length 8 characters")
    print("- upper + lower case, digit + special character")
    print("- no repeating characters, no sequences (abc / 123)")
    print("- the name and date of birth are NOT inside the password")


main()
'''

import random
name = input("Enter the name:")
DOB = input("Enter the date of birth (dd-mm-yy):")
spc = ['@','#','$','%','^','&','*','+','.',',','!']
password = name + random.choice(spc)+ DOB[-4:]
print("Generated Password:", password)