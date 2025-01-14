import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.time_label = tk.Label(root, text="00:00:00.000", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", font=("Helvetica", 14), command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(root, text="Stop", font=("Helvetica", 14), command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), command=self.reset)
        self.reset_button.pack(side="left", padx=10)

        self.running = False
        self.start_time = None
        self.elapsed_time = 0

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            formatted_time = self.format_time(self.elapsed_time)
            self.time_label.config(text=formatted_time)
            self.root.after(10, self.update_time)

    def format_time(self, elapsed):
        minutes, seconds = divmod(int(elapsed), 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((elapsed - int(elapsed)) * 1000)
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00.000")

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()