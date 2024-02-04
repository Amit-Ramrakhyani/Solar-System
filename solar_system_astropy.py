import turtle
import math
import astropy.constants as const
import astropy.units as u

# Set up the turtle screen
screen = turtle.Screen()
screen.tracer(0)  # Increase the speed to 0 for a more realistic time scale
screen.setup(1000, 1000)  # Reduce the canvas size

# Create the Sun
sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')
sun.shapesize(0.3)


# Define a function to calculate the angle increment based on the planet's orbital period
def calculate_angle_increment(orbital_period):
    # Convert orbital period to seconds
    orbital_period = orbital_period.to(u.s)
    # Calculate the angle increment based on the time step (e.g., 1 day)
    time_step = 10 * u.day
    time_step = time_step.to(u.s)
    angle_increment = 2 * math.pi * (time_step / orbital_period)
    return angle_increment.value

class Planet(turtle.Turtle):
    def __init__(self, name, semimajor_axis, color, shape_size=0.2):
        super().__init__(shape='circle')
        self.name = name
        self.color(color)
        self.up()
        self.pd()
        self.angle = 0
        self.semimajor_axis = semimajor_axis
        self.shapesize(shape_size)
        self.radius = self.semimajor_axis.to(u.km).value / 10000000  # Adjust the scaling factor
        self.angle_increment = calculate_angle_increment(self.get_orbital_period())

    def get_orbital_period(self):
        # Real orbital periods of the planets in Earth days
        planet_orbital_periods = {
            'Mercury': 88.0,
            'Venus': 224.7,
            'Earth': 365.25,
            'Mars': 687.0,
            'Jupiter': 4332.0,
            'Saturn': 10759.0,
            'Uranus': 30688.0,
            'Neptune': 60182.0,
        }
        return planet_orbital_periods[self.name] * u.day

    def move(self):
        self.angle += self.angle_increment
        x = self.radius * math.cos(self.angle)
        y = self.radius * math.sin(self.angle)
        self.goto(x, y)

# Create planets with real semimajor axes and colors
mercury = Planet('Mercury', const.au * 0.387, color='grey')
venus = Planet('Venus', const.au * 0.723, color='yellow')
earth = Planet('Earth', const.au, color='blue')
mars = Planet('Mars', const.au * 1.524, color='red')
jupiter = Planet('Jupiter', const.au * 5.203, color='brown')
saturn = Planet('Saturn', const.au * 9.583, color='pink')
uranus = Planet('Uranus', const.au * 19.22, color='light blue')
neptune = Planet('Neptune', const.au * 30.05, color='black')

# List of planets
myList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Main simulation loop
while True:
    screen.update()
    
    for i in myList:
        i.move()
