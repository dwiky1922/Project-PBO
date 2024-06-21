import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from remote_ac_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.powerButton.clicked.connect(self.toggle_power)
        self.tempUpButton.clicked.connect(self.increase_temp)
        self.tempDownButton.clicked.connect(self.decrease_temp)
        self.ac_on = False
        self.temperature = 24

    def toggle_power(self):
        self.ac_on = not self.ac_on
        state = "ON" if self.ac_on else "OFF"
        self.statusBar().showMessage(f"AC turned {state}")

    def increase_temp(self):
        if self.ac_on:
            self.temperature += 1
            self.statusBar().showMessage(f"Temperature set to {self.temperature}°C")

    def decrease_temp(self):
        if self.ac_on:
            self.temperature -= 1
            self.statusBar().showMessage(f"Temperature set to {self.temperature}°C")

if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())