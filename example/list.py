import os
os.environ['KIVY_DPI'] = '320'
os.environ['KIVY_METRICS_DENSITY'] = '2'

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
import pprint


class CreateCard(GridLayout):

    datte = ObjectProperty()
    namma = ObjectProperty()
    klass = ObjectProperty()
    shoop = ObjectProperty()
    fromm = ObjectProperty()
    price = ObjectProperty()
    karen = ObjectProperty()
    toooo = ObjectProperty()
    tpric = ObjectProperty()
    tkare = ObjectProperty()
    desci = ObjectProperty()

    datteTitle = StringProperty()
    nammaTitle = StringProperty()
    klassTitle = StringProperty()
    shoopTitle = StringProperty()
    frommTitle = StringProperty()
    priceTitle = StringProperty()
    karenTitle = StringProperty()
    tooooTitle = StringProperty()
    tpricTitle = StringProperty()
    tkareTitle = StringProperty()
    desciTitle = StringProperty()

    datteText = StringProperty()
    nammaText = StringProperty()
    klassText = StringProperty()
    shoopText = StringProperty()
    frommText = StringProperty()
    priceText = StringProperty()
    karenText = StringProperty()
    tooooText = StringProperty()
    tpricText = StringProperty()
    tkareText = StringProperty()
    desciText = StringProperty()

    storeText = StringProperty()
    sumitText = StringProperty()
    usrdir = StringProperty()

    def stored(self,fro,too,tar,tan):
        tar.text = fro
        self.temra.update({ tan : fro })

    def sumited(self):
        pprint.pprint(self.temra)

    def __init__(self, **kwargs):
        super(CreateCard, self).__init__(**kwargs)
        self.datteTitle = "Date: "
        self.nammaTitle = "Name: "
        self.klassTitle = "Class: "
        self.shoopTitle = "Seller: "
        self.frommTitle = "From: "
        self.karenTitle = "Currency: "
        self.priceTitle = "Price: "
        self.tooooTitle = "To: "
        self.tkareTitle = "Currency: "
        self.tpricTitle = "Price: "
        self.desciTitle = "Notes: "

        self.storeText = 'Store -->'
        self.sumitText = 'Sumit'

        self.temra={
            'datte' : self.datteText,
            'namma' : self.nammaText,
            'klass' : self.klassText,
            'shoop' : self.shoopText,
            'fromm' : self.frommText,
            'price' : self.priceText,
            'karen' : self.karenText,
            'toooo' : self.tooooText,
            'tpric' : self.tpricText,
            'tkare' : self.tkareText,
            'desci' : self.desciText,
        }

class DosApp(App):

    def build(self):
        return CreateCard(usrdir=usrdir)


if __name__ == '__main__':
    usrdir = DosApp().user_data_dir
    DosApp().run()
