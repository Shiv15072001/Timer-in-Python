from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.progressbar import ProgressBar
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)

class MyCountUpApp(App):
    hours = 0
    min = 0
    started = False
    count = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button = None
        self.button1 = None
        self.progress = None
        self.screen = None
        self.label = None
        self.Input = None
        
        
    def build(self):
        self.icon = "icon.png"
        self.screen = BoxLayout(orientation="vertical", spacing=8, padding=15)
        self.button = Button(text="Start",bold=True, border =([16, 16, 16, 16]),color=(1,0,0,1),background_color=(0,1,0,1))
        self.button1 = Button(text="Stop",bold=True, border =([16, 16, 16, 16]),color=(1,0,0,1),background_color=(0,1,1,1))
        self.button2 = Button(text="Reset",bold=True, border =([16, 16, 16, 16]),color=(1,0,0,1),background_color=(1,0,0,1))
        self.button3 = Button(text="Set",bold=True, border =([16, 16, 16, 16]),color=(1,0,0,1),background_color=(1,1,0,1))
        self.label = Label(text='00:00:00', font_size=45,color=(1,0,0,1))
        self.Input = TextInput(text="100",size_hint=(0.4,0.4),pos_hint={"center_x":0.5,"center_y":0.5})
        self.label3 = Label(text="'It takes Input in Seconds'", font_size=25,color=(1,0,0,1))
        self.label2 = Label(text="", font_size = 20,color=(1,0,0,1))
        self.screen.add_widget(self.button)
        self.screen.add_widget(self.button1)
        self.screen.add_widget(self.button2)
        
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.Input)
        self.screen.add_widget(self.label3)
        self.screen.add_widget(self.button3)
        self.screen.add_widget(self.label2)
        
        
        self.progress = ProgressBar(max=60, value=0)
        self.button.bind(on_press=self.Stop_start)
        self.button1.bind(on_press=self.on_Stop)
        self.button2.bind(on_press=self.reset)
        self.button3.bind(on_press=self.set)
        
        
        self.screen.add_widget(self.progress)
        return self.screen
    
    # To stop the App
    def on_Stop(self, btn):
        Clock.unschedule(self.count_down)
        
    # To Start the App
    def Stop_start(self, btn):
        self.set(btn)
        if cd_time == "0" or cd_time == "":
            Clock.unschedule(self.count_down)
            self.label2.text = "Please enter the time in Seconds'"
            
        else:
            Clock.schedule_interval(self.count_down, 1)
        
    def reset(self, btn):
        Clock.unschedule(self.count_down)
        self.label.text = "00:00:00"
        
        if MyCountUpApp.count or MyCountUpApp.min or MyCountUpApp.hours:
            MyCountUpApp.count = 0
            MyCountUpApp.min = 0
            MyCountUpApp.hours = 0
    
    def set(self, btn):
        global cd_time
        cd_time = self.Input.text
        
        if cd_time == "":
            self.label2.text = "Please enter the time in Seconds or above 0 "
        else:
            MyCountUpApp.count = cd_time[0:10]
            
            MyCountUpApp.hours = int(MyCountUpApp.hours)
            MyCountUpApp.min = int(MyCountUpApp.min)
            MyCountUpApp.count = int(MyCountUpApp.count)
            self.label.text = cd_time
            Clock.unschedule(self.count_down)
            
    def stop_clock(self):
        if MyCountUpApp.hours == 0 and MyCountUpApp.min == 0 and MyCountUpApp.count == 0:
            Clock.unschedule(self.count_down)
    
    def set_alarm(self):
        if MyCountUpApp.hours == 0 and MyCountUpApp.min == 0 and MyCountUpApp.count == 30:
            sound = SoundLoader.load("beep.wav")
            sound.play()
        elif MyCountUpApp.hours == 0 and MyCountUpApp.min == 0 and MyCountUpApp.count == 0:
            sound = SoundLoader.load("Long beep.wav")
            sound.play()
            
    def count_down(self,*args):
        MyCountUpApp.count -= 1
        self.label.text = "HOURS MIN SEC"
        self.progress.value = MyCountUpApp.count
        
    # To play the Beep Sound in Every 1 minutes
        if MyCountUpApp.started:
            MyCountUpApp.count -= 1
        min, count = divmod(self.count, 60)
        hours, min = divmod(min, 60)
        self.label.text = "{:02d}:{:02d}:{:02d}".format(hours,min,count)
        self.stop_clock()
        self.set_alarm()
        
        


if __name__ == "__main__":
    MyCountUpApp().run()