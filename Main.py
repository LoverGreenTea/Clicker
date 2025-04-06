import pip
import json
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

player_data = {}
class GamePlayWindow(Screen):
    def __init__(self, **kw):
            super().__init__(**kw)

def click(self):
    score = int(self.ids.score_lbl.text)
    score += 1
    self.ids.score_lbl.text = str(score)
    self.ids.ClickerIcon.img.size_hint = (0.5, 0.5)
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(GamePlayWindow(name="game_play_window"))
        return sm

MyApp().run()