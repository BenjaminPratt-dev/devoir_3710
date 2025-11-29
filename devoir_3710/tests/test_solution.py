#!/usr/bin/env python3
"""
Simple tests for the solution.

Run with: uv run python tests/test_solution.py
"""

import sys
import os

# Add parent directory to path to import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solution import add, multiply, process_data


def assert_equal(actual, expected, message=""):
    """Helper function to assert equality."""
    if actual != expected:
        raise AssertionError(
            f"{message}\n  Expected: {expected}\n  Got: {actual}"
        )
    print(f"  ✓ {message if message else 'Test passed'}")


def test_add():
    """Test the add function."""
    print("\nTesting add()...")
    assert_equal(add(2, 3), 5, "2 + 3 should equal 5")
    assert_equal(add(0, 0), 0, "0 + 0 should equal 0")
    assert_equal(add(-1, 1), 0, "-1 + 1 should equal 0")
    assert_equal(add(100, 200), 300, "100 + 200 should equal 300")


def test_multiply():
    """Test the multiply function."""
    print("\nTesting multiply()...")
    assert_equal(multiply(2, 3), 6, "2 * 3 should equal 6")
    assert_equal(multiply(0, 5), 0, "0 * 5 should equal 0")
    assert_equal(multiply(1, 10), 10, "1 * 10 should equal 10")
    assert_equal(multiply(-2, 3), -6, "-2 * 3 should equal -6")


def test_process_data():
    """Test the process_data function."""
    print("\nTesting process_data()...")
    assert_equal(process_data([1, 2, 3]), 6, "sum of [1,2,3] should be 6")
    assert_equal(process_data([]), 0, "sum of [] should be 0")
    assert_equal(process_data([10]), 10, "sum of [10] should be 10")
    assert_equal(process_data([5, 5, 5]), 15, "sum of [5,5,5] should be 15")


def run_all_tests():
    """Run all test functions."""
    print("=" * 60)
    print("Running Tests")
    print("=" * 60)
    
    try:
        test_add()
        test_multiply()
        test_process_data()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        return True
        
    except AssertionError as e:
        print("\n" + "=" * 60)
        print(f"❌ TEST FAILED:\n{e}")
        print("=" * 60)
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
