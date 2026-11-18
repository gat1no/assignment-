import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

# Ensure Kivy version is compatible
kivy.require('2.1.0')

class HelloWorldApp(App):
    def build(self):
        # Layout manager
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Widgets
        label = Label(text="Welcome to Kivy!", font_size=24)
        button = Button(text="Click Me", size_hint=(1, 0.5))
        
        # Event binding
        button.bind(on_press=self.show_message)
        
        # Add widgets to layout
        layout.add_widget(label)
        layout.add_widget(button)
        return layout

    def show_message(self, instance):
        # Popup dialog
        popup = Popup(title="Message", 
                      content=Label(text="Hello! You clicked the Kivy button."),
                      size_hint=(0.8, 0.4), auto_dismiss=True)
        popup.open()

if __name__ == "__main__":
    HelloWorldApp().run()