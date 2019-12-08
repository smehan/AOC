"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:
For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.

second part:

for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount
you just calculated as the input mass and repeat the process, continuing until a fuel requirement
is zero or negative.
"""


def module_mass(m: int):
    res = m//3 - 2
    return res


def module_mass_2(m: int):
    res = m//3 - 2
    if res <= 0:
        return 0
    else:
        return res + module_mass_2(res)


def process(fname, rec=False):
    res = 0
    with open(fname) as fh:
        if not rec:
            res = sum(module_mass(int(l)) for l in fh.readlines())
        else:
            res = sum(module_mass_2(int(l)) for l in fh.readlines())
    return res


if __name__ == "__main__":
    assert module_mass(12) == 2
    assert module_mass(14) == 2
    assert module_mass(1969) == 654
    assert module_mass(100756) == 33583
    print(process("d1.txt"))
    assert module_mass_2(12) == 2
    assert module_mass_2(14) == 2
    assert module_mass_2(1969) == 966
    assert module_mass_2(100756) == 50346
    print(process("d1.txt", rec=True))