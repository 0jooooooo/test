#!/usr/bin/env python3
"""A simple command-line calculator."""

import argparse


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(a: float, b: float) -> float:
    return a ** b


OPERATIONS = {
    "add": add,
    "sub": subtract,
    "mul": multiply,
    "div": divide,
    "pow": power,
}


def calculate(operation: str, a: float, b: float) -> float:
    if operation not in OPERATIONS:
        raise ValueError(f"unknown operation: {operation}")
    return OPERATIONS[operation](a, b)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple CLI calculator")
    parser.add_argument("operation", choices=OPERATIONS.keys(), help="operation to perform")
    parser.add_argument("a", type=float, help="first operand")
    parser.add_argument("b", type=float, help="second operand")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        result = calculate(args.operation, args.a, args.b)
    except ZeroDivisionError as exc:
        parser.error(str(exc))
        return

    print(result)


if __name__ == "__main__":
    main()
