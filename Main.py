import pip
import json
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class GamePlayWindow(Screen):
    def __init__(self, **kw):
            super().__init__(**kw)



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(GamePlayWindow(name="game_play_window"))
        return sm

MyApp().run()