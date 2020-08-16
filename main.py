from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineListItem
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.button import MDRectangleFlatButton

KV = """

<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height
    type_swipe: "auto"

    MDCardSwipeLayerBox:
        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_release: app.on_swipe_complete(root)


    MDCardSwipeFrontBox:

        OneLineListItem:
            id: content
            text: root.text
            ripple_effect: True

Screen:
    BoxLayout:
        orientation:"vertical"
        spacing:10
        MDToolbar:
            title:" WHAT TODO"
            elevation:10

        MDTextField:
            id: text_input
            pos_hint: {'center_x':0.5,'center_y':0.5}
            size_hint_x:None
            width:270
            hint_text:"What to do?"
            icon_right:"lightbulb-on-outline"
            icon_right_color:1,1,0,1


        MDRectangleFlatIconButton:
            text:"add"
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_release:app.add_item(text_input.text)
            text_color:app.theme_cls.primary_color
            icon:"notebook-multiple"

        MDLabel:
            text:"Swipe right on item to remove"
            size_hint_y:0.2
            halign:"center"
            theme_text_color:"Hint"
        ScrollView:
            MDList:
                id:md_list
                padding:20 

        MDBottomAppBar:
            MDToolbar:
                mode:"end"
                type:"bottom"
                icon:"select-color"
                on_action_button: app.show_theme_picker()




"""


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()


class TODOApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.screen = Builder.load_string(KV)
        return self.screen

    def add_item(self, value):
        self.screen.ids.md_list.add_widget(SwipeToDeleteItem(text=value))

    def on_swipe_complete(self, instance):
        self.screen.ids.md_list.remove_widget(instance)

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()


if __name__ == "__main__":
    TODOApp().run()
