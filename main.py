from database import init_db
from frontend import run_gui

if _name_ == "_main_":
    init_db()
    run_gui()