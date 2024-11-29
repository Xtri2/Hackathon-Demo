import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
from pages.consultation_page import ConsultationPage
from pages.shop_page import ShopPage
from pages.skin_consultation_page import SkinConsultationPage
import ctypes   

class MedicalApp:
    def __init__(self, root):
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except:
            pass
            
        self.root = root
        self.root.title("Medical Consultation App")
        
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Set minimum window size
        self.root.minsize(400, 600)
        
        # Set window size to 60% of screen width and height for better split view compatibility
        window_height = int(screen_height * 0.6)
        window_width = int(screen_width * 0.3)  # Reduced width for split view
        
        # Calculate position for center of screen
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # Set window size and position
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Make the window resizable
        self.root.resizable(True, True)
        
        ctk.set_window_scaling(1.0)
        ctk.set_widget_scaling(1.0)
        
        self.root.configure(bg='white')
        
        self.create_navigation()
        
        self.current_page = None
        self.show_consultation_page()

    def create_navigation(self):
        self.nav_frame = ctk.CTkFrame(
            self.root,
            fg_color="white"
        )
        self.nav_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
        self.home_btn = ctk.CTkButton(
            self.nav_frame, 
            text="Consultation",
            command=self.show_consultation_page,
            fg_color="#FF9F67",
            hover_color="#FF8B4D",
            height=35
        )
        self.home_btn.pack(side=tk.LEFT, expand=True, padx=5)
        
        self.skin_btn = ctk.CTkButton(
            self.nav_frame, 
            text="Skin Care",
            command=self.show_skin_consultation_page,
            fg_color="#FF9F67",
            hover_color="#FF8B4D",
            height=35
        )
        self.skin_btn.pack(side=tk.LEFT, expand=True, padx=5)
        
        self.shop_btn = ctk.CTkButton(
            self.nav_frame, 
            text="Shop",
            command=self.show_shop_page,
            fg_color="#FF9F67",
            hover_color="#FF8B4D",
            height=35
        )
        self.shop_btn.pack(side=tk.LEFT, expand=True, padx=5)

    def show_consultation_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = ConsultationPage(self.root)

    def show_shop_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = ShopPage(self.root)

    def show_skin_consultation_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = SkinConsultationPage(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalApp(root)
    root.mainloop() 