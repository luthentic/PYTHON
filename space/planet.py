#CLASS
class Planet:
  shape = 'round'

  def __init__(self,name,radius,gravity,system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system
  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'
  @classmethod
  def commons(cls):
    return f'All planets are {cls.shape}'
  @staticmethod
  def spin(speed='2000 mile per hour'):
    return f'The speed and spins at {speed}'

hoth = Planet('LEE',20000,5.6,'HOHOHO')
print(f'Name is:{hoth.name}')
print(f'Radius is:{hoth.radius}')
print(f'Gravity is:{hoth.gravity}')
print(hoth.orbit())
print(Planet.commons())
print(Planet.spin('1000 miles'))