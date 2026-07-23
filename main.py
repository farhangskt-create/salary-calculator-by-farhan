from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SalaryCalculatorApp(App):
    def build(self):
        self.title = "Salary Calculator"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # عنوان
        layout.add_widget(Label(text='Salary Calculator', font_size=24, bold=True))

        # بنیادی تنخواہ کا ان پٹ
        layout.add_widget(Label(text='Enter Basic Salary:', font_size=18))
        self.salary_input = TextInput(text='', multiline=False, input_filter='float', font_size=18)
        layout.add_widget(self.salary_input)

        # کیلکولیٹ بٹن
        calc_btn = Button(text='Calculate Total', font_size=18, background_color=(0.1, 0.6, 0.8, 1))
        calc_btn.bind(on_press=self.calculate_salary)
        layout.add_widget(calc_btn)

        # رزلٹ شو کرنے کے لیے لیبل
        self.result_label = Label(text='Total Salary will appear here', font_size=18)
        layout.add_widget(self.result_label)

        return layout

    def calculate_salary(self, instance):
        try:
            basic = float(self.salary_input.text)
            total = basic + (basic * 0.10)
            self.result_label.text = f'Total Salary (with 10% bonus): {total}'
        except ValueError:
            self.result_label.text = 'Please enter a valid number!'

if __name__ == '__main__':
    SalaryCalculatorApp().run()
