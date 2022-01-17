
def saturation_function(x, lower_bound=0, high_bound=1):
    y = max(lower_bound, min(high_bound, x))
    return y
