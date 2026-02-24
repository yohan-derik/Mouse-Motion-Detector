import tkinter as tk
from pynput import mouse
import threading
import winsound
import time

class MouseHoverDetector:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mouse Hover Detector")
        self.window.geometry("400x300")
        self.window.configure(bg='white')

        self.is_hovering = False
        self.beeping_thread = None
        self.should_beep = False
        self.listener = None

    def is_mouse_over_window(self):
        """Check if mouse is over the window"""
        x, y = mouse.Controller().position
        window_x = self.window.winfo_x()
        window_y = self.window.winfo_y()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        return (window_x < x < window_x + window_width and
                window_y < y < window_y + window_height)

    def beep_continuously(self):
        """Play continuous beeping while hovering"""
        while self.should_beep:
            winsound.Beep(1000, 100)  # 1000 Hz for 100ms
            time.sleep(0.05)  # Small gap between beeps

    def on_move(self, x, y):
        """Callback when mouse moves"""
        currently_hovering = self.is_mouse_over_window()

        if currently_hovering and not self.is_hovering:
            # Just entered the window
            self.is_hovering = True
            self.should_beep = True
            self.beeping_thread = threading.Thread(target=self.beep_continuously, daemon=True)
            self.beeping_thread.start()

        elif not currently_hovering and self.is_hovering:
            # Just left the window
            self.is_hovering = False
            self.should_beep = False

    def on_window_move(self, event=None):
        """Update hover state when window is moved"""
        if not self.is_mouse_over_window() and self.is_hovering:
            self.is_hovering = False
            self.should_beep = False

    def start(self):
        """Start the detector"""
        # Start mouse listener
        self.listener = mouse.Listener(on_move=self.on_move)
        self.listener.start()

        # Bind window move event
        self.window.bind("<Configure>", self.on_window_move)

        # Run tkinter event loop
        self.window.mainloop()

        # Clean up
        self.listener.stop()

if __name__ == "__main__":
    detector = MouseHoverDetector()
    detector.start()
