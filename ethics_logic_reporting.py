def utilitarian_decision(scenario):
    if scenario["name"] == "car_vs_car":
        return "swerve"
    return "brake"

def deontological_decision(scenario):
    return "brake"

def virtue_ethics_decision(scenario):
    if scenario["name"] in ["car_vs_car", "pedestrian_vs_pedestrian"]:
        return "slow down"
    return "brake"
