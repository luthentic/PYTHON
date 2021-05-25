from space.planet import Planet
from space.calc import planet_mass,planet_vol

hoth = Planet('LEE',20000,5.6,'HOHOHO')

hoth_mass = planet_mass(hoth.gravity,hoth.radius)
hoth_vol = planet_vol(hoth.radius)

print(f'{hoth.name} has a mass of {hoth_mass} and volume of {hoth_vol}')