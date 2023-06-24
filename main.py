from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.username_label = Label(text='Username:')
        self.add_widget(self.username_label)

        self.username_input = TextInput()
        self.add_widget(self.username_input)

        self.password_label = Label(text='Password:')
        self.add_widget(self.password_label)

        self.password_input = TextInput(password=True)
        self.add_widget(self.password_input)

        self.login_button = Button(text='Login', on_release=self.login)
        self.add_widget(self.login_button)

        self.signup_button = Button(text='Sign Up', on_release=self.goto_signup)
        self.add_widget(self.signup_button)

    def login(self, *args):
        username = self.username_input.text
        password = self.password_input.text

        # Check username and password against valid credentials
        if username == 'admin' and password == 'password':
            self.login_successful()
        else:
            self.login_failed()

    def login_successful(self):
        print("Login Successful")
        # Add code to navigate to the next screen or perform other actions

    def login_failed(self):
        print("Login Failed")
        # Add code to display an error message or perform other actions

    def goto_signup(self, *args):
        app = App.get_running_app()
        app.root.current = 'signup'


class SignupScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(SignupScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.username_label = Label(text='Username:')
        self.add_widget(self.username_label)

        self.username_input = TextInput()
        self.add_widget(self.username_input)

        self.password_label = Label(text='Password:')
        self.add_widget(self.password_label)

        self.password_input = TextInput(password=True)
        self.add_widget(self.password_input)

        self.email_label = Label(text='Email:')
        self.add_widget(self.email_label)

        self.email_input = TextInput()
        self.add_widget(self.email_input)

        self.signup_button = Button(text='Sign Up', on_release=self.signup)
        self.add_widget(self.signup_button)

        self.back_button = Button(text='Back', on_release=self.goto_login)
        self.add_widget(self.back_button)

    def signup(self, *args):
        username = self.username_input.text
        password = self.password_input.text
        email = self.email_input.text

        # Perform sign-up logic here
        print(f"Sign up successful for username: {username}, password: {password}, email: {email}")
        # Add code to handle sign-up success and perform any desired actions

    def goto_login(self, *args):
        app = App.get_running_app()
        app.root.current = 'login'


class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        # Create the login screen
        login_screen = Screen(name='login')
        login_screen.add_widget(LoginScreen())
        sm.add_widget(login_screen)

        # Create the signup screen
        signup_screen = Screen(name='signup')
        signup_screen.add_widget(SignupScreen())
        sm.add_widget(signup_screen)

        return sm


if __name__ == '__main__':
    MyApp().run()
