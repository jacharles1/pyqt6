from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QCheckBox, QButtonGroup
from PyQt6.QtCore import QSize, Qt 

import sys




#Subclass to customize app main window
class MainWindow(QMainWindow):
    def __init__(self): ##always need init
        super().__init__()

        self.setWindowTitle("My App")

        self.window_title = ['its working','1 percent better', 'do not stop', 'lets go!', 'one more chance', 'uh oh']
        self.current_index = 0


        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.button_clicked)
        self.button.setCheckable(True)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.button.setText("You already clicked me")
        ##self.button.setEnabled(False)
        print("Clicked!")

        self.setWindowTitle(self.window_title[self.current_index])
        self.current_index = (self.current_index + 1)

        if self.current_index == 6:
            self.button.setEnabled(False)
           
          

    
## ^task: create multiple window namnes and have it change through the dictionary. once it reaches to with window 
## title that says uh oph, make box unclickable




app = QApplication(sys.argv)
#windows are hidden by defaulat so we need this
window = MainWindow()
window.show()

app.exec()
