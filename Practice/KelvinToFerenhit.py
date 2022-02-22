def k2f(Tempreture):
    assert (Tempreture>=0),"Colder than absolute zero!"
    return ((Tempreture-273)*1.8)+32


print(k2f(273))
print(int(k2f(505.78)))
print(k2f(-5))
