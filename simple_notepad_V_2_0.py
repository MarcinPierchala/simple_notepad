import os
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class Notes(QWidget):

    def __init__(self):
        super(Notes, self).__init__()
        self.text = QTextEdit(self)
        self.clear_btn = QPushButton('Clear')
        self.save_btn = QPushButton('Save')
        self.open_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clear_btn)
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.open_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.save_btn.clicked.connect(self.save_text)
        self.clear_btn.clicked.connect(self.clear_text)
        self.open_btn.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        self.setWindowTitle('Edytor TXT')

        self.show()

    def save_text(self):        
    #here is the problem with bug in close procedure..... :(
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
    #problem as before:(
        filename = QFileDialog.getOpenFileName(self, 'Open File'," ", "Text files (*.txt)", os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()

app = QApplication(sys.argv)
notes = Notes()
sys.exit(app.exec_())