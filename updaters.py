
from gui.maingui import MainGUI

def update_gui(line: str, gui: MainGUI):

    if "RN:" in line:
        gui.set_led("Run", True)
    elif "ST:" in line:
        gui.set_led("Run", False)

    
    elif "EB:" in line and "enabled" in line:
        gui.set_led("Balance", True)
    elif "DB:" in line and "disabled" in line:
        gui.set_led("Balance", False)
        
    
    elif "XE:" in line and "on" in line:
        gui.set_led("Ext Bus", True)
    elif "XD:" in line and "off" in line:
        gui.set_led("Ext Bus", False)
        
    
    elif "EQ:" in line and "enabled" in line:
        gui.set_led("MQ Dump", True)
    elif "DQ:" in line and "disabled" in line:
        gui.set_led("MQ Dump", False)
        
    
    elif "SN:" in line and "-> ON" in line:
        gui.set_led("Show DN", True)
    elif "SN:" in line and "-> OFF" in line:
        gui.set_led("Show DN", False)
        
    
    elif "ED:" in line and "enabled" in line:
        gui.set_led("Debug", True)
    elif "DD:" in line and "disabled" in line:
        gui.set_led("Debug", False)

    
    elif "E2:" in line and "enabled" in line:
        gui.set_led("Debug 2", True)
    elif "D2:" in line and "disabled" in line:
        gui.set_led("Debug 2", False)

    
    elif "TA:" in line and "active" in line:
        gui.set_led("Trace", True)
    elif "DT:" in line and "disabled" in line:
        gui.set_led("Trace", False)
        
    
    elif "EE:" in line and "enabled" in line:
        gui.set_led("Error", True)
    elif "DE:" in line and "disabled" in line:
        gui.set_led("Error", False)