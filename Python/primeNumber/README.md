# Prime Number Checker

## Purpose

Check whether a given number is prime.

## What it teaches

- valid numeric input handling
- looping with a `for` range
- using the modulus operator to test for divisibility
- `else` on loops for prime detection

## How it works

1. The script reads an integer from the user.
2. If the number is greater than 1, it checks divisibility from 2 to `num - 1`.
3. If any divisor is found, it prints that the number is not prime.
4. If none are found, it prints that the number is prime.

## Run

```bash
python3 primeNumber.py
```

## Example

```text
Enter a number to check if it's prime: 13
13 is a prime number
```
