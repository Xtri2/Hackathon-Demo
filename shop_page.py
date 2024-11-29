import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class ShopPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="white")
        self.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header = ctk.CTkLabel(
            self, 
            text="Online Shop", 
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
            text="≡",
            width=40,
            height=40,
            corner_radius=20,
            fg_color="#FF9F67",
            hover_color="#FF8B4D"
        )
        self.filter_btn.pack(side=tk.RIGHT, padx=(10,0))
        
        # Categories
        self.create_categories()
        
        # Products container with scrolling
        self.products_canvas = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.products_canvas.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Products
        self.create_product_card(
            "Vitamin C",
            "With our New Improved formula",
            "$5.99",
            "vitamin_c.png"
        )
        
        self.create_product_card(
            "After Sun",
            "Expert on diet & nutrition",
            "$15.99",
            "after_sun.png"
        )

    def create_categories(self):
        categories = ["Medicine", "Capsule", "Generic", "Syrup", "Phexin"]
        category_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        category_frame.pack(fill=tk.X, padx=20, pady=15)
        
        for category in categories:
            btn = ctk.CTkButton(
                category_frame,
                text=category,
                width=80,
                height=30,
                corner_radius=15,
                fg_color="#F5F5F5",
                text_color="#666666",
                hover_color="#EAEAEA"
            )
            btn.pack(side=tk.LEFT, padx=5)

    def create_product_card(self, name, description, price, image_path):
        # Create main card container
        card_container = ctk.CTkFrame(
            self.products_canvas,
            fg_color="white",
            corner_radius=15,
        )
        card_container.pack(fill=tk.X, pady=10)
        
        # Content frame
        content_frame = ctk.CTkFrame(
            card_container,
            fg_color="transparent",
        )
        content_frame.pack(fill=tk.BOTH, padx=15, pady=15)
        
        # Product info
        name_label = ctk.CTkLabel(
            content_frame,
            text=name,
            font=("Helvetica", 16, "bold"),
            text_color="black"
        )
        name_label.pack(anchor='w')
        
        desc_label = ctk.CTkLabel(
            content_frame,
            text=description,
            text_color="#666666"
        )
        desc_label.pack(anchor='w')
        
        price_label = ctk.CTkLabel(
            content_frame,
            text=price,
            font=("Helvetica", 16, "bold"),
            text_color="#FF9F67"
        )
        price_label.pack(anchor='w', pady=(5,0))

        # Bind events to all widgets in the card
        def on_enter(e):
            card_container.configure(fg_color="#F5F5F5")
        
        def on_leave(e):
            card_container.configure(fg_color="white")
        
        def on_click(e):
            self.on_product_click(name)

        # Bind events to card container and all its children
        for widget in [card_container, content_frame, name_label, desc_label, price_label]:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)

    def on_product_click(self, product_name):
        print(f"Clicked on product: {product_name}")