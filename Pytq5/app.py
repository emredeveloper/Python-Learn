import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    """
    Main window of the application.
    """

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()

        # Set the window properties
        self.setWindowTitle("Data Visualization")

        # Set the window icon
        self.setWindowIcon(QIcon("icon.png"))

        # Set the menu bar
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.plot_menu = self.menu.addMenu("Plot")

        # Set the toolbar
        self.toolbar = self.addToolBar("Toolbar")

        # Set the status bar
        self.status_bar = self.statusBar()

        # Create the figure and canvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)

        # Initialize the data
        self.data = None

        # Show the main window
        self.show()

    def open_file(self):
        """
        Slot function for the open file action.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)")
        if file_path:
            self.data = np.genfromtxt(file_path, delimiter=",")
            self.status_bar.showMessage("File loaded successfully.")

    def plot_data(self):
        """
        Slot function for the plot data action.
        """
        if self.data is None:
            self.status_bar.showMessage("No data available.")
        else:
            x = self.data[:, 0]
            y = self.data[:, 1]
            self.figure.clear()
            self.figure.add_subplot(111).scatter(x, y)
            self.canvas.draw()
            self.status_bar.showMessage("Data plotted successfully.")

    def exit_application(self):
        """
        Slot function for the exit application action.
        """
        sys.exit()

if __name__ == "__main__":
    # Create an application
    app = QApplication(sys.argv)

    # Create a main window
    # Create a main window
    main_window = MainWindow()

    # Create the actions
    open_file_action = main_window.file_menu.addAction("Open File")
    plot_data_action = main_window.plot_menu.addAction("Plot Data")
    exit_application_action = main_window.file_menu.addAction("Exit")

    # Connect the actions to the slots
    open_file_action.triggered.connect(main_window.open_file)
    plot_data_action.triggered.connect(main_window.plot_data)
    exit_application_action.triggered.connect(main_window.exit_application)

    # Add the actions to the toolbar
    main_window.toolbar.addAction(open_file_action)
    main_window.toolbar.addAction(plot_data_action)
    main_window.toolbar.addAction(exit_application_action)

    # Run the application
    sys.exit(app.exec_())

    #
