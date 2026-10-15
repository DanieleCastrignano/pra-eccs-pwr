"""
Fault Tree Analysis of an Emergency Core Cooling System (ECCS) in a PWR.

Scenario:
- 2 redundant injection pumps (A and B)
- 1 diesel generator (backup power)
- System fails if BOTH pumps fail OR diesel fails when needed.

Author: Daniele Castrignano
Date: 2026
"""

# ============================================================
# INPUT VALIDATION
# ============================================================
def get_probability(prompt: str) -> float:
    """
    Ask the user for a probability value and validate it.

    Args:
        prompt: the message shown to the user
    Returns:
        A float between 0 and 1
    """
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 1:
                return value
            else:
                print("  ⚠️  The value must be between 0 and 1. Try again.")
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a number (e.g. 0.01).")


# ============================================================
# FAULT TREE LOGIC
# ============================================================
def probability_both_pumps_fail(p_pump: float) -> float:
    """
    AND gate: both redundant pumps must fail.
    """
    return p_pump ** 2


def probability_eccs_fail(p_pump: float, p_diesel: float) -> float:
    """
    OR gate: ECCS fails if both pumps fail OR diesel fails.

    Inclusion-exclusion principle:
        P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
    """
    p_both_pumps = probability_both_pumps_fail(p_pump)
    return p_both_pumps + p_diesel - (p_both_pumps * p_diesel)


# ============================================================
# MAIN
# ============================================================
def main():
    print("=" * 55)
    print("   ECCS FAULT TREE ANALYSIS - Interactive Tool")
    print("=" * 55)
    print("Enter the failure probabilities (values between 0 and 1).")
    print("Example: 0.01 for 1% failure probability.\n")

    # Ask the user for inputs
    p_pump = get_probability("→ Single pump failure probability:   ")
    p_diesel = get_probability("→ Diesel generator failure prob.:    ")

    # Compute results
    p_both_pumps = probability_both_pumps_fail(p_pump)
    p_eccs = probability_eccs_fail(p_pump, p_diesel)

    # Display results
    print("\n" + "=" * 55)
    print("   RESULTS")
    print("=" * 55)
    print(f"  Single pump failure:        {p_pump:.6f}")
    print(f"  Diesel failure:             {p_diesel:.6f}")
    print(f"  Both pumps failure:         {p_both_pumps:.6f}")
    print(f"  → ECCS failure probability: {p_eccs:.6f}")
    print("=" * 55)


if __name__ == "__main__":
    main()