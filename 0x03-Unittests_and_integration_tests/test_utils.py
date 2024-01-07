#!/usr/bin/env python3
"""test_util module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any, Dict, Callable


class TestAccessNestedMap (unittest.TestCase):
    """test class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence,
            expected_result
            ) -> Any:
        """testing parameters"""

        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()