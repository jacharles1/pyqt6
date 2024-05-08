import psutil
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar
from PyQt6.QtCore import Qt 
import sys 

cpu = psutil.cpu_percent(interval = 1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')
network = psutil.net_io_counters()

memory_percent = memory[2]
disk_usage = disk[3]
net = network[0]


class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle(" @FloatingInPeace's System Monitor")
        self.setGeometry(100,100,400,300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        cpu_label = QLabel("Your current system-wide CPU utilization is: {:.2f}%".format(cpu))
        cpu_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(cpu_label)

        memory_label = QLabel("Memory Usage:")
        memory_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(memory_label)

        memory_progress = QProgressBar()
        memory_progress.setValue(int(memory_percent))
        layout.addWidget(memory_progress)

        disk_label = QLabel("Disk Space: ")
        disk_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(disk_label)

        disk_progress = QProgressBar()
        disk_progress.setValue(int(disk_usage))
        layout.addWidget(disk_progress)

        network_label = QLabel("Network bytes sent: {}".format(net))
        network_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(network_label)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    system_monitor = SystemMonitor()
    sys.exit(app.exec())
