def l100kmtompg(liters):
    inmile = 100 * 1000 / 1609.344
    ingallon = liters / 3.785411784
    return inmile / ingallon

def mpgtol100km(miles):
    inkm = miles * 1609.344 / 1000
    inliter = 3.785411784
    return 100 / inkm * inliter

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
