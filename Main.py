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
        print("Ха - ні")

def save_data():
    global player_data
    try:
        with open("play.json", "w", encoding="utf-8") as file:
            json.dump(player_data, file, indent=4, ensure_ascii=True)
    except:
        print("json не працує")

class GamePlayWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def on_enter(self, *args):
        read_data()
        self.ids.score_lbl.text = str(player_data['score'])

    def click(self):
        player_data['score'] += 1
        self.ids.score_lbl.text = str(player_data['score'])
        self.ids.ClickerIcon_png.size_hint = (0.5, 1.3)
        save_data()

    def un_click(self):
            self.ids.ClickerIcon.png.size_hint = (0.4, 1)

    def GoToSHOP(self):
        self.manager.current = "shop"
class ShopWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def buy(self, price, bonus):
        save_data()
        if player_data['score'] >= price:
            player_data['score'] -= price
            player_data['power'] += bonus
        save_data()
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(GamePlayWindow(name="game_play_window"))
        sm.add_widget(ShopWindow(name="shop"))
        return sm


MyApp().run()