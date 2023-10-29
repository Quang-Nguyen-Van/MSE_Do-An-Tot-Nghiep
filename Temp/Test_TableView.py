import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QAbstractItemView
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Table Widget Example')
        self.setGeometry(100, 100, 600, 400)

        # Create a QTableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 500, 300)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Set the number of rows and columns in the table
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)  # Adding an extra column for the buttons

        # Set table headers
        headers = ["ID", "First Name", "Last Name", "Details"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Populate the table with data and buttons
        data = [
            [1, "John", "Doe"],
            [2, "Alice", "Smith"],
            [3, "Bob", "Johnson"],
            [4, "Eve", "Brown"],
            [5, "Charlie", "Davis"]
        ]

        for row, rowData in enumerate(data):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(str(value))

                # Make the items read-only
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                self.tableWidget.setItem(row, col, item)

            # Create a button for the "Details" column
            button = QPushButton("Details")
            button.clicked.connect(self.viewDetails)
            self.tableWidget.setCellWidget(row, len(headers) - 1, button)

    def viewDetails(self):
        button = self.sender()
        if button:
            # Get the row of the button clicked
            row = self.tableWidget.indexAt(button.pos()).row()

            # Retrieve data for the selected row
            id_item = self.tableWidget.item(row, 0)
            first_name_item = self.tableWidget.item(row, 1)
            last_name_item = self.tableWidget.item(row, 2)

            if id_item and first_name_item and last_name_item:
                id_value = id_item.text()
                first_name = first_name_item.text()
                last_name = last_name_item.text()

                # Implement your logic to view details here
                print(f"View details for ID: {id_value}, Name: {first_name} {last_name}")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
