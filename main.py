def pow(v, p):
    return v**p
def PowToPow(p):
    p = pow(p, p)
    p = PowToPow(p)
    if p > 10000000000000000:
        return p
print(PowToPow(2))
