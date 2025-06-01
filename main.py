from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# 載入 ui.kv
Builder.load_file("ui.kv")

class JizhangForm(BoxLayout):
    def submit(self, instance):
        jtype = self.ids.type_spinner.text
        amount = self.ids.amount_input.text
        remark = self.ids.remark_input.text
        print(f"📒 記帳：{jtype} - {amount} 元 - 備註：{remark}")
        self.ids.amount_input.text = ''
        self.ids.remark_input.text = ''

class JizhangApp(App):
    def build(self):
        return JizhangForm()

if __name__ == '__main__':
    JizhangApp().run()