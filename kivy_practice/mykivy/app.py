import kivy
from kivy.clock import Clock
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup


class MainPage(Screen):
    input1 = ObjectProperty(None)
    input2 = ObjectProperty(None)
    result = ObjectProperty(None)
    btnsum = ObjectProperty(None)

    def on_touch_up(self, touch):
        # return super().on_touch_up(touch) 
        self.btnsum.opacity = 1
        print("touch up",touch)

    def caldata(self):
        cal = str(int(self.input1.text) + int(self.input2.text))
        self.result.text = cal
        return print(cal)
    # pass

class SecondPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass



def testpopup():
    pop = Popup(title="Invalid",
                cotent=Label(text="Invalid username"),
                size_hint=(None,None),
                size=(400,400))
    pop.open()

kv = Builder.load_file("Main.kv")
sm = WindowManager()
screens = [MainPage(name="main"),SecondPage(name="second")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"



class Foo(object):
    def start(self):
        Clock.schedule_interval(self.callback, 0.5)

    def callback(self, dt):
        print('In callback')

class Mainpage1(GridLayout):
    """docstring for Mainpage."""
    def __init__(self, **kwargs):
        super(Mainpage1, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3

        self.lbinput1 = Label(text="input_data1",font_size="20sp")
        self.add_widget(self.lbinput1)

        self.txinput1 = TextInput(font_size="20sp")
        self.add_widget(self.txinput1)

        self.lbinput2 = Label(text="input_data2",font_size="20sp")
        self.add_widget(self.lbinput2)

        self.txinput2 = TextInput(font_size="20sp")
        self.add_widget(self.txinput2)

        self.btn1 = Button(text="Enter",font_size="20sp")
        self.btn1.bind(on_press = self.caldata)
        self.add_widget(self.btn1)

        self.lbinput3 = Label(font_size="20sp")
        self.add_widget(self.lbinput3)

        
    def caldata(self,btn):
        cal = str(int(self.txinput1.text) + int(self.txinput2.text))
        self.lbinput3.text = cal
        return print(cal)

class MyGrid(Widget):
    input1 = ObjectProperty(None)
    input2 = ObjectProperty(None)
    result = ObjectProperty(None)
    btn = ObjectProperty(None)

    # def on_touch_down(self, touch):
    #     # return super().on_touch_down(touch)
    #     print("touch down",touch)
    
    # def on_touch_move(self, touch):
    #     # return super().on_touch_move(touch)
    #     print("touch move",touch)

   
    # pass
        
class MyApp(App):

    def build(self):
        # return Label(text='Hello world')
        # return Mainpage1()
        # return MyGrid()
        return sm


if __name__ == '__main__':
    MyApp().run()