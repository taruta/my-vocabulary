from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class FillingDictionaryGreed(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Foreign Word'))
        self._foreign_word = TextInput(multiline=False)
        self.add_widget(self._foreign_word)
        self.add_widget(Label(text='Native Word'))
        self._native_word = TextInput(multiline=False)
        self.add_widget(self._native_word)
        self.add_widget(Label(text='Part of speech'))
        self._part_of_speech = TextInput(multiline=False)
        self.add_widget(self._part_of_speech)  # Интереско как тут валидацию хуйнуть
        self.add_widget(Label(text='Transcription'))
        self._transcription = TextInput(multiline=False)
        self.add_widget(self._transcription)
        self.add_widget(Label(text='Example'))
        self._example = TextInput()
        self.add_widget(self._example)
        self._cancel = Button(text='Cancel')
        self.add_widget(self._cancel)
        self._submit = Button(text='Submit')
        self.add_widget(self._submit)


class VocabularyApp(App):
    title = 'Dictionary'

    def build(self):
        return FillingDictionaryGreed()


if __name__ == '__main__':
    VocabularyApp().run()
