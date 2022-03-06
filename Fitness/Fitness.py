from turtle import textinput
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

kivy.require('1.9.0')

#Define our different screens
class HomePage(Screen):
    pass

class SecondPage(Screen):
    pass

class ThirdPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('fitnessapp.kv')

class FitnessApp(App):
    def build(self):
        layout = GridLayout(cols=3)
        self.name = TextInput(text = "Enter your Name")    
        self.age = TextInput(text = "Enter your Age")
        self.weight = TextInput(text = "Enter your Weight")
        submit = Button(text='Submit', on_press = self.submit)
        layout.add_widget(self.name)
        layout.add_widget(self.age)
        layout.add_widget(self.weight)
        return layout

    def submit(self,obj):
        print("Name: "+ self.name.text)
        print("Age: "+ self.age.text)
        print("Weight: "+ self.weight.text)

            
if __name__ == '__main__':
    FitnessApp().run()