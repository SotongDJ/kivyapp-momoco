import os
os.environ['KIVY_DPI'] = '320'
os.environ['KIVY_METRICS_DENSITY'] = '2'

from kivy.app import App
from dbMgr import ListData
from cardCreating import CreateCard

class CreatingApp(App):

    def build(self):
        return CreateCard(usrdir=usrdir)


if __name__ == '__main__':
    usrdir = CreatingApp().user_data_dir
    CreatingApp().run()
