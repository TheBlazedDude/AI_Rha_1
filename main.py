import os

def start_gui():
    os.system("python gui/gui_main.py")

def start_terminal():
    from core.agent_core import AIAgent
    ai = AIAgent()
    ai.boot()
    while ai.active:
        ai.run_cycle()

if __name__ == "__main__":
    mode = input("🔧 Modus wählen – 'gui' oder 'terminal': ").strip().lower()
    if mode == "gui":
        start_gui()
    else:
        start_terminal()