from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty  # explicity use of property

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

# from kivy.core.window import Window
# Windw.size = (720, 1280)

# TODO:
# 1. Create a GUI for the app
# 2. Write a function or maybe two functions to make needed calculations
# 3. Bind these funcitions to the Kivy app
# 4. Provide an appearance of a virtual keyboard, when a TextInput gets a focus
# 5. Filter out any symbols except numbers

def get_weight(m):
    nitro = str(10 * m / 1000)
    salt = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    monosugars = str(5 * m / 1000)
    salting_time = str(round(m / 500 * 2))

    return {'nitro': nitro, 'salt': salt, 'starts': starts, 'monosugars': monosugars, 'salting_time': salting_time}

class Container(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingr = get_weight(mass)

        self.salt.text = ingr.get('salt')
        self.nitro.text = ingr.get('nitro')
        self.monosugars.text = ingr.get('monosugars')
        self.starts.text = ingr.get('starts')
        self.time.text = ingr.get('salting_time')

class MyApp(App):
    title = 'The Coppa Calc'
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()
