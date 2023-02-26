import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.core.clipboard import Clipboard
import cv2

class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.camera = Camera(resolution=(640, 480), play=True)
        self.add_widget(self.camera)

        self.result_box = BoxLayout(orientation='vertical', size_hint=(1, 0.4))
        self.add_widget(self.result_box)

        self.result_label = Label(text='')
        self.result_box.add_widget(self.result_label)

        self.capture_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.add_widget(self.capture_layout)

        self.capture_button = Button(text='Capture')
        self.capture_button.bind(on_press=self.on_capture_button_press)
        self.capture_layout.add_widget(self.capture_button)

    def on_capture_button_press(self, instance):
        self.camera.export_to_png("image.png")

        self.result_label.text = 'Result: Hello World'

        self.capture_layout.remove_widget(self.capture_button)

        self.copy_button = Button(text='Copy', on_press=self.on_copy_button_press)
        self.capture_layout.add_widget(self.copy_button)

        self.again_button = Button(text='Again', on_press=self.on_again_button_press)
        self.capture_layout.add_widget(self.again_button)

        self.camera.play = False

    def on_copy_button_press(self, instance):
        Clipboard.copy(self.result_label.text)

    def on_again_button_press(self, instance):
        self.capture_layout.remove_widget(self.copy_button)
        self.capture_layout.remove_widget(self.again_button)

        self.capture_layout.add_widget(self.capture_button)

        self.result_label.text = ''
        self.camera.play = True


class MyCameraApp(App):

    def build(self):
        return MainLayout()


if __name__ == '__main__':
    MyCameraApp().run()
