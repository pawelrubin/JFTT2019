#!/usr/bin/env python3

from argparse import ArgumentParser


def compute_transition_function(pattern, alphabet):
    transition_function = {}
    m = len(pattern)
    for q in range(m + 1):
        for char in alphabet:
            k = min(m + 1, q + 2) - 1
            while not (pattern[:q] + char).endswith(pattern[:k]):
                k -= 1
            transition_function[(q, char)] = k
    return transition_function


def finite_automaton_matcher(text, transition_function, pattern_length):
    result = []
    q = 0
    for i in range(len(text)):
        q = transition_function[(q, text[i])]
        if q == pattern_length:
            shift = i - pattern_length + 1
            print(f"pattern occured with shift {shift}")
            result.append(shift)
    return shift


def parse_cli():
    """Parses command line arguments."""
    parser = ArgumentParser()

    parser.add_argument(
        "--alphabet",
        "-a",
        type=str,
        required=True,
        help="Alphabet for the DFA. Please type as a string",
    )

    parser.add_argument(
        "--text", "-t", type=str, required=True, help="Text for the pattern matcher."
    )

    parser.add_argument(
        "--pattern",
        "-p",
        type=str,
        required=True,
        help="Pattern for the pattern matcher.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_cli()
    transition_function = compute_transition_function(
        pattern=args.pattern, alphabet=args.alphabet
    )

    finite_automaton_matcher(
        text=args.text,
        transition_function=transition_function,
        pattern_length=len(args.pattern),
    )
