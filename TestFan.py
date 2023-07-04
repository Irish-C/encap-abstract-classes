from Fan import Fan
import PySimpleGUI as sg

# Test Program for Fan
class TestFan:
    def run(self):

        # insert theme
        sg.theme('DarkBlue4')

        # create two objects
        fan1 = Fan()
        fan2 = Fan()

        # sets fan1 speed to maximum, radius to 10, color to yellow, and turn on
        fan1.set_speed(Fan.FAST)
        fan1.set_radius(10)
        fan1.set_color('yellow')
        fan1.turn_on(True)

        # sets fan2 speed to maximum, radius to 10, color to yellow, and turn on
        fan2.set_speed(Fan.FAST)
        fan2.set_radius(5)
        fan2.set_color('blue')
        fan2.turn_on(False)