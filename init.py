from gui.gui import GUI
import verify

args = None

def _verify_and_close(gui: GUI):
    """Close GUI iff all inputs are valid."""
    try:
        global args
        verify.serial(gui.get_port(), gui.get_baud())
        verify.log_path(gui.get_path())
        args = (gui.get_port(), int(gui.get_baud()), gui.get_path())
        gui.quit()
        gui.destroy()
    except Exception as e:
        print("\033[1;31m[CONNECT]\033[0m ", e)

def get_args():
    """port, baud, and log path"""
    gui = GUI()
    gui.set_connect_button(lambda: _verify_and_close(gui))
    gui.mainloop()  # blocking
    return args