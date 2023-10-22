import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.graphics import Color

class Mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(Mygrid,self).__init__(**kwargs)
        with self.canvas:
            # Add a red color
            Color(101, 92, 93, 0.84)

            # Add a rectangle
            Rectangle(pos=(250, 50), size=(500, 655))
        # Adding Label
        self.lb = Label(text="Calculator", font_size=55, size_hint_y=None,height=100,size_hint_x=None,width=500,pos=(250,600),color=(0,0,0,1))
        self.add_widget(self.lb)
        # Adding Input
        self.ans = TextInput(multiline=False, readonly=False, halign="right", font_size=55, size_hint_y=None,height=80,size_hint_x=None,width=500,pos=(250,480))
        self.add_widget(self.ans)
        # Adding Button
        self.bb = Button(text="Jou", font_size=55, size_hint_y=None,height=100,size_hint_x=None,width=500,pos=(250,200),on_press=self.btn)
        self.add_widget(self.bb)

    def btn(self,instance):
        self.ans.text = str(eval(self.ans.text))

class MyApp(App):
    def build(self):
        return Mygrid()

if __name__ == "__main__":
    MyApp().run()