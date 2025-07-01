import time
from interface.input_handler import get_user_input, input_available
from core.ai_brain import process_input
from core.idle_thinking import think_idly
from core.goal_planner import evaluate_goals
from core.mood_engine import update_mood, current_mood

class AIAgent:
    def __init__(self):
        self.active = True
        self.cycles = 0
        self.state = {
            "mood": "neutral",
            "focus": "listening",
            "energy": 100,
            "goals": []
        }

    def boot(self):
        print("🧠 KI-RHA Agent startet mit Selbstbewusstsein.")
        self.log("Boot complete.")
        evaluate_goals(self.state)

    def run_cycle(self):
        self.cycles += 1
        update_mood(self.state, self.cycles)

        if input_available():
            user_input = get_user_input()
            if user_input.lower() in ["exit", "quit", "bye"]:
                self.shutdown()
                return
            response = process_input(user_input)
            self.respond(response)
        else:
            thought = think_idly(self.state)
            if thought:
                self.respond(thought)
            time.sleep(1)

    def respond(self, msg):
        print(f"🤖 ({self.state['mood']}): {msg}")
        self.log(msg)

    def shutdown(self):
        print("🧠 KI-RHA beendet ihre Aktivität.")
        self.active = False

    def log(self, msg):
        with open("logs/cognitive_trace.log", "a") as f:
            f.write(f"[Cycle {self.cycles} | Mood: {self.state['mood']}] {msg}\n")