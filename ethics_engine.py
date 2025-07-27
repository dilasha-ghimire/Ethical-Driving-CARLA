def utilitarian_decision(data):
    if data["name"] == "car_vs_pedestrian":
        return "swerve_left"  # left is car, so swerving toward car minimizes harm
    elif data["name"] == "car_vs_car":
        return "swerve_left"  # utilitarian might pick the lower-risk car
    elif data["name"] == "pedestrian_vs_pedestrian":
        return "brake" # both pedestrians, so brake to minimize harm
    return "straight"


def deontological_decision(data):
    if data["name"] == "car_vs_pedestrian":
        return "brake"  # follow principle: do not harm human if avoidable
    elif data["name"] == "car_vs_car":
        return "brake"        # obey rule: stop before impact
    elif data["name"] == "pedestrian_vs_pedestrian":
        return "brake" # follow principle: do not harm humans
    return "straight"


def virtue_ethics_decision(data):
    if data["name"] == "car_vs_pedestrian":
        return "swerve_left"  # show moral character: protect human
    elif data["name"] == "car_vs_car":
        return "slow down"    # cautious and thoughtful response
    elif data["name"] == "pedestrian_vs_pedestrian":
        return "brake"  # act with compassion
    return "straight"
