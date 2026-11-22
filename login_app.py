import tkinter as tk
from main_app import MainApp

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GST Login")
        self.geometry("560x340")  # کمی فضا بازتر شد تا متن کتاب به زیبایی جا بگیرد
        self.configure(bg="white")
        self.resizable(False, False)

        # عنوان اصلی
        tk.Label(
            self, 
            text="Grey Material Requirement Planning", 
            font=("Arial", 18, "bold"), 
            bg="white"
        ).pack(pady=(15, 4))

        # ایمیل تماس
        tk.Label(
            self, 
            text="Contact: (************)", 
            font=("Arial", 11), 
            fg="#004085", 
            bg="white"
        ).pack(pady=(0, 15))

        # دکمه ورود
        tk.Button(
            self, 
            text="Enter Application",  # عنوان تمیزتر برای ورود به برنامه اصلی
            width=18, 
            font=("Times New Roman", 14, "bold"), 
            fg="black", 
            bg="#ffeb3b", 
            cursor="hand2",
            relief="groove",
            command=self.open_main
        ).pack(pady=15)

        # متن معرفی کتاب و ناشر (Springer)
        book_info = (
            "Companion software for the paper:\n"
            "\"Doi:**********\"\n"
            "Developed by Professor *******"
        )
        tk.Label(
            self, 
            text=book_info, 
            font=("Arial", 9, "italic"), 
            fg="#333333", 
            bg="white", 
            justify="center",
            wraplength=520  # جلوگیری از خروج متن از کادر
        ).pack(side="bottom", pady=15)

    def open_main(self):
        self.destroy()
        app = MainApp()
        app.mainloop()

if __name__ == "__main__":
    login = LoginApp()
    login.mainloop()