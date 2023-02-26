import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.core.clipboard import Clipboard
from kivy.uix.filechooser import FileChooserListView
from path import Path
import cv2

import infer

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

from model import Model, DecoderType
from typing import List

class FilePaths:
    """Filenames and paths to data."""
    fn_char_list = '../model/charList.txt'
    fn_summary = '../model/summary.json'
    fn_corpus = '../data/corpus.txt'

def char_list_from_file() -> List[str]:
    with open(FilePaths.fn_char_list) as f:
        return list(f.read())

model = Model(char_list_from_file(), DecoderType.WordBeamSearch, must_restore=True, dump=False)

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

        self.upload_button = Button(text='Upload')
        self.upload_button.bind(on_press=lambda instance: self.on_upload_button_press(instance, self.file_chooser.path))
        self.capture_layout.add_widget(self.upload_button)

        self.file_chooser = FileChooserListView(path=Path('..\data\\'))
        self.file_chooser.bind(selection=self.on_upload_file_selected)

    def on_capture_button_press(self, instance):
        self.camera.export_to_png(Path('.\image.png'))
        img = cv2.imread(Path('.\image.png'))
        img = cv2.flip(img, 1)
        cv2.imwrite(Path('.\image.png'), img)
        self.result_label.text, _ = infer.infer(model, Path('.\image.png'))

        self.copy_button = Button(text='Copy', on_press=self.on_copy_button_press)
        self.capture_layout.add_widget(self.copy_button)

        self.again_button = Button(text='Again', on_press=self.on_again_button_press)
        self.capture_layout.add_widget(self.again_button)

        self.capture_layout.remove_widget(self.capture_button)

        self.camera.play = False

    def on_copy_button_press(self, instance):
        Clipboard.copy(self.result_label.text)

    def on_again_button_press(self, instance):
        self.capture_layout.remove_widget(self.copy_button)
        self.capture_layout.remove_widget(self.again_button)

        self.capture_layout.add_widget(self.capture_button)

        self.result_label.text = ''
        self.camera.play = True

    def on_upload_button_press(self, instance, path):
        self.remove_widget(self.upload_button)
        self.add_widget(self.file_chooser)

    def on_upload_file_selected(self, instance, value):
        self.remove_widget(self.file_chooser)
        self.result_label.text, _ = infer.infer(model, Path(value[0]))

        self.capture_layout.remove_widget(self.capture_button)

        self.again_button = Button(text='Again', on_press=self.on_again_button_press)
        self.capture_layout.add_widget(self.again_button)

        self.copy_button = Button(text='Copy', on_press=self.on_copy_button_press)
        self.capture_layout.add_widget(self.copy_button)

        self.camera.play = False

class MyCameraApp(App):

    def build(self):
        return MainLayout()


if __name__ == '__main__':
    MyCameraApp().run()
