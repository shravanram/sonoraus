from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import pyrebase

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
email='abc@gmail'
password='abcde123'
list1=[]
config = {
    "apiKey": "AIzaSyBqpjwayWXr9GLqKmd7lOquRo1Kgx7LS-Y",
    "authDomain": "lyricquest-89c01.firebaseapp.com",
    "databaseURL": "https://lyricquest-89c01.firebaseio.com",
    "projectId": "lyricquest-89c01",
    "storageBucket": "lyricquest-89c01.appspot.com",
    "messagingSenderId": "72893211179"
  }
firebase = pyrebase.initialize_app(config)
#
# auth = firebase.auth()
# user=auth.sign_in_with_email_and_password("abc@gmail.com","abcde123")
#
db=firebase.database()
auth = firebase.auth()

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        orientation:'vertical'
        Button:	
            text: 'Press to record'
            size_hint:.9,.1
            pos_hint:{'center_x':0.5,'center_y':0.8}
            background_color: 1.0, 0, 0, 1.0
            on_press: root.getAudio()
        Button:
            text: 'Analysis'
            size_hint:.9,.1
            pos_hint:{'center_x':0.5,'center_y':0.6}
            on_press: root.manager.current = 'analysis'
        Button:
            text: 'User Experience'
            size_hint:.9,.1
            pos_hint:{'center_x':0.5,'center_y':0.4}
            on_press: root.manager.current = 'login_page'
<AnalysisScreen>:
    FloatLayout:
        orientation:'vertical'
        Label:
            pos_hint:{'center_x':0.5,'center_y':0.9}
            text:"Please enter the year to view its trends"
        TextInput:
            id:year
            pos_hint:{'center_x':0.4,'center_y':0.8}
            size_hint:(0.5,.1)
        Button:
            id:"year"
            text:"Enter"
            pos_hint:{'center_x':0.7,'center_y':0.8}
            size_hint:(0.1,.1)
            on_release:
                root.trends()
        Label:
            pos_hint:{'center_x':0.5,'center_y':0.4}
            text:"Press press the emotion to see the its trends across the years"
        Button:
            text:"Angry"
            pos_hint:{'center_x':0.2,'center_y':0.3}
            size_hint:(0.1,.1)
            on_release:root.pop_image(self)
        Button:
            text:"Senti"
            pos_hint:{'center_x':0.3,'center_y':0.3}
            size_hint:(0.1,.1)
        Button:
            text:"Happy"
            pos_hint:{'center_x':0.4,'center_y':0.3}
            size_hint:(0.1,.1)
        Button:
            text:"Enter"
            pos_hint:{'center_x':0.5,'center_y':0.3}
            size_hint:(0.1,.1)
        Button:
            text:"Enter"
            pos_hint:{'center_x':0.6,'center_y':0.3}
            size_hint:(0.1,.1)
        Button:
            text:"Enter"
            pos_hint:{'center_x':0.7,'center_y':0.3}
            size_hint:(0.1,.1)
        Button:
            text:"Enter"
            pos_hint:{'center_x':0.8,'center_y':0.3}
            size_hint:(0.1,.1)
        Button:
            text:"Back"
            size_hint:(0.1,0.1)
            pos_hint:{'center_x':0.5,'center_y':0.1}
            on_release:
                root.manager.current="menu"


<ResultsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label: 
            text: root.result
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'Graph'
                font_size: '30sp'
                size:300,100
                size_hint: None, None
                on_press: root.pop1()

            Button:
                text: 'Something'
                font_size: '30sp'
                size:300,100
                size_hint: None, None
                on_press: root.pop1()
        BoxLayout:
            Button:
                text: 'Back to menu'
                size:600,100
                size_hint: None, None

                on_press: root.manager.current = 'menu'


<LoginPage>:
    name:"login_page"
    
    FloatLayout:
        orientation: 'vertical'		
        TextInput:
            pos_hint:{'center_x':0.5,'top':0.9}
            size_hint:(.9,0.1)
            id: login
            
        TextInput:
            pos_hint:{'center_x':0.5,'top':0.8}
            size_hint:(.9,0.1)
            
            id: passw
            password: True # hide password
        Button:
            text: "login"
            pos_hint:{'center_x':0.5,'top':0.5}
            size_hint:(.5,0.1)
            
            on_release: 
                root.sign_in()
                root.pull_playlist()
                root.manager.current="user"


<UserExperience>:
    FloatLayout:
        orientation: 'vertical'	
        
        ScrollView:
            height:40
            Label:
                id: Playscroll
                size_hint_y:None
                text_size: self.width, None
                height: self.texture_size[1]
                halign: 'center'
                valign: 'top'
                text: root.playlist	
        Label:
            id: Play
            text: root.playlist
            background_color: 0, 0, 0, 0
            pos_hint:{'center_x':0.5,'top':1}
            
        TextInput:
            id:SongName
            size_hint:(0.45,0.1)
            pos_hint:{'right':.5,'center_y':0.3}
        Button:
            text:"+"
            size_hint:(.2,.1)
            pos_hint:{'center_x':0.6,'center_y':.3}
            on_release:
                root.insert()
        Button:
            text:"-"
            size_hint:(.2,.1)
            pos_hint:{'center_x':0.8,'center_y':.3}
            on_release:
                root.delete()
        Button:
            text:"Done"
            size_hint:(0.9,.1)
            pos_hint:{'center_x':0.5,'center_y':.1}
            on_release:
                root.push_playlist()
        Button:
            text:"Show Playlist"
            size_hint:(0.9,.1)    
            pos_hint:{'center_x':0.5,'center_y':.2}
            on_release:root.show()      
        Button:
            text:"Exit"
            size_hint:(0.9,.1)    
            pos_hint:{'center_x':0.5,'center_y':.1}

            on_release:
                root.push_playlist()
                root.manager.current="menu"
""")

class MenuScreen(Screen):
    def say_hello(self):
        print ("Heloooooo")
    def getAudio(self):
        print("audio")
        sm.current='results'

    pass
class ResultsScreen(Screen):

    result="answer"

    def pop1(self):
        pop = Popup(title='test', content=Image(source='apple.png'), size=(400, 400))
        pop.open()
    pass

class AnalysisScreen(Screen):
    def analyze(self):
        print("analyzing")
    def pop_image(self,instance):
        print(instance.text)
        pop = Popup(title='test', content=Image(source=instance.text+'.png'), size=(500, 500))
        pop.open()
    def trends(self):
        year=self.ids["year"].text
        print(year)
        pop = Popup(title='test', content=Image(source=year+'.png'), size=(500, 500))
        pop.open()


class LoginPage(Screen):

    def sign_in(self):
        global email,password,obj
        email=self.ids["login"].text
        password=self.ids["passw"].text
        user = auth.sign_in_with_email_and_password(email+".com", password)
    def pull_playlist(self):
        global email,password,list1
        try:
            a=list(db.child(email).child("playlist").get().val())[0]
            list1 = list(db.child(email).child("playlist").child(a).get().val())

        except:
            if(len(list1) == 0):
                print(".NO ENTRIES.")




class UserExperience(Screen):



    playlist=""
    def show(self):
        global email,password,list1
        self.playlist="\n".join(list1)
        #print(self.playlist)
        self.ids['Playscroll'].text = self.playlist

    def pull_playlist(self):
        global email,password,list1
        try:
            a=list(db.child(email).child("playlist").get().val())[0]
            list1 = list(db.child(email).child("playlist").child(a).get().val())
            self.playlist="\n".join(list1)
        #print(self.playlist)
            self.ids['Playscroll'].text = self.playlist
        except:
            if(len(list1) == 0):
                print(".NO ENTRIES.")

    def insert(self):

        global email,password,list1
        list1.append(self.ids['SongName'].text)
        print("List:",list1)
        self.playlist="\n".join(list1)
        #print(self.playlist)
        self.ids['Playscroll'].text = self.playlist
        print()
        #db.child("abc@gmail").child("playlist").push("sing2S")

    def delete(self):

        global email,password,list1
        try:
            to_del=self.ids['SongName'].text
            print("Deleting:", list1.remove(to_del))
            self.playlist="\n".join(list1)
            #print(self.playlist)
            self.ids['Playscroll'].text = self.playlist
        except:
            pass

    def push_playlist(self):

        global email,password,list1
        firebase = pyrebase.initialize_app(config)
        db=firebase.database()
        db.child(email).remove()
        db.child(email).child("playlist").push(list1)



sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ResultsScreen(name='results'))
sm.add_widget(AnalysisScreen(name='analysis'))
sm.add_widget(LoginPage(name='login_page'))
sm.add_widget(UserExperience(name='user'))





class LoginApp(App):
   def build(self):
       Window.size = (600, 600)
       return sm

if __name__ == '__main__':
    LoginApp().run()
