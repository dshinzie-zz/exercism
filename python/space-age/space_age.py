PLANETS = {
    'earth' : 1,
    'mercury' : 0.2408467,
    'venus' : 0.61519726,
    'mars' : 1.8808158,
    'jupiter' : 11.862615,
    'saturn' : 29.447498,
    'uranus' : 84.016846,
    'neptune' : 164.79132
}

class SpaceAge(object):
    def __init__(self, age):
        self.age = age
        self.seconds = age
        self.earth_days = float(age) / float(31557600)

    def _earth_days(self):
        return float(self.age) / float(31557600)

    @classmethod
    def _setattr_planets(cls):
        def make_method(ratio):
            return lambda self: round(self._earth_days() / ratio, 2)

        for planet, ratio in PLANETS.items():
            setattr(cls, 'on_%s' % planet.lower(), make_method(ratio))

SpaceAge._setattr_planets()
