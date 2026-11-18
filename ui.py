from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QLabel, QLineEdit, QComboBox,
                             QSpinBox, QPushButton, QTableWidget, QTableWidgetItem,
                             QMessageBox, QHeaderView, QGroupBox, QRadioButton,
                             QDateEdit, QFrame, QGraphicsDropShadowEffect)
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QColor
from logic import StudentManager


# ---------------------------------------------------------------
# THEME TOKENS  (one place to change the whole look)
# ---------------------------------------------------------------
THEMES = {
    "dark": {
        "bg": "#060814",          # deep space
        "surface": "#0e1329",     # cards
        "surface_alt": "#141b38", # inputs / alt rows
        "border": "#232c57",
        "text": "#e6eaff",
        "muted": "#8a94c4",
        "accent": "#7c5cff",      # electric violet
        "accent2": "#22d3ee",     # aqua
        "on_accent": "#ffffff",
        "warn": "#fbbf24",
        "danger": "#fb4b7a",
        "header_a": "#0e1233",
        "header_b": "#0a2a3d",
        "glow": "#7c5cff",
    },
    "light": {
        "bg": "#eef1fb",
        "surface": "#ffffff",
        "surface_alt": "#f4f6ff",
        "border": "#d9defa",
        "text": "#141a3a",
        "muted": "#64708f",
        "accent": "#5b3df5",
        "accent2": "#0891b2",
        "on_accent": "#ffffff",
        "warn": "#d97706",
        "danger": "#e11d48",
        "header_a": "#e4e0ff",
        "header_b": "#d3f3fb",
        "glow": "#5b3df5",
    },
}


