import sys
import keyboard
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QCompleter
from PyQt6.QtCore import QStringListModel
import pyautotask
class KeyboardTrigger(QObject):
    hotkey_pressed = pyqtSignal()

class LauncherApp(QMainWindow):
    def __init__(self, trigger):
        super().__init__()
        self.trigger = trigger
        
        self.trigger.hotkey_pressed.connect(self.toggle_visibility)
        
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |      
            Qt.WindowType.WindowStaysOnTopHint |  
            Qt.WindowType.Tool                      
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # 2. Main Search Input Box
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search apps, calculate, or type a command...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #202020;
                color: #FFFFFF;
                border: 1px solid #3c3c3c;
                border-radius: 8px;
                padding: 12px 16px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 18px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.setContentsMargins(10, 10, 10, 10)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.resize(600, 75)
        self.center_on_screen()
        
        self.search_input.returnPressed.connect(self.on_type)

    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = int(screen.height() * 0.15)
        self.move(x, y)

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()
            self.activateWindow()
            self.search_input.setFocus()

    def changeEvent(self, event):
        if event.type() == event.Type.ActivationChange and not self.isActiveWindow():
            self.hide()
        super().changeEvent(event)
    def on_type(self):
        command = self.search_input.text().strip()
        pyautotask.inputtask(command)
        self.hide()
        self.search_input.clear()
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    trigger = KeyboardTrigger()
    keyboard.add_hotkey("ctrl+space", lambda: trigger.hotkey_pressed.emit())
    
    launcher = LauncherApp(trigger)
    launcher.show()
    
    sys.exit(app.exec())
