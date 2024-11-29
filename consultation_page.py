import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

class ConsultationPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="white")
        self.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header = ctk.CTkLabel(
            self, 
            text="Consultation", 
            font=("Helvetica", 24, "bold"),
            text_color="black"
        )
        self.header.pack(pady=(20,10), padx=20, anchor='w')
        
        # Search bar
        self.search_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.search_frame.pack(fill=tk.X, padx=20)
        
        self.search_entry = ctk.CTkEntry(
            self.search_frame,
            placeholder_text="Search",
            height=40,
            corner_radius=20,
            border_color="#E0E0E0",
            fg_color="#F5F5F5",
            text_color="white",
            placeholder_text_color="white"
        )
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.filter_btn = ctk.CTkButton(
            self.search_frame,
            text="≡",  # Filter icon
            width=40,
            height=40,
            corner_radius=20,
            fg_color="#FF9F67",
            hover_color="#FF8B4D"
        )
        self.filter_btn.pack(side=tk.RIGHT, padx=(10,0))
        
        # Top Rated Doctors Label
        self.top_rated_label = ctk.CTkLabel(
            self,
            text="Top Rated Doctors",
            font=("Helvetica", 18, "bold"),
            text_color="black"
        )
        self.top_rated_label.pack(pady=(20,10), padx=20, anchor='w')
        
        # Doctor cards
        self.create_doctor_card(
            "Ada Lucas",
            "Expert on diet & nutrition",
            "5.0",
            "#FF9ACD"  # Pink background
        )
        
        self.create_doctor_card(
            "Robert Beck",
            "Expert on diet & nutrition",
            "4.8",
            "#FFB84D"  # Yellow background
        )

    def create_doctor_card(self, name, specialty, rating, bg_color):
        # Create main card container
        card_container = ctk.CTkFrame(
            self,
            fg_color=bg_color,
            corner_radius=20,
        )
        card_container.pack(fill=tk.X, padx=20, pady=10)
        
        # Content frame
        content_frame = ctk.CTkFrame(
            card_container,
            fg_color="transparent",
        )
        content_frame.pack(fill=tk.BOTH, padx=15, pady=15)
        
        # Doctor info
        name_label = ctk.CTkLabel(
            content_frame, 
            text=name,
            font=("Helvetica", 20, "bold"),
            text_color="white"
        )
        name_label.pack(anchor='w')
        
        specialty_label = ctk.CTkLabel(
            content_frame,
            text=specialty,
            font=("Helvetica", 14),
            text_color="white"
        )
        specialty_label.pack(anchor='w', pady=(0, 10))
        
        # Rating pill
        rating_frame = ctk.CTkFrame(
            content_frame,
            fg_color="white",
            corner_radius=12,
        )
        rating_frame.pack(anchor='w')
        
        rating_label = ctk.CTkLabel(
            rating_frame,
            text=f"★ {rating}",
            font=("Helvetica", 12),
            text_color=bg_color,
        )
        rating_label.pack(padx=10, pady=2)

        # Bind events to all widgets in the card
        def on_enter(e):
            card_container.configure(fg_color=self.adjust_color(bg_color, -20))
        
        def on_leave(e):
            card_container.configure(fg_color=bg_color)
        
        def on_click(e):
            self.on_doctor_click(name)

        # Bind events to card container and all its children
        for widget in [card_container, content_frame, name_label, specialty_label, rating_frame, rating_label]:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)

    def on_doctor_click(self, doctor_name):
        print(f"Clicked on doctor: {doctor_name}")

    def adjust_color(self, hex_color, amount):
        # Helper function to darken/lighten colors for hover effect
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
        new_rgb = [max(0, min(255, x + amount)) for x in rgb]
        return f"#{new_rgb[0]:02x}{new_rgb[1]:02x}{new_rgb[2]:02x}" 