from math import pow

def activation_function_single(x, r = 1):
    symbol = -1 if x < 0 else 1
    result = abs(x)

    result = pow(result, r) * symbol

    return result

def activation_function():
    pass

if __name__ == "__main__":
    cases = [
        (2, 0.5),
        (10, 0.2),
        (9, 0.5)
    ]

    for x, r in cases:
        y = activation_function_single(x, r)
        print("x={:>5.2f}, r={:>5.2f} => {:.3f}".format(x, r, y))
