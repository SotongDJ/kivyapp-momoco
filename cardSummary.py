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

    btempoTitol = StringProperty()
    ftempoTitol = StringProperty()
    btempoText = StringProperty()
    ftempoText = StringProperty()

    takasTitle = StringProperty()
    takasText = StringProperty()
    kekasTitle = StringProperty()
    kekasText = StringProperty()
    karenTitol = StringProperty()
    karenText = StringProperty()

    nammaTitol = StringProperty()
    klassTitol = StringProperty()
    shoopTitol = StringProperty()
    frommTitol = StringProperty()
    tooooTitol = StringProperty()

    nammaText = StringProperty()
    klassText = StringProperty()
    shoopText = StringProperty()
    frommText = StringProperty()
    tooooText = StringProperty()

    def __init__(self, **kwargs):
        super(SummaryCard, self).__init__(**kwargs)
        self.btempoTitol = "Start: "
        self.ftempoTitol = "End: "
        self.kekasTitle = "Filter Class: "
        self.takasTitle = "Target Class: "
        self.karenTitol = "Currency: "

        self.nammaTitol = "namma"
        self.klassTitol = "klass"
        self.shoopTitol = "shoop"
        self.frommTitol = "fromm"
        self.tooooTitol = "toooo"

        self.sumitTitle = "SUMIT"
        self.gleanTitle = "CLEAN"
        self.storeText = 'CHANGE -->'

        self.dicto={
            'btempo' : self.btempoText,
            'ftempo' : self.ftempoText,
            'kekas' : self.kekasText,
            'takas' : self.takasText,
            'karen' : self.karenText,

            'namma' : self.nammaText,
            'klass' : self.klassText,
            'shoop' : self.shoopText,
            'fromm' : self.frommText,
            'toooo' : self.tooooText,
        }

class MomocoApp(App):

    def build(self):
        btempoText = tool.date(modde=6)
        ftempoText = tool.date(modde=6)
        karenText = modDatabase.openSetting(usrdir).get('karen','MYR')
        return SummaryCard(btempoText=btempoText,ftempoText=ftempoText,karenText=karenText,usrdir=usrdir)

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
