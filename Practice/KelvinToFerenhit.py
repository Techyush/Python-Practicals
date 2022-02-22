def k2f(temperature):
    assert (temperature >= 0), "Colder than absolute zero!"
    return ((temperature-273)*1.8)+32


print(k2f(273))
print(int(k2f(505.78)))
print(k2f(-5))
