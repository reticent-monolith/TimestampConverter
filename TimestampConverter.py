from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QBoxLayout, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QCalendarWidget, QLabel, QVBoxLayout, QWidget
import datetime, sys


class TimestampConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timestamp Converter")
        self.setFixedSize(400, 100)
        self.setWindowIcon(QIcon("clock.ico"))
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        topRow = QHBoxLayout()
        topRow.addWidget(QLabel("Datetime (ISO)"))
        self.datetimeInput = QLineEdit()
        topRow.addWidget(self.datetimeInput)
        bottomRow = QHBoxLayout()
        bottomRow.addWidget(QLabel("Timestamp"))
        self.timestampInput = QLineEdit()
        bottomRow.addWidget(self.timestampInput)
        self.convertButton = QPushButton("Convert")
        self.layout.addLayout(topRow)
        self.layout.addWidget(self.convertButton)
        self.layout.addLayout(bottomRow)
        self.toConvert = None
        self.datetimeInput.textEdited.connect(lambda text: self.setToConvert(text, which="datetime"))
        self.timestampInput.textEdited.connect(lambda text: self.setToConvert(text, which="timestamp"))
        self.convertButton.clicked.connect(self.convert)
        self.show()


    def getTimestamp(self, date: str) -> str:
        date = datetime.datetime.fromisoformat(date)
        return str(int(date.timestamp()))

    def getDatetime(self, timestamp: str) -> str:
        date = datetime.datetime.fromtimestamp(int(timestamp))
        date = date.isoformat().split('T')
        return f"{date[0]} {date[1]}"

    def convert(self):
        if self.toConvert == "datetime":
            try:
                self.timestampInput.setText(self.getTimestamp(self.datetimeInput.text()))
            except:
                pass
        elif self.toConvert == "timestamp":
            try:
                self.datetimeInput.setText(self.getDatetime(self.timestampInput.text()))
            except:
                pass
        else:
            return

    def setToConvert(self, text, which):
        self.toConvert = which



def main():
    app = QApplication([])
    tc = TimestampConverter()
    sys.exit(app.exec())

if __name__=="__main__":
    main()