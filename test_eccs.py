"""
Unit tests for the ECCS fault tree analysis module.
Run with: pytest test_eccs.py -v
"""

import pytest
from ECCS import probability_both_pumps_fail, probability_eccs_fail


# ============================================================
# TEST: AND gate (both pumps fail)
# ============================================================
def test_both_pumps_fail_basic():
    """Both pumps fail probability should be p^2."""
    assert probability_both_pumps_fail(0.01) == pytest.approx(0.0001)


def test_both_pumps_fail_zero():
    """If pump failure is 0, both fail is 0."""
    assert probability_both_pumps_fail(0.0) == 0.0


def test_both_pumps_fail_certain():
    """If pump failure is 1, both fail is 1."""
    assert probability_both_pumps_fail(1.0) == 1.0


# ============================================================
# TEST: OR gate (ECCS failure)
# ============================================================
def test_eccs_fail_basic():
    """ECCS failure probability with standard values."""
    result = probability_eccs_fail(0.01, 0.005)
    assert result == pytest.approx(0.0051, abs=1e-6)


def test_eccs_fail_zero():
    """If all failures are 0, ECCS failure is 0."""
    assert probability_eccs_fail(0.0, 0.0) == 0.0


def test_eccs_fail_diesel_only():
    """If pumps never fail, ECCS failure equals diesel failure."""
    result = probability_eccs_fail(0.0, 0.005)
    assert result == pytest.approx(0.005)


def test_eccs_fail_monotonic():
    """Increasing pump failure should increase ECCS failure."""
    low = probability_eccs_fail(0.01, 0.005)
    high = probability_eccs_fail(0.05, 0.005)
    assert high > low