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

        title = "Fan's Test Program"

        # Place fan1 and fan2 into the TestFan layout
        TestFan_layout = [
            [sg.Text(title.center(50), font=('Algerian', 25), justification='center')],
            [sg.Frame('', [[sg.Text(f"Fan 1 \n\nspeed: {fan1.get_speed()} \n,radius: {fan1.get_radius()} \ncolor {fan1.get_color()}\n\n\n", size=(50,5), font=('Elephant',12))]], background_color='Orange',border_width=3)], 
            [sg.Frame('', [[sg.Text(f"Fan 2 \n\nspeed: {fan2.get_speed()} \n,radius: {fan2.get_radius()} \ncolor {fan2.get_color()}\n\n\n", size=(50,5), font=('Elephant',12))]], background_color='Orange',border_width=3)], 
        ]