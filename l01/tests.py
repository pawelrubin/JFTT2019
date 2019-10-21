#!/usr/bin/env python3
# Paweł Rubin 2019
#
"""Unit tests for pattern matching."""

import unittest

from pattern_matcher import finite_automaton_matcher, kmp_matcher
from tests_data import TEST_CASES


class TestPatternMatcher(unittest.TestCase):
    """TestCase class for DFA and KMP pattern matchers."""

    def test_dfa(self):
        """Runs DFA matcher on all test cases."""
        for test_case in TEST_CASES:
            for pattern in test_case["patterns"]:
                self.assertEqual(
                    finite_automaton_matcher(
                        text=test_case["text"],
                        pattern=pattern[0],
                        alphabet=set(test_case["alphabet"]),
                    ),
                    pattern[1],
                )

    def test_kmp(self):
        """Runs KMP matcher on all test cases."""
        for test_case in TEST_CASES:
            for pattern in test_case["patterns"]:
                self.assertEqual(
                    kmp_matcher(text=test_case["text"], pattern=pattern[0]), pattern[1]
                )


if __name__ == "__main__":
    unittest.main()
