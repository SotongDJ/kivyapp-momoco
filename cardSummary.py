from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Rectangle,Color,Line

from kivy.lang import Builder
Builder.load_file('cakvSummarizing.kv')

import pprint
from core import modSummer
from core import modDatabase
from core import tool

class SummaryCard(GridLayout):
    choseBox = ObjectProperty()
    resutBox = ObjectProperty()

    sumitTitle = StringProperty()
    gleanTitle = StringProperty()

    dtempoTitol = StringProperty()
    utempoTitol = StringProperty()
    dtempoText = StringProperty()
    utempoText = StringProperty()

    nammaTitol = StringProperty()
    klassTitol = StringProperty()
    shoopTitol = StringProperty()
    frommTitol = StringProperty()
    karenTitol = StringProperty()
    priceTitol = StringProperty()
    tooooTitol = StringProperty()
    tkareTitol = StringProperty()
    tpricTitol = StringProperty()

    nammaText = StringProperty()
    klassText = StringProperty()
    shoopText = StringProperty()
    frommText = StringProperty()
    karenText = StringProperty()
    priceText = StringProperty()
    tooooText = StringProperty()
    tkareText = StringProperty()
    tpricText = StringProperty()

    def __init__(self, **kwargs):
        super(SummaryCard, self).__init__(**kwargs)
        self.sumitTitle = "SUMIT"
        self.gleanTitle = "CLEAN"

        self.dtempoTitol = "Start: "
        self.utempoTitol = "End: "

        self.nammaTitol = "namma"
        self.klassTitol = "klass"
        self.shoopTitol = "shoop"
        self.frommTitol = "fromm"
        self.karenTitol = "karen"
        self.priceTitol = "price"
        self.tooooTitol = "toooo"
        self.tkareTitol = "tkare"
        self.tpricTitol = "tpric"

        self.storeText = 'CHANGE -->'

        self.dicto={
            'dtempo' : self.dtempoText,
            'utempo' : self.utempoText,
            'namma' : self.nammaText,
            'klass' : self.klassText,
            'shoop' : self.shoopText,
            'fromm' : self.frommText,
            'karen' : self.karenText,
            'price' : self.priceText,
            'toooo' : self.tooooText,
            'tkare' : self.tkareText,
            'tpric' : self.tpricText,
        }

class MomocoApp(App):

    def build(self):
        dtempoText = tool.date(modde=6)
        utempoText = tool.date(modde=6)
        return SummaryCard(dtempoText=dtempoText,utempoText=utempoText,usrdir=usrdir)

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
