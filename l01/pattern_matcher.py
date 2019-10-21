#!/usr/bin/env python3
# Paweł Rubin 2019
#
"""Pattern matching with finite automata and Knuth-Morris-Pratt algorithm."""

from argparse import ArgumentParser


class PatternAlphabetMismatchError(Exception):
    """Error raised when pattern contains characters from outside of the alphabet."""


def compute_transition_function(pattern, alphabet):
    """Computes the transition function from a given pattern."""
    if not set(pattern).issubset(alphabet):
        raise PatternAlphabetMismatchError(
            "Pattern contains characters from outside of the alphabet."
        )
    transition_function = {}
    m = len(pattern)
    for q in range(m + 1):
        for char in alphabet:
            k = min(m + 1, q + 2) - 1
            while not (pattern[:q] + char).endswith(pattern[:k]):
                k -= 1
            transition_function[(q, char)] = k
    return transition_function


def finite_automaton_matcher(text, pattern, alphabet):
    """Finite automaton matcher. Returns list of shifts of pattern occurences."""
    transition_function = compute_transition_function(pattern, alphabet)
    result = []
    q = 0
    pattern_length = len(pattern)
    for i, t in enumerate(text):
        q = transition_function[(q, t)]
        if q == pattern_length:
            shift = i - pattern_length + 1
            result.append(shift)
    return result


def compute_prefix_function(pattern):
    """Computes the prefix function from a given pattern."""
    m = len(pattern)
    pi = {}
    pi[0] = -1
    k = -1
    for q in range(1, m):
        while k > -1 and pattern[k + 1] != pattern[q]:
            k = pi[k]
        if pattern[k + 1] == pattern[q]:
            k += 1
        pi[q] = k
    return pi


def kmp_matcher(text, pattern):
    """Knuth-Morris-Pratt matcher. Returns list of shifts of pattern occurences."""
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    result = []
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1] + 1
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            shift = i - m + 1
            result.append(shift)
            q = pi[q - 1] + 1
    return result


def parse_cli():
    """Parses command line arguments."""
    parser = ArgumentParser()

    parser.add_argument(
        "--alphabet",
        "-a",
        type=str,
        help="Alphabet for the DFA Matcher. If not specified, KMP Matcher will be used.",
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
    if args.alphabet is not None:
        print("Finite Automaton Matcher.")
        print(
            finite_automaton_matcher(
                text=args.text, pattern=args.pattern, alphabet=set(args.alphabet)
            )
        )
    else:
        print("Knuth-Morris-Pratt Matcher.")
        print(kmp_matcher(text=args.text, pattern=args.pattern))
