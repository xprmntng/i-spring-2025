from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
import random

app = QApplication([])
window = QWidget()
window.setWindowTitle('Hello, world...')
# window.setGeometry(0, 0, 400, 400)

layout = QGridLayout()


# layout.setColumnMinimumWidth(32)
# layout.setRowMinimumHeight(32)
window.setLayout(layout)

for r in range(8):
    layout.setRowMinimumHeight(32, r)
    layout.setColumnMinimumWidth(32, r)
    for c in range(8):
        label = QLabel()
        random_color = random.randint(0, 2**32 - 1)
        label.setStyleSheet('QLabel {background-color: #' + '{:06x}'.format(random_color) + '}')
        layout.addWidget(label, r, c)

label = QLabel('This is Qt!')

layout.addWidget(label, 1, 1)

window.show()
exit(app.exec())