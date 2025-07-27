from ethics_logic_reporting import utilitarian_decision, deontological_decision, virtue_ethics_decision
import csv
import os

# Define test scenarios
scenarios = [
    {"name": "car_vs_pedestrian", "left_risk": 10, "right_risk": 3, "left_is_child": False},
    {"name": "car_vs_car", "left_risk": 7, "right_risk": 6, "left_is_child": False},
    {"name": "pedestrian_vs_pedestrian", "left_risk": 6, "right_risk": 4, "left_is_child": True}
]

# Map modes to logic functions
ethics = {
    "utilitarian": utilitarian_decision,
    "deontological": deontological_decision,
    "virtue": virtue_ethics_decision
}

# Make sure result folder exists
os.makedirs("results", exist_ok=True)

# Create results log
with open("results/ethical_decision_log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["scenario", "mode", "decision"])
    for scenario in scenarios:
        for mode_name, mode_func in ethics.items():
            decision = mode_func(scenario)
            writer.writerow([scenario["name"], mode_name, decision])
            print(f"{scenario['name']} | {mode_name} => {decision}")
