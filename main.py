# ==========================================
# STEP 1: Main.py Code Create Karna
# ==========================================
code_data = '''from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

Window.clearcolor = (0.95, 0.96, 0.98, 1)

class SalaryCalculatorApp(App):
    def build(self):
        self.title = "Punjab Pay Revision 2026 - Farhan Iqbal"

        self.bps_chart_2022 = {
            1: [13550, 430], 2: [13820, 490], 3: [14260, 570], 4: [14690, 660],
            5: [15230, 750], 6: [15770, 840], 7: [16310, 910], 8: [16890, 990],
            9: [17500, 1070], 10: [18140, 1170], 11: [18820, 1270], 12: [20310, 1430],
            13: [22110, 1590], 14: [23870, 1790], 15: [25790, 1990], 16: [28070, 2260],
            17: [45070, 3400]
        }

        self.bps_chart_2026 = {
            1: [16260, 520], 2: [16580, 590], 3: [17110, 680], 4: [17630, 790],
            5: [18280, 900], 6: [18920, 1010], 7: [19570, 1090], 8: [20270, 1190],
            9: [21000, 1280], 10: [21770, 1400], 11: [22580, 1520], 12: [24370, 1720],
            13: [26530, 1910], 14: [28640, 2150], 15: [30950, 2390], 16: [33680, 2710],
            17: [54080, 4080]
        }

        self.gp_fund_rates = {
            1: 400, 2: 600, 3: 700, 4: 800, 5: 900, 6: 1000, 7: 1100, 8: 1200,
            9: 1300, 10: 1400, 11: 1500, 12: 1800, 13: 2000, 14: 2200, 15: 2500,
            16: 3100, 17: 4200
        }

        self.selected_scale = 14

        root = ScrollView()
        layout = BoxLayout(orientation="vertical", padding=15, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))

        layout.add_widget(
            Label(
                text="[b]Punjab Pay Revision 2026[/b]",
                markup=True,
                font_size="20sp",
                color=(0.1, 0.2, 0.4, 1),
                size_hint_y=None,
                height=35
            )
        )

        scale_box = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=40)
        scale_box.add_widget(Label(text="Select BPS Scale:", color=(0.2, 0.2, 0.2, 1), font_size="14sp"))
        self.btn_dropdown = Button(
            text="BPS-14",
            size_hint_x=0.6,
            background_color=(0.17, 0.42, 0.69, 1),
            color=(1, 1, 1, 1)
        )

        self.dropdown = DropDown()
        for i in range(1, 18):
            btn = Button(text=f"BPS-{i}", size_hint_y=None, height=35)
            btn.bind(on_release=lambda btn_obj: self.dropdown.select(btn_obj.text))
            self.dropdown.add_widget(btn)

        self.btn_dropdown.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=self.on_scale_select)
        scale_box.add_widget(self.btn_dropdown)
        layout.add_widget(scale_box)

        input_box = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=40)
        input_box.add_widget(Label(text="Old Basic Pay (Rs):", color=(0.2, 0.2, 0.2, 1), font_size="14sp"))
        self.input_basic = TextInput(
            text="36450",
            multiline=False,
            input_filter="int",
            size_hint_x=0.6,
            padding=[10, 10, 10, 10]
        )
        input_box.add_widget(self.input_basic)
        layout.add_widget(input_box)

        btn_calc = Button(
            text="Calculate Salary Increase",
            size_hint_y=None,
            height=45,
            background_color=(0.18, 0.52, 0.35, 1),
            font_size="15sp",
            bold=True
        )
        btn_calc.bind(on_press=self.calculate)
        layout.add_widget(btn_calc)

        self.results_layout = GridLayout(cols=2, spacing=8, size_hint_y=None, height=420)

        self.add_row("Detected Stage:", "val_stage", False)
        self.add_row("New Basic Pay (2026):", "val_new_basic", True)
        self.add_row("Increased Basic Pay:", "val_basic_diff", True)
        self.add_row("Adhoc 2022 (15% Merged):", "val_adhoc22", False, is_red=True)
        self.add_row("Adhoc 2025 (10% Merged):", "val_adhoc25", False, is_red=True)
        self.add_row("New Adhoc Relief 2026 (+7%):", "val_adhoc26", False)
        self.add_row("Conveyance Allowance Diff:", "val_conveyance", False)
        self.add_row("GP Fund Deduction Diff:", "val_gpfund", False, is_red=True)
        self.add_row("Benevolent Fund Diff:", "val_benovlent", False, is_red=True)
        self.add_row("Income Tax Reduction Diff:", "val_tax", False, is_red=True)
        self.add_row("[b]TOTAL NET INCREASE:[/b]", "val_net", True)

        layout.add_widget(self.results_layout)

        footer = Label(
            text="[b][i]Best of Luck from Farhan Iqbal[/i][/b]",
            markup=True,
            font_size="16sp",
            color=(0.17, 0.42, 0.69, 1),
            size_hint_y=None,
            height=45
        )
        layout.add_widget(footer)

        root.add_widget(layout)
        return root

    def add_row(self, title, var_name, is_bold, is_red=False):
        lbl_title = Label(text=title, markup=True, color=(0.2, 0.2, 0.2, 1))
        color = (
            (0.8, 0.2, 0.2, 1)
            if is_red
            else ((0.18, 0.52, 0.35, 1) if is_bold else (0.1, 0.1, 0.1, 1))
        )
        lbl_val = Label(text="-", bold=is_bold, color=color)
        setattr(self, var_name, lbl_val)
        self.results_layout.add_widget(lbl_title)
        self.results_layout.add_widget(lbl_val)

    def on_scale_select(self, instance, text):
        self.btn_dropdown.text = text
        self.selected_scale = int(text.replace("BPS-", ""))

    def calculate(self, instance):
        try:
            user_basic = float(self.input_basic.text)
            scale = self.selected_scale

            init_22, incr_22 = self.bps_chart_2022[scale]
            stage = round((user_basic - init_22) / incr_22)
            if stage < 0:
                stage = 0

            init_26, incr_26 = self.bps_chart_2026[scale]
            new_basic = init_26 + (stage * incr_26)
            basic_diff = new_basic - user_basic

            adhoc22_merged = round(user_basic * 0.15)
            adhoc25_merged = round(user_basic * 0.10)
            new_adhoc26 = round(new_basic * 0.07)
            conveyance_diff = (
                1000 if scale <= 10 else (1428 if scale <= 15 else 2500)
            )

            gross_increase = (
                basic_diff - adhoc22_merged - adhoc25_merged
            ) + new_adhoc26 + conveyance_diff

            gp_fund_diff = round(self.gp_fund_rates.get(scale, 1500) * 0.15)
            benovlent_diff = round((new_basic - user_basic) * 0.03)
            tax_diff = round(new_adhoc26 * 0.02)

            total_deductions = gp_fund_diff + benovlent_diff + tax_diff
            net_increase = gross_increase - total_deductions

            self.val_stage.text = f"Stage {stage}"
            self.val_new_basic.text = f"Rs. {new_basic:,.0f}"
            self.val_basic_diff.text = f"+ Rs. {basic_diff:,.0f}"
            self.val_adhoc22.text = f"- Rs. {adhoc22_merged:,.0f}"
            self.val_adhoc25.text = f"- Rs. {adhoc25_merged:,.0f}"
            self.val_adhoc26.text = f"+ Rs. {new_adhoc26:,.0f}"
            self.val_conveyance.text = f"+ Rs. {conveyance_diff:,.0f}"
            self.val_gpfund.text = f"- Rs. {gp_fund_diff:,.0f}"
            self.val_benovlent.text = f"- Rs. {benovlent_diff:,.0f}"
            self.val_tax.text = f"- Rs. {tax_diff:,.0f}"
            self.val_net.text = f"+ Rs. {net_increase:,.0f}"

        except Exception:
            self.val_net.text = "Invalid Input!"

if __name__ == "__main__":
    SalaryCalculatorApp().run()
'''

with open('main.py', 'w') as f:
    f.write(code_data)

print("✅ main.py recreated successfully!")

# ==========================================
# STEP 2: System Tools & Dependencies Install
# ==========================================
!sudo apt-get update
!sudo apt-get install -y build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev libssl-dev libgdbm-dev liblzma-dev libffi-dev uuid-dev libreadline-dev libncurses5-dev libncursesw5-dev xz-utils tk-dev zlib1g-dev autoconf libtool pkg-config automake zip unzip

# ==========================================
# STEP 3: Setup Stable Buildozer & Build APK
# ==========================================
!pip install --upgrade buildozer cython==0.29.33

!buildozer init
!sed -i 's/title = My Application/title = Salary Calculator by Farhan/g' buildozer.spec
!sed -i 's/package.name = myapp/package.name = salarycalculator/g' buildozer.spec
!sed -i 's/requirements = python3,kivy/requirements = python3,kivy==2.2.1/g' buildozer.spec

!buildozer android debug