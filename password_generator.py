#!/usr/bin/env python3
"""
Random Password Generator

This script generates one or more random passwords using letters,
digits, and punctuation characters. It uses argparse to allow users
to control password length and the number of passwords.
"""

import argparse
import random
import string
from typing import Sequence

# Default set of allowed characters
CHARSET = string.ascii_letters + string.digits + string.punctuation


def generate_password(length: int, charset: Sequence[str] = CHARSET) -> str:
    """
    Generate a random password.

    Args:
        length: Length of the password. Must be a positive integer.
        charset: Characters to choose from.

    Returns:
        A string containing the generated password.

    Raises:
        ValueError: If length is not a positive integer.
    """
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")

    return "".join(random.choice(charset) for _ in range(length))


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate one or more random passwords."
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=12,
        help="Password length (default: 12).",
    )

    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of passwords to generate (default: 1).",
    )

    return parser.parse_args()


def main() -> None:
    """Main entry point of the program."""
    args = parse_args()

    # Basic checks
    if args.length <= 0:
        print("Error: password length must be greater than zero.")
        return

    if args.number <= 0:
        print("Error: number of passwords must be greater than zero.")
        return

    # Generate passwords
    for _ in range(args.number):
        password = generate_password(args.length)
        print(password)


if __name__ == "__main__":
    main()
