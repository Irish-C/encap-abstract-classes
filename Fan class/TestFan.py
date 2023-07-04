from Fan import Fan
import PySimpleGUI as sg

# Test Program for Fan
class TestFan:
    def run(self):

        # insert theme
        sg.theme('LightBlue6')

        # create two objects
        fan1 = Fan()
        fan2 = Fan()

        # sets fan1 speed to maximum, radius to 10, color to yellow, and turn on
        fan1.set_speed(Fan.FAST)
        fan1.set_radius(10)
        fan1.set_color('yellow')
        fan1.set_on(True)

        # sets fan2 speed to maximum, radius to 10, color to yellow, and turn on
        fan2.set_speed(Fan.MEDIUM)
        fan2.set_radius(5)
        fan2.set_color('blue')
        fan2.set_on(False)

        title = "Fan's Test Program"

        # Place fan1 and fan2 into the TestFan layout
        TestFan_layout = [
            [sg.Text(title.center(50), font=('Elephant', 25), justification='center')],
            [sg.Frame('', [[sg.Text(f"  Fan 1 is turned {'On' if fan1.get_on() else 'Off'} \n\n  speed: {fan1.get_speed()} [max] \n  radius: {fan1.get_radius()} \n  color: {fan1.get_color()}\n\n\n", size=(50,5), font=('Lucida',12))]], background_color='Light Green',border_width=3)], 
            [sg.Frame('', [[sg.Text(f"  Fan 2 is turned {'On' if fan2.get_on() else 'Off'} \n\n  speed: {fan2.get_speed()} \n  radius: {fan2.get_radius()} \n  color: {fan2.get_color()}\n\n\n", size=(50,5), font=('Lucida',12))]], background_color='Pink',border_width=3)], 
        ]

        # Create TestTV window
        TestFan_window = sg.Window('Test Driver Program', TestFan_layout, size=(400, 350))
    
        # Read and close window
        TestFan_window.read()
        TestFan_window.close()