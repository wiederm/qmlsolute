"""
Unit and regression test for the qmlsolute package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import qmlsolute


def test_qmlsolute_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "qmlsolute" in sys.modules
