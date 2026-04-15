#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cocos UI Visualizer - Main GUI Application
A powerful tool for previewing and analyzing Cocos2d-x UI files (.csb and .json formats)
"""

import sys
import argparse
from pathlib import Path

try:
    from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QFileDialog, QMenu, QMenuBar, QLabel, QPushButton, QCheckBox,
        QMessageBox, QStatusBar, QSplitter
    )
    from PyQt5.QtCore import Qt, QSize
    from PyQt5.QtGui import QIcon, QFont
except ImportError:
    print("Error: PyQt5 is not installed.")
    print("Please run 'python install.py' to install required dependencies.")
    sys.exit(1)


class CocosUIVisualizer(QMainWindow):
    """Main application window for Cocos UI visualization"""
    
    def __init__(self, initial_path=None):
        """Initialize the main window"""
        super().__init__()
        self.current_path = initial_path or Path.cwd()
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Cocos UI Visualizer")
        self.setWindowIcon(self.create_icon())
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout()
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar area
        toolbar_layout = QHBoxLayout()
        
        # Open folder button
        open_btn = QPushButton("Open Folder")
        open_btn.clicked.connect(self.open_folder)
        toolbar_layout.addWidget(open_btn)
        
        # Open file button
        file_btn = QPushButton("Open File")
        file_btn.clicked.connect(self.open_file)
        toolbar_layout.addWidget(file_btn)
        
        toolbar_layout.addStretch()
        
        # Panel Fill checkbox
        self.panel_fill_checkbox = QCheckBox("Panel Fill")
        self.panel_fill_checkbox.stateChanged.connect(self.on_panel_fill_changed)
        toolbar_layout.addWidget(self.panel_fill_checkbox)
        
        # Show Hidden checkbox
        self.show_hidden_checkbox = QCheckBox("Show Hidden")
        self.show_hidden_checkbox.stateChanged.connect(self.on_show_hidden_changed)
        toolbar_layout.addWidget(self.show_hidden_checkbox)
        
        main_layout.addLayout(toolbar_layout)
        
        # Info area
        info_layout = QHBoxLayout()
        self.info_label = QLabel(f"Current Path: {self.current_path}")
        info_layout.addWidget(self.info_label)
        main_layout.addLayout(info_layout)
        
        # Placeholder for visualization area
        placeholder = QLabel("Load a Cocos UI file (.csb or .json) to begin")
        placeholder.setAlignment(Qt.AlignCenter)
        font = placeholder.font()
        font.setPointSize(14)
        placeholder.setFont(font)
        main_layout.addWidget(placeholder)
        
        central_widget.setLayout(main_layout)
        
        # Create status bar
        self.statusBar().showMessage("Ready")
        
    def create_menu_bar(self):
        """Create the application menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        open_folder_action = file_menu.addAction("Open Folder")
        open_folder_action.triggered.connect(self.open_folder)
        
        open_file_action = file_menu.addAction("Open File")
        open_file_action.triggered.connect(self.open_file)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        
        # View menu
        view_menu = menubar.addMenu("View")
        
        reset_view_action = view_menu.addAction("Reset View")
        reset_view_action.triggered.connect(self.reset_view)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.show_about)
        
        about_author_action = help_menu.addAction("About Author")
        about_author_action.triggered.connect(self.show_about_author)
        
    def open_folder(self):
        """Open a folder dialog to select UI folder"""
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select UI Folder",
            str(self.current_path)
        )
        if folder:
            self.current_path = Path(folder)
            self.info_label.setText(f"Current Path: {self.current_path}")
            self.statusBar().showMessage(f"Loaded folder: {folder}")
            
    def open_file(self):
        """Open a file dialog to select a UI file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Cocos UI File",
            str(self.current_path),
            "Cocos UI Files (*.csb *.json);;All Files (*)"
        )
        if file_path:
            self.current_path = Path(file_path).parent
            self.info_label.setText(f"Current Path: {self.current_path}")
            self.statusBar().showMessage(f"Loaded file: {file_path}")
            
    def on_panel_fill_changed(self):
        """Handle panel fill checkbox change"""
        state = self.panel_fill_checkbox.isChecked()
        self.statusBar().showMessage(f"Panel Fill: {'ON' if state else 'OFF'}")
        
    def on_show_hidden_changed(self):
        """Handle show hidden checkbox change"""
        state = self.show_hidden_checkbox.isChecked()
        self.statusBar().showMessage(f"Show Hidden: {'ON' if state else 'OFF'}")
        
    def reset_view(self):
        """Reset the viewport"""
        self.statusBar().showMessage("View reset")
        
    def show_about(self):
        """Show about dialog"""
        about_text = """
        <b>Cocos UI Visualizer</b> v1.0.0
        <br><br>
        A powerful tool for previewing and analyzing Cocos2d-x UI files.
        <br><br>
        Features:
        <ul>
        <li>Real-time preview of .csb and .json files</li>
        <li>Interactive node inspection</li>
        <li>Visual debugging tools</li>
        <li>Resource validation</li>
        <li>Animation preview</li>
        </ul>
        <br>
        © 2026 All rights reserved.
        """
        QMessageBox.about(self, "About Cocos UI Visualizer", about_text)
        
    def show_about_author(self):
        """Show author information dialog"""
        author_text = """
        <b>Author: WangChuanSef</b>
        <br><br>
        <a href="http://space.bilibili.com/1642823606">Bilibili Channel</a>
        <br>
        <a href="https://github.com/WangChuanSef">GitHub Profile</a>
        <br><br>
        For more information and support, visit the links above.
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("About Author")
        msg_box.setText(author_text)
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setOpenExternalLinks(True)
        msg_box.exec_()
        
    def create_icon(self):
        """Create a simple icon for the application"""
        icon = QIcon()
        return icon
        

def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(
        description="Visualize Cocos UI files (.csb/.json)"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="Path to UI folder or file"
    )
    
    args = parser.parse_args()
    
    # Validate path if provided
    initial_path = None
    if args.path:
        path = Path(args.path)
        if path.exists():
            initial_path = path
        else:
            print(f"Warning: Path does not exist: {args.path}")
    
    # Create and run application
    app = QApplication(sys.argv)
    
    # Set application style
    try:
        app.setStyle('Fusion')
    except:
        pass
    
    # Create main window
    window = CocosUIVisualizer(initial_path)
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
