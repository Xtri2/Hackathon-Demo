import tkinter as tk
import customtkinter as ctk
from datetime import datetime
from bus_data import bus_data  # Import the bus data
import cohere

class BusResultsPage:
    def __init__(self, departure, destination, date, gender, bus_type):
        self.root = ctk.CTk()
        self.root.title("Available Buses")
        self.root.geometry("650x800")
        
        # Store search parameters
        self.departure = departure
        self.destination = destination
        self.date = date
        self.gender = gender
        self.bus_type = bus_type
        
        # Define fonts and colors
        self.title_font = ("Helvetica", 24, "bold")
        self.heading_font = ("Helvetica", 18)
        self.body_font = ("Helvetica", 14)
        self.small_font = ("Helvetica", 12)
        
        self.bg_color = "#FFFFFF"
        self.root.configure(fg_color=self.bg_color)
        
        self.cohere_api_key = "5ZqVCB40NtEdfDfV7Rjjqy8BMaBPxXLKWD0EFYPH"
        self.cohere_client = cohere.Client(self.cohere_api_key)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header with route
        header_frame = ctk.CTkFrame(self.root, fg_color=self.bg_color)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        route_text = f"{self.departure} → {self.destination}"
        route_label = ctk.CTkLabel(
            header_frame,
            text=route_text,
            font=self.title_font,
            text_color="black"
        )
        route_label.pack(side="left")
        
        date_label = ctk.CTkLabel(
            header_frame,
            text=self.format_date(self.date),
            font=self.heading_font,
            text_color="black"
        )
        date_label.pack(side="right")
        
        # Results count
        results_count = ctk.CTkLabel(
            self.root,
            text=f"Found {len(self.get_filtered_buses())} buses",
            font=self.body_font,
            text_color="gray"
        )
        results_count.pack(anchor="w", padx=20, pady=(0, 20))
        
        # Create scrollable frame for bus results
        scroll_frame = ctk.CTkScrollableFrame(
            self.root,
            fg_color=self.bg_color
        )
        scroll_frame.pack(fill="both", expand=True, padx=20)
        
        # Add bus results
        for bus in self.get_filtered_buses():
            self.create_bus_card(scroll_frame, bus)
        
        self.get_cohere_recommendations()
    
    def create_bus_card(self, parent, bus):
        # Bus card container
        card = ctk.CTkFrame(
            parent,
            fg_color="#F8F9FA",
            corner_radius=10
        )
        card.pack(fill="x", pady=5)
        
        # Operator name and rating
        header_frame = ctk.CTkFrame(card, fg_color="transparent")
        header_frame.pack(fill="x", padx=15, pady=(15, 5))
        
        operator = ctk.CTkLabel(
            header_frame,
            text=bus["service_company"],
            font=("Helvetica", 16, "bold"),
            text_color="black"
        )
        operator.pack(side="left")
        
        rating = ctk.CTkLabel(
            header_frame,
            text=f"{'★' * int(bus['rating'])}{'☆' * (5-int(bus['rating']))} {bus['rating']}",
            font=self.body_font,
            text_color="black"
        )
        rating.pack(side="right")
        
        # Bus details
        details_frame = ctk.CTkFrame(card, fg_color="transparent")
        details_frame.pack(fill="x", padx=15, pady=(5, 15))
        
        details_text = f"{bus['bus_model']} • {bus['seat_capacity']} Seats • {'AC' if bus['ac'] else 'Non-AC'} • {'WiFi' if bus['wifi'] else 'No WiFi'}"
        details = ctk.CTkLabel(
            details_frame,
            text=details_text,
            font=self.small_font,
            text_color="gray"
        )
        details.pack(side="left")
        
        departure_time = ctk.CTkLabel(
            details_frame,
            text=bus["bus_number"],
            font=self.small_font,
            text_color="gray"
        )
        departure_time.pack(side="right")
    
    def format_date(self, date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%Y-%m-%d")
    
    def get_filtered_buses(self):
        # Filter bus data based on search parameters
        return [
            bus for bus in bus_data
            if bus['route']['start'] == self.departure and
               bus['route']['end'] == self.destination and
               bus['date'] == self.date
        ]
    
    def get_cohere_recommendations(self):
        # Prepare the input for Cohere
        input_text = f"Find the best bus from {self.departure} to {self.destination} on {self.date} for a {self.gender} traveler preferring a {self.bus_type} bus."

        # Call Cohere's API
        response = self.cohere_client.generate(
            model='command-r-plus',
            prompt=input_text,
            max_tokens=100
        )

        # Add AI Recommendation heading
        heading_label = ctk.CTkLabel(
            self.root,
            text="AI Recommendation",
            font=("Arial", 20, "bold"),
            text_color="white"
        )
        heading_label.pack(anchor="w", padx=20, pady=(10, 5))

        # Create a scrollable frame for the recommendation
        recommendation_frame = ctk.CTkScrollableFrame(
            self.root,
            fg_color="#333333",
            corner_radius=15,
            height=150  # Set a fixed height for scrolling
        )
        recommendation_frame.pack(fill="x", padx=20, pady=(0, 20))

        # Display the response with a minimalist style
        recommendation_text = response.generations[0].text.strip()
        recommendation_label = ctk.CTkLabel(
            recommendation_frame,
            text=recommendation_text,
            font=("Arial", 16),
            text_color="white",
            justify="left",
            wraplength=550
        )
        recommendation_label.pack(padx=20, pady=10)
    
    def run(self):
        self.root.mainloop() 