import pip
import json
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

player_data = {
    "score": 0,
    "power": 1
}

def read_data():
    global player_data
    try:
        with open("play.json", "r", encoding="utf-8") as file:
            player_data = json.load(file)
    except:
        print("")

def save_data():
    global player_data
    try:
        with open("play.json", "w", encoding="utf-8") as file:
            json.dump(player_data, file, indent=4, ensure_ascii=True)
    except:
        print("")
def on_enter(self, *args):
    read_data()
    self.ids.score_lbl.text = str(player_data['scoree'])
class GamePlayWindow(Screen):
    def __init__(self, **kw):
            super().__init__(**kw)

def click(self):
    player_data['score'] += 1
    self.ids.score_lbl.text = str(player_data['score'])
    self.ids.ClickerIcon.img.size_hint = (0.5, 0.5)
    save_data()
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(GamePlayWindow(name="game_play_window"))
        return sm

MyApp().run()