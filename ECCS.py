"""
Fault Tree Analysis of an Emergency Core Cooling System (ECCS) in a PWR.

Scenario:
- 2 redundant injection pumps (A and B)
- 1 diesel generator (backup power)
- System fails if BOTH pumps fail OR diesel fails when needed.

Data (illustrative, from public reliability databases):
- Pump failure probability: 0.01 per demand
- Diesel failure probability: 0.005 per demand
"""

# Probabilities (per demand)
P_pump_fail = 0.01
P_diesel_fail = 0.005

# Fault Tree Logic
# Top Event: ECCS fails
# OR gate: (Pump A fails AND Pump B fails) OR (Diesel fails)

# Probability that both pumps fail (AND gate)
P_both_pumps_fail = P_pump_fail * P_pump_fail

# Probability of top event (OR gate)
P_eccs_fail = P_both_pumps_fail + P_diesel_fail - (P_both_pumps_fail * P_diesel_fail)

# Results
print("=" * 50)
print("FAULT TREE ANALYSIS - ECCS")
print("=" * 50)
print(f"Pump failure probability (each): {P_pump_fail}")
print(f"Diesel failure probability:      {P_diesel_fail}")
print("-" * 50)
print(f"P(both pumps fail):              {P_both_pumps_fail:.6f}")
print(f"P(ECCS fails):                   {P_eccs_fail:.6f}")
print("=" * 50)