import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        ##############################ADDING WIDGETS##############################
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password = True,multiline = False)
        self.add_widget(self.password)
        ##############################ADDING BUTTONS##############################
        self.confirm_button = Button(text='Confirm Entry', font_size = 32)
        self.confirm_button.bind(on_press = self.confirm)
        self.add_widget(self.confirm_button)
    
    def confirm(self, instance):
        name = self.username.text
        password = self.password.text
        self.add_widget(Label(text = 'Hello ' + name + ' your password is now ' + password))
        

class MyApp(App):
    
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()