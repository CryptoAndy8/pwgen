#!/usr/bin/env python3
import argparse, secrets, string, sys

ALPHABET = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digits": string.digits,
    "symbols": "!@#$%^&*()-_=+[]{};:,.?/\\",
}

def gen(n: int, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    pools = [ALPHABET["lower"]]
    if use_upper: pools.append(ALPHABET["upper"])
    if use_digits: pools.append(ALPHABET["digits"])
    if use_symbols: pools.append(ALPHABET["symbols"])
    alphabet = "".join(pools)
    if n < len(pools):
        raise ValueError("length is too small for selected sets")
    # guarantee at least one char from each selected pool
    pwd = [secrets.choice(pool) for pool in pools]
    pwd += [secrets.choice(alphabet) for _ in range(n - len(pools))]
    # shuffle without random module
    for i in range(len(pwd) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        pwd[i], pwd[j] = pwd[j], pwd[i]
    return "".join(pwd)

def main(argv=None):
    p = argparse.ArgumentParser(description="Simple secure password generator")
    p.add_argument("-n", "--length", type=int, default=16)
    p.add_argument("--no-upper", action="store_true", help="disable uppercase")
    p.add_argument("--no-digits", action="store_true", help="disable digits")
    p.add_argument("--no-symbols", action="store_true", help="disable symbols")
    args = p.parse_args(argv)
    try:
        print(gen(
            n=args.length,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        ))
    except ValueError as e:
        sys.exit(f"error: {e}")

if __name__ == "__main__":
    main()
