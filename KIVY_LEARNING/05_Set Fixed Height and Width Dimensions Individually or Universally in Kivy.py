import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 1

        self.inner_grid = GridLayout()
        self.inner_grid.cols = 2
        ##############################ADDING WIDGETS##############################
        self.inner_grid.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline = False)
        self.inner_grid.add_widget(self.username)
        self.inner_grid.add_widget(Label(text='Password'))
        self.password = TextInput(password = True,multiline = False)
        self.inner_grid.add_widget(self.password)
        ##############################ADDING BUTTONS##############################
        self.confirm_button = Button(text='Confirm Entry', font_size = 32)
        self.confirm_button.bind(on_press = self.confirm)
        self.add_widget(self.inner_grid)
        self.add_widget(self.confirm_button)
        self.output_label = Label(text = '')
        self.add_widget(self.output_label)

    
    def confirm(self, instance):
        name = self.username.text
        password = self.password.text
        self.output_label.text = 'Hello ' + name + ' your password is now ' + password
        

class MyApp(App):
    
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()