def build_stylesheet(t):
    grad = (f"qlineargradient(x1:0, y1:0, x2:1, y2:0, "
            f"stop:0 {t['accent']}, stop:1 {t['accent2']})")
    header_grad = (f"qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                   f"stop:0 {t['header_a']}, stop:1 {t['header_b']})")
    return f"""
        QWidget {{
            background-color: {t['bg']};
            color: {t['text']};
            font-family: 'Space Grotesk', 'Inter', 'Segoe UI', sans-serif;
            font-size: 14px;
        }}
        QLabel, QRadioButton {{ background: transparent; }}
        QRadioButton::indicator {{
            width: 16px; height: 16px; border-radius: 9px;
            border: 2px solid {t['border']}; background: {t['surface_alt']};
        }}
        QRadioButton::indicator:checked {{
            border: 2px solid {t['accent2']}; background: {t['accent']};
        }}

        /* ---------- hero header ---------- */
        QFrame#headerFrame {{
            background: {header_grad};
            border-bottom: 1px solid {t['accent']};
        }}
        QLabel#titleLabel {{
            font-size: 30px; font-weight: 800; letter-spacing: 1px;
            color: {t['text']};
        }}
        QLabel#subtitleLabel {{ font-size: 14px; color: {t['muted']}; }}
        QPushButton#themeBtn {{
            background: {t['surface']}; color: {t['text']};
            border: 1px solid {t['border']}; border-radius: 18px;
            padding: 8px 18px; font-weight: 600;
        }}
        QPushButton#themeBtn:hover {{ border: 1px solid {t['accent2']}; }}

        /* ---------- stat cards ---------- */
        QFrame#statCard {{
            background-color: {t['surface']};
            border: 1px solid {t['border']};
            border-radius: 16px;
        }}
        QLabel#statValue {{
            font-size: 26px; font-weight: 800; color: {t['accent2']};
        }}
        QLabel#statCaption {{ font-size: 12px; color: {t['muted']}; }}

        /* ---------- cards ---------- */
        QGroupBox {{
            background-color: {t['surface']};
            border: 1px solid {t['border']};
            border-radius: 18px;
            margin-top: 18px; padding: 24px 20px 20px 20px;
        }}
        QGroupBox::title {{
            subcontrol-origin: margin; left: 20px; padding: 0 10px;
            color: {t['accent2']}; font-weight: 700; font-size: 15px;
            background-color: {t['bg']}; border-radius: 8px;
        }}

        /* ---------- inputs ---------- */
        QLineEdit, QComboBox, QSpinBox, QDateEdit {{
            background-color: {t['surface_alt']};
            color: {t['text']};
            border: 1px solid {t['border']};
            border-radius: 12px; padding: 10px 12px;
            selection-background-color: {t['accent']};
        }}
        QLineEdit:hover, QComboBox:hover, QSpinBox:hover, QDateEdit:hover {{
            border: 1px solid {t['muted']};
        }}
        QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QDateEdit:focus {{
            border: 1px solid {t['accent2']};
        }}
        QLineEdit:read-only {{ color: {t['muted']}; }}
        QComboBox QAbstractItemView {{
            background-color: {t['surface']}; color: {t['text']};
            border: 1px solid {t['border']};
            selection-background-color: {t['accent']};
            selection-color: {t['on_accent']}; outline: none;
        }}
        QLineEdit#searchInput {{
            border-radius: 20px; padding: 11px 18px;
        }}

        /* ---------- buttons ---------- */
        QPushButton {{
            border-radius: 12px; padding: 13px;
            font-weight: 700; font-size: 14px;
        }}
        QPushButton#addBtn {{
            background: {grad}; color: {t['on_accent']}; border: none;
        }}
        QPushButton#addBtn:hover {{ background: {t['accent2']}; color: #04121a; }}
        QPushButton#updateBtn {{
            background: transparent; color: {t['warn']};
            border: 1px solid {t['warn']};
        }}
        QPushButton#updateBtn:hover {{ background: {t['warn']}; color: #1a1200; }}
        QPushButton#deleteBtn {{
            background: transparent; color: {t['danger']};
            border: 1px solid {t['danger']};
        }}
        QPushButton#deleteBtn:hover {{ background: {t['danger']}; color: white; }}

        /* ---------- table ---------- */
        QTableWidget {{
            background-color: {t['surface']};
            alternate-background-color: {t['surface_alt']};
            color: {t['text']};
            gridline-color: transparent;
            border: 1px solid {t['border']};
            border-radius: 18px; padding: 6px;
        }}
        QTableWidget::item {{ padding: 8px; border: none; }}
        QTableWidget::item:selected {{
            background: {grad}; color: {t['on_accent']};
        }}
        QHeaderView::section {{
            background-color: {t['surface']}; color: {t['muted']};
            padding: 12px 8px; border: none;
            border-bottom: 1px solid {t['border']};
            font-weight: 700;
        }}
        QScrollBar:vertical {{
            background: transparent; width: 10px; margin: 4px;
        }}
        QScrollBar::handle:vertical {{
            background: {t['border']}; border-radius: 5px; min-height: 30px;
        }}
        QScrollBar::handle:vertical:hover {{ background: {t['accent']}; }}
        QScrollBar::add-line, QScrollBar::sub-line {{ height: 0; }}

        /* ---------- menus ---------- */
        QMenuBar {{ background-color: {t['surface']}; color: {t['text']}; }}
        QMenuBar::item:selected {{ background-color: {t['surface_alt']}; }}
        QMenu {{
            background-color: {t['surface']}; color: {t['text']};
            border: 1px solid {t['border']};
        }}
        QMenu::item:selected {{
            background-color: {t['accent']}; color: {t['on_accent']};
        }}
        QMessageBox {{ background-color: {t['surface']}; }}
    """


class StudentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = StudentManager()
        self.is_dark_mode = True   # futuristic look by default

        # 1. Main Window setup
        self.setWindowTitle("Student Record Manager - Tshering Gatsho Norbu (08230229)")
        self.resize(1200, 800)

        self.setup_menu()
        self.setup_ui()
        self.load_table_data()
        self.apply_theme()

    # ------------------------------------------------------------
    def setup_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        view_menu = menubar.addMenu("View")
        theme_action = view_menu.addAction("Toggle Dark/Light Mode")
        theme_action.triggered.connect(self.toggle_theme)

    # ------------------------------------------------------------
    def make_stat_card(self, caption):
        card = QFrame()
        card.setObjectName("statCard")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(18, 12, 18, 12)
        layout.setSpacing(0)
        value = QLabel("0")
        value.setObjectName("statValue")
        cap = QLabel(caption)
        cap.setObjectName("statCaption")
        layout.addWidget(value)
        layout.addWidget(cap)
        return card, value

    def add_glow(self, widget, color="#7c5cff", blur=30):
        glow = QGraphicsDropShadowEffect(self)
        glow.setBlurRadius(blur)
        glow.setOffset(0, 0)
        glow.setColor(QColor(color))
        widget.setGraphicsEffect(glow)
        return glow

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        root_layout = QVBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # ================= HERO HEADER =================
        self.header_frame = QFrame()
        self.header_frame.setObjectName("headerFrame")
        header_layout = QHBoxLayout(self.header_frame)
        header_layout.setContentsMargins(36, 26, 36, 26)
        header_layout.setSpacing(20)

        title_box = QVBoxLayout()
        title_box.setSpacing(4)
        self.title_label = QLabel("Student Record Manager")
        self.title_label.setObjectName("titleLabel")
        self.subtitle_label = QLabel("Add, search and manage every student record in one place.")
        self.subtitle_label.setObjectName("subtitleLabel")
        title_box.addWidget(self.title_label)
        title_box.addWidget(self.subtitle_label)
        header_layout.addLayout(title_box)
        header_layout.addStretch()

        # Live stats
        card_total, self.stat_total = self.make_stat_card("Students")
        card_avg, self.stat_avg = self.make_stat_card("Average marks")
        card_top, self.stat_top = self.make_stat_card("Top score")
        for card in (card_total, card_avg, card_top):
            card.setMinimumWidth(130)
            header_layout.addWidget(card)

        self.theme_btn = QPushButton("Light mode")
        self.theme_btn.setObjectName("themeBtn")
        self.theme_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.theme_btn.clicked.connect(self.toggle_theme)
        header_layout.addWidget(self.theme_btn)

        root_layout.addWidget(self.header_frame)

        # ================= CONTENT AREA =================
        content_widget = QWidget()
        main_layout = QHBoxLayout(content_widget)
        main_layout.setContentsMargins(36, 28, 36, 32)
        main_layout.setSpacing(28)

        # ---------- LEFT: FORM CARD ----------
        form_group = QGroupBox("Student details")
        form_layout = QGridLayout(form_group)
        form_layout.setSpacing(14)

        form_layout.addWidget(QLabel("Student ID"), 0, 0)
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("e.g., 08230229")
        form_layout.addWidget(self.id_input, 0, 1)

        form_layout.addWidget(QLabel("Full name"), 1, 0)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("e.g., Tshering Gatsho")
        form_layout.addWidget(self.name_input, 1, 1)

        form_layout.addWidget(QLabel("Course"), 2, 0)
        self.course_combo = QComboBox()
        self.course_combo.addItems(["B.Ed IT", "B.Ed Maths", "B.Ed Science", "B.Ed English"])
        form_layout.addWidget(self.course_combo, 2, 1)

        form_layout.addWidget(QLabel("Marks (0-100)"), 3, 0)
        self.marks_spin = QSpinBox()
        self.marks_spin.setRange(0, 100)
        form_layout.addWidget(self.marks_spin, 3, 1)

        form_layout.addWidget(QLabel("Gender"), 4, 0)
        gender_layout = QHBoxLayout()
        self.radio_male = QRadioButton("Male")
        self.radio_female = QRadioButton("Female")
        self.radio_male.setChecked(True)
        gender_layout.addWidget(self.radio_male)
        gender_layout.addWidget(self.radio_female)
        form_layout.addLayout(gender_layout, 4, 1)

        form_layout.addWidget(QLabel("Enrollment date"), 5, 0)
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)
        form_layout.addWidget(self.date_input, 5, 1)

        self.add_btn = QPushButton("Add student")
        self.add_btn.setObjectName("addBtn")
        self.add_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.add_btn.clicked.connect(self.handle_add)
        form_layout.addWidget(self.add_btn, 6, 0, 1, 2)
        self.add_glow(self.add_btn)

        self.update_btn = QPushButton("Update selected")
        self.update_btn.setObjectName("updateBtn")
        self.update_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.update_btn.clicked.connect(self.handle_update)
        form_layout.addWidget(self.update_btn, 7, 0, 1, 2)

        self.delete_btn = QPushButton("Delete selected")
        self.delete_btn.setObjectName("deleteBtn")
        self.delete_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.delete_btn.clicked.connect(self.handle_delete)
        form_layout.addWidget(self.delete_btn, 8, 0, 1, 2)

        form_layout.setRowStretch(9, 1)

        # ---------- RIGHT: TABLE ----------
        right_layout = QVBoxLayout()
        right_layout.setSpacing(16)

        self.search_input = QLineEdit()
        self.search_input.setObjectName("searchInput")
        self.search_input.setPlaceholderText("Search by name or ID...")
        self.search_input.setClearButtonEnabled(True)
        self.search_input.textChanged.connect(self.handle_search)
        right_layout.addWidget(self.search_input)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Course", "Marks", "Gender", "Date"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(44)
        self.table.setShowGrid(False)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.itemSelectionChanged.connect(self.fill_form_from_table)
        right_layout.addWidget(self.table)

        main_layout.addWidget(form_group, 1)
        main_layout.addLayout(right_layout, 2)
        root_layout.addWidget(content_widget)

    # ------------------------------------------------------------
    def apply_theme(self):
        key = "dark" if self.is_dark_mode else "light"
        t = THEMES[key]
        self.setStyleSheet(build_stylesheet(t))
        self.theme_btn.setText("Light mode" if self.is_dark_mode else "Dark mode")
        glow = self.add_btn.graphicsEffect()
        if glow:
            glow.setColor(QColor(t["glow"]))

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def refresh_stats(self):
        students = self.manager.students
        total = len(students)
        marks = []
        for s in students:
            try:
                marks.append(int(s.get("marks", 0)))
            except (ValueError, TypeError):
                pass
        self.stat_total.setText(str(total))
        self.stat_avg.setText(f"{sum(marks) / len(marks):.1f}" if marks else "-")
        self.stat_top.setText(str(max(marks)) if marks else "-")

    # ------------------------------------------------------------
    def load_table_data(self):
        self.table.setRowCount(0)
        for student in self.manager.students:
            self.add_row_to_table(student)
        self.refresh_stats()

    def add_row_to_table(self, student):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(student.get("id", "")))
        self.table.setItem(row, 1, QTableWidgetItem(student.get("name", "")))
        self.table.setItem(row, 2, QTableWidgetItem(student.get("course", "")))
        self.table.setItem(row, 3, QTableWidgetItem(str(student.get("marks", ""))))
        self.table.setItem(row, 4, QTableWidgetItem(student.get("gender", "")))
        self.table.setItem(row, 5, QTableWidgetItem(student.get("date", "")))

    def handle_add(self):
        s_id = self.id_input.text()
        name = self.name_input.text()
        course = self.course_combo.currentText()
        marks = self.marks_spin.value()
        gender = "Male" if self.radio_male.isChecked() else "Female"
        date = self.date_input.date().toString("yyyy-MM-dd")

        is_valid, error_msg = self.manager.validate_student(s_id, name, course, marks)
        if not is_valid:
            QMessageBox.warning(self, "Validation Error", error_msg)
            return

        self.manager.add_student(s_id, name, course, marks, gender, date)
        self.load_table_data()
        self.clear_form()
        QMessageBox.information(self, "Success", "Student added successfully!")

    def handle_update(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a student from the table to update.")
            return

        s_id = self.table.item(selected_row, 0).text()
        name = self.name_input.text()
        course = self.course_combo.currentText()
        marks = self.marks_spin.value()
        gender = "Male" if self.radio_male.isChecked() else "Female"
        date = self.date_input.date().toString("yyyy-MM-dd")

        if not name.strip():
            QMessageBox.warning(self, "Validation Error", "Name cannot be empty.")
            return

        self.manager.update_student(s_id, name, course, marks, gender, date)
        self.load_table_data()
        self.clear_form()
        QMessageBox.information(self, "Success", "Student updated successfully!")

    def handle_delete(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a student to delete.")
            return

        s_id = self.table.item(selected_row, 0).text()
        s_name = self.table.item(selected_row, 1).text()

        reply = QMessageBox.question(self, "Confirm Delete",
                                     f"Are you sure you want to delete {s_name} ({s_id})?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.manager.delete_student(s_id)
            self.load_table_data()
            self.clear_form()

    def handle_search(self, text):
        results = self.manager.search_students(text)
        self.table.setRowCount(0)
        for student in results:
            self.add_row_to_table(student)

    def fill_form_from_table(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            self.id_input.setText(self.table.item(selected_row, 0).text())
            self.id_input.setReadOnly(True)
            self.name_input.setText(self.table.item(selected_row, 1).text())
            self.course_combo.setCurrentText(self.table.item(selected_row, 2).text())
            self.marks_spin.setValue(int(self.table.item(selected_row, 3).text()))

            gender = self.table.item(selected_row, 4).text()
            if gender == "Male":
                self.radio_male.setChecked(True)
            else:
                self.radio_female.setChecked(True)

            date_str = self.table.item(selected_row, 5).text()
            if date_str:
                self.date_input.setDate(QDate.fromString(date_str, "yyyy-MM-dd"))

    def clear_form(self):
        self.id_input.clear()
        self.id_input.setReadOnly(False)
        self.name_input.clear()
        self.course_combo.setCurrentIndex(0)
        self.marks_spin.setValue(0)
        self.radio_male.setChecked(True)
        self.date_input.setDate(QDate.currentDate())