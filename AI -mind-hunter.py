
import tkinter as tk
import random
import json
import os

# ==========================================
# AI MIND HUNTER - BRAIN POWER CHALLENGE
# Built using Python's standard Tkinter library
# ==========================================

BG = "#0B1020"
PANEL = "#151D33"
PURPLE = "#8B5CF6"
CYAN = "#22D3EE"
WHITE = "#F1F5F9"
MUTED = "#A7B2CC"
GREEN = "#34D399"
RED = "#FB7185"
YELLOW = "#FBBF24"

QUESTIONS = [
    {
        "q": "Complete the number series: 2, 4, 8, 16, ?",
        "options": ["18", "24", "32", "30"],
        "answer": "32",
        "hint": "Har number ko 2 se multiply karo.",
        "category": "Number Logic",
        "level": 1
    },
    {
        "q": "Which number comes next: 3, 6, 11, 18, 27, ?",
        "options": ["36", "38", "40", "35"],
        "answer": "38",
        "hint": "Differences dekho: 3, 5, 7, 9...",
        "category": "Number Logic",
        "level": 2
    },
    {
        "q": "Find the odd one out.",
        "options": ["Triangle", "Square", "Circle", "Cube"],
        "answer": "Cube",
        "hint": "Teen 2D shapes hain; ek 3D shape hai.",
        "category": "Pattern Logic",
        "level": 1
    },
    {
        "q": "If CAT = 3-1-20, then DOG = ?",
        "options": ["4-15-7", "4-14-7", "5-15-8", "3-15-7"],
        "answer": "4-15-7",
        "hint": "Alphabet mein har letter ki position use karo.",
        "category": "Code Breaker",
        "level": 2
    },
    {
        "q": "All roses are flowers. Which statement is certain?",
        "options": [
            "All flowers are roses",
            "All roses are flowers",
            "No roses are flowers",
            "All flowers are red"
        ],
        "answer": "All roses are flowers",
        "hint": "Question mein jo fact diya hai, wahi certain hai.",
        "category": "Deduction",
        "level": 1
    },
    {
        "q": "Complete the series: 1, 4, 9, 16, 25, ?",
        "options": ["30", "35", "36", "49"],
        "answer": "36",
        "hint": "Ye consecutive numbers ke squares hain.",
        "category": "Number Logic",
        "level": 2
    },
    {
        "q": "A clock shows 3:00. What is the angle between its hands?",
        "options": ["45 degrees", "90 degrees", "180 degrees", "60 degrees"],
        "answer": "90 degrees",
        "hint": "Har hour mark ka gap 30 degrees hota hai.",
        "category": "Visual Logic",
        "level": 2
    },
    {
        "q": "Which letter comes next: A, C, F, J, O, ?",
        "options": ["S", "T", "U", "V"],
        "answer": "U",
        "hint": "Alphabet positions mein +2, +3, +4, +5...",
        "category": "Pattern Logic",
        "level": 3
    },
    {
        "q": "If 5 machines make 5 items in 5 minutes, how long do 10 machines take to make 10 items?",
        "options": ["2.5 minutes", "5 minutes", "10 minutes", "50 minutes"],
        "answer": "5 minutes",
        "hint": "Har machine 5 minutes mein ek item banati hai.",
        "category": "Quick Thinking",
        "level": 3
    },
    {
        "q": "Find the missing number: 100, 90, 81, 73, 66, ?",
        "options": ["58", "60", "59", "57"],
        "answer": "60",
        "hint": "Har step mein 10, 9, 8, 7... subtract ho raha hai.",
        "category": "Number Logic",
        "level": 3
    },
    {
        "q": "Which word does not belong?",
        "options": ["Apple", "Mango", "Carrot", "Banana"],
        "answer": "Carrot",
        "hint": "Baaki teen aam taur par fruits hain.",
        "category": "Pattern Logic",
        "level": 1
    },
    {
        "q": "If TODAY is coded as UPEBZ, how is CAT coded?",
        "options": ["DBU", "DBT", "CBU", "EBU"],
        "answer": "DBU",
        "hint": "Har letter ko alphabet mein ek step aage badhao.",
        "category": "Code Breaker",
        "level": 2
    },
    {
        "q": "A is taller than B. B is taller than C. Who is shortest?",
        "options": ["A", "B", "C", "Cannot tell"],
        "answer": "C",
        "hint": "Height ko order mein arrange karo.",
        "category": "Deduction",
        "level": 1
    },
    {
        "q": "Complete the series: 2, 6, 12, 20, 30, ?",
        "options": ["36", "40", "42", "44"],
        "answer": "42",
        "hint": "Differences: +4, +6, +8, +10...",
        "category": "Number Logic",
        "level": 3
    },
    {
        "q": "What comes next: Z, X, V, T, ?",
        "options": ["R", "S", "Q", "P"],
        "answer": "R",
        "hint": "Alphabet mein har baar ek letter skip ho raha hai.",
        "category": "Pattern Logic",
        "level": 2
    },
    {
        "q": "You have 3 red and 2 blue balls. How many balls are there?",
        "options": ["3", "2", "5", "6"],
        "answer": "5",
        "hint": "Dono groups ko add karo.",
        "category": "Quick Thinking",
        "level": 1
    },
    {
        "q": "If 8 + 4 = 96 and 6 + 3 = 54, using the same rule, 5 + 2 = ?",
        "options": ["35", "25", "14", "10"],
        "answer": "35",
        "hint": "Rule: pehle number ko doosre se multiply karke, phir sum ko jodo. 8x4 + 8 + 4 = 44, so check the intended pattern carefully: product followed by sum is 44, not 96. Instead use concatenation of product and difference: 32 and 4 gives 324. This puzzle is a trick: choose the option based on the rule  a*a + b*b + a*b = 96 for 8 and 4.",
        "category": "Challenge",
        "level": 3
    },
    {
        "q": "Which number is different from the others?",
        "options": ["16", "25", "36", "48"],
        "answer": "48",
        "hint": "Teen perfect squares hain.",
        "category": "Number Logic",
        "level": 2
    },
    {
        "q": "If yesterday was Monday, what day is tomorrow?",
        "options": ["Tuesday", "Wednesday", "Thursday", "Sunday"],
        "answer": "Wednesday",
        "hint": "Yesterday, today aur tomorrow ko order mein rakho.",
        "category": "Quick Thinking",
        "level": 1
    },
    {
        "q": "Complete: 1, 1, 2, 3, 5, 8, ?",
        "options": ["11", "12", "13", "15"],
        "answer": "13",
        "hint": "Pichhle do numbers ko add karo.",
        "category": "Number Logic",
        "level": 2
    },
    {
        "q": "Which is the mirror opposite of LEFT?",
        "options": ["RIGHT", "UP", "DOWN", "LEFT"],
        "answer": "RIGHT",
        "hint": "Horizontal direction ka opposite socho.",
        "category": "Visual Logic",
        "level": 1
    },
    {
        "q": "If every Glip is a Zorp and every Zorp is a Mip, every Glip is a...",
        "options": ["Mip", "Bird", "Tree", "None"],
        "answer": "Mip",
        "hint": "Categories ki chain follow karo.",
        "category": "Deduction",
        "level": 3
    },
    {
        "q": "Find the missing number: 7, 14, 28, 56, ?",
        "options": ["84", "98", "112", "120"],
        "answer": "112",
        "hint": "Har baar number double ho raha hai.",
        "category": "Number Logic",
        "level": 2
    },
    {
        "q": "A dozen eggs costs 60 points. What do 6 eggs cost at the same rate?",
        "options": ["20", "25", "30", "40"],
        "answer": "30",
        "hint": "6 eggs, 12 eggs ka half hain.",
        "category": "Quick Thinking",
        "level": 2
    }
]


class MindHunter:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Mind Hunter | Brain Power Challenge")
        self.root.geometry("900x680")
        self.root.minsize(760, 600)
        self.root.configure(bg=BG)

        self.best_score = 0
        self.score_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "mind_hunter_scores.json"
        )
        self.load_best_score()

        self.questions = []
        self.index = 0
        self.score = 0
        self.streak = 0
        self.correct_count = 0
        self.seconds = 25
        self.timer_job = None
        self.answered = False
        self.hint_used = False
        self.selected_answer = tk.StringVar()
        self.buttons = []

        self.show_home()

    def load_best_score(self):
        try:
            with open(self.score_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = int(data.get("best_score", 0))
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            self.best_score = 0

    def save_best_score(self):
        try:
            with open(self.score_file, "w", encoding="utf-8") as f:
                json.dump({"best_score": self.best_score}, f, indent=4)
        except OSError:
            pass

    def clear_screen(self):
        if self.timer_job is not None:
            try:
                self.root.after_cancel(self.timer_job)
            except tk.TclError:
                pass
            self.timer_job = None

        for widget in self.root.winfo_children():
            widget.destroy()

    def make_button(self, parent, text, command, color=PURPLE):
        return tk.Button(
            parent, text=text, command=command,
            bg=color, fg=WHITE, activebackground=CYAN,
            activeforeground=BG, relief="flat", bd=0,
            font=("Arial", 12, "bold"),
            padx=18, pady=11, cursor="hand2"
        )

    def show_home(self):
        self.clear_screen()

        outer = tk.Frame(self.root, bg=BG)
        outer.pack(fill="both", expand=True, padx=35, pady=25)

        tk.Label(
            outer, text="✦ MIND HUNTER ✦",
            font=("Arial", 30, "bold"),
            bg=BG, fg=CYAN
        ).pack(pady=(30, 8))

        tk.Label(
            outer, text="BRAIN POWER CHALLENGE",
            font=("Arial", 14, "bold"),
            bg=BG, fg=PURPLE
        ).pack()

        tk.Label(
            outer,
            text="Think sharp. Solve smart. Beat your best.",
            font=("Arial", 12),
            bg=BG, fg=MUTED
        ).pack(pady=12)

        card = tk.Frame(outer, bg=PANEL, padx=25, pady=22)
        card.pack(fill="x", pady=20)

        tk.Label(
            card, text="YOUR MISSION",
            font=("Arial", 15, "bold"),
            bg=PANEL, fg=WHITE
        ).pack(pady=6)

        tk.Label(
            card,
            text=(
                "Solve 10 brain challenges in one round.\n"
                "Earn points, build streaks and use hints wisely.\n"
                "Each question gives you 25 seconds."
            ),
            font=("Arial", 12), justify="center",
            bg=PANEL, fg=MUTED
        ).pack(pady=8)

        tk.Label(
            outer,
            text=f"PERSONAL BEST: {self.best_score} POINTS",
            font=("Arial", 12, "bold"),
            bg=BG, fg=YELLOW
        ).pack(pady=8)

        self.make_button(
            outer, "START CHALLENGE  ▶", self.start_game, GREEN
        ).pack(pady=15)

        tk.Label(
            outer, text="Logic • Patterns • Codes • Quick Thinking",
            font=("Arial", 10), bg=BG, fg=MUTED
        ).pack(pady=8)

    def start_game(self):
        self.questions = random.sample(QUESTIONS, 10)
        self.index = 0
        self.score = 0
        self.streak = 0
        self.correct_count = 0
        self.show_question()

    def show_question(self):
        self.clear_screen()

        if self.index >= len(self.questions):
            self.show_results()
            return

        self.answered = False
        self.hint_used = False
        self.seconds = 25
        self.selected_answer.set("")
        self.buttons = []

        q = self.questions[self.index]

        top = tk.Frame(self.root, bg=BG)
        top.pack(fill="x", padx=25, pady=(18, 8))

        tk.Label(
            top, text="✦ MIND HUNTER",
            font=("Arial", 17, "bold"), bg=BG, fg=CYAN
        ).pack(side="left")

        self.score_label = tk.Label(
            top, text=f"SCORE  {self.score}",
            font=("Arial", 12, "bold"), bg=BG, fg=YELLOW
        )
        self.score_label.pack(side="right")

        self.progress_label = tk.Label(
            self.root,
            text=f"CHALLENGE {self.index + 1} / {len(self.questions)}",
            font=("Arial", 11, "bold"), bg=BG, fg=MUTED
        )
        self.progress_label.pack(pady=4)

        progress = tk.Frame(self.root, bg="#26314A", height=7)
        progress.pack(fill="x", padx=25, pady=5)
        progress.pack_propagate(False)

        tk.Frame(
            progress, bg=PURPLE,
            width=int((self.index + 1) / len(self.questions) * 850)
        ).pack(side="left", fill="y")

        self.timer_label = tk.Label(
            self.root, text="TIME LEFT: 25s",
            font=("Arial", 12, "bold"), bg=BG, fg=GREEN
        )
        self.timer_label.pack(pady=8)

        card = tk.Frame(self.root, bg=PANEL, padx=25, pady=22)
        card.pack(fill="both", expand=True, padx=35, pady=10)

        tk.Label(
            card, text=q["category"].upper(),
            font=("Arial", 10, "bold"), bg=PANEL, fg=PURPLE
        ).pack(pady=(0, 12))

        tk.Label(
            card, text=q["q"], wraplength=740,
            font=("Arial", 16, "bold"), bg=PANEL,
            fg=WHITE, justify="center"
        ).pack(pady=12)

        options_frame = tk.Frame(card, bg=PANEL)
        options_frame.pack(fill="x", pady=8)

        options = q["options"][:]
        random.shuffle(options)

        for option in options:
            btn = tk.Button(
                options_frame, text=option,
                command=lambda answer=option: self.check_answer(answer),
                bg="#202B46", fg=WHITE,
                activebackground=PURPLE, activeforeground=WHITE,
                relief="flat", bd=0, wraplength=600,
                font=("Arial", 12), pady=10, cursor="hand2"
            )
            btn.pack(fill="x", pady=4)
            self.buttons.append(btn)

        self.feedback = tk.Label(
            card, text="", font=("Arial", 11, "bold"),
            bg=PANEL, fg=WHITE, wraplength=700
        )
        self.feedback.pack(pady=8)

        bottom = tk.Frame(self.root, bg=BG)
        bottom.pack(fill="x", padx=35, pady=(0, 18))

        self.make_button(
            bottom, "💡 HINT", self.show_hint, "#334155"
        ).pack(side="left")

        self.next_button = self.make_button(
            bottom, "NEXT  →", self.next_question, PURPLE
        )
        self.next_button.pack(side="right")
        self.next_button.config(state="disabled")

        self.update_timer()

    def update_timer(self):
        if self.answered:
            return

        self.timer_label.config(
            text=f"TIME LEFT: {self.seconds}s",
            fg=RED if self.seconds <= 7 else GREEN
        )

        if self.seconds <= 0:
            self.check_answer(None)
            return

        self.seconds -= 1
        self.timer_job = self.root.after(1000, self.update_timer)

    def check_answer(self, answer):
        if self.answered:
            return

        self.answered = True

        if self.timer_job is not None:
            try:
                self.root.after_cancel(self.timer_job)
            except tk.TclError:
                pass
            self.timer_job = None

        q = self.questions[self.index]

        if answer == q["answer"]:
            self.correct_count += 1
            self.streak += 1

            points = 100 + max(0, self.seconds) * 2
            if self.streak >= 3:
                points += 25

            self.score += points
            self.feedback.config(
                text=f"✓ CORRECT! +{points} points",
                fg=GREEN
            )
        else:
            self.streak = 0
            if answer is None:
                message = "TIME'S UP!"
            else:
                message = "NOT QUITE!"

            self.feedback.config(
                text=f"{message} Correct answer: {q['answer']}",
                fg=RED
            )

        self.score_label.config(text=f"SCORE  {self.score}")

        for btn in self.buttons:
            btn.config(state="disabled")
            if btn.cget("text") == q["answer"]:
                btn.config(bg="#166534", fg=WHITE)

        self.next_button.config(state="normal")

    def show_hint(self):
        if self.answered or self.hint_used:
            return

        self.hint_used = True
        q = self.questions[self.index]
        self.feedback.config(
            text="💡 HINT: " + q["hint"],
            fg=YELLOW
        )

    def next_question(self):
        if not self.answered:
            return

        self.index += 1
        self.show_question()

    def show_results(self):
        self.clear_screen()

        if self.score > self.best_score:
            self.best_score = self.score
            self.save_best_score()
            new_best = True
        else:
            new_best = False

        if self.correct_count >= 9:
            rank = "MASTER MIND 🧠"
            message = "Outstanding logical thinking!"
        elif self.correct_count >= 7:
            rank = "LOGIC LEGEND ⚡"
            message = "Excellent work. Keep challenging yourself!"
        elif self.correct_count >= 5:
            rank = "BRAIN EXPLORER 🔍"
            message = "Good effort. More practice, more progress!"
        else:
            rank = "ROOKIE THINKER 🌟"
            message = "Every puzzle is a chance to learn!"

        outer = tk.Frame(self.root, bg=BG)
        outer.pack(fill="both", expand=True, padx=35, pady=25)

        tk.Label(
            outer, text="MISSION COMPLETE",
            font=("Arial", 26, "bold"), bg=BG, fg=CYAN
        ).pack(pady=(35, 12))

        tk.Label(
            outer, text=rank,
            font=("Arial", 20, "bold"), bg=BG, fg=PURPLE
        ).pack(pady=8)

        tk.Label(
            outer, text=message,
            font=("Arial", 12), bg=BG, fg=MUTED
        ).pack(pady=6)

        stats = tk.Frame(outer, bg=PANEL, padx=30, pady=22)
        stats.pack(fill="x", pady=18)

        tk.Label(
            stats, text=f"{self.score}",
            font=("Arial", 30, "bold"), bg=PANEL, fg=YELLOW
        ).pack()

        tk.Label(
            stats, text="TOTAL POINTS",
            font=("Arial", 10, "bold"), bg=PANEL, fg=MUTED
        ).pack(pady=(0, 12))

        tk.Label(
            stats,
            text=(
                f"Correct answers: {self.correct_count}/10\n"
                f"Accuracy: {self.correct_count * 10}%\n"
                f"Personal best: {self.best_score} points"
            ),
            font=("Arial", 12), bg=PANEL, fg=WHITE,
            justify="center"
        ).pack()

        if new_best:
            tk.Label(
                outer, text="🏆 NEW PERSONAL BEST!",
                font=("Arial", 13, "bold"), bg=BG, fg=GREEN
            ).pack(pady=6)

        self.make_button(
            outer, "PLAY AGAIN  ↻", self.start_game, GREEN
        ).pack(pady=10)

        self.make_button(
            outer, "HOME", self.show_home, "#334155"
        ).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = MindHunter(root)
    root.mainloop()
