import tkinter as tk
import customtkinter as ctk
from datetime import datetime
from bus_data import bus_data  # Import the bus data
import cohere

class BusResultsPage:
    def __init__(self, departure, destination, date, gender, bus_type):
        self.root = ctk.CTk()
        self.root.title("Available Buses")
        self.root.geometry("670x800")
        
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
        
        self.cohere_api_key = "rotMOkfFkuw27TPTtsFSkX60FfaBkyToHfloGeUR"
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
        
        details_text = (
            f"{bus['bus_model']} • {bus['seat_capacity']} Seats • "
            f"{'AC' if bus['ac'] else 'Non-AC'} • {'WiFi' if bus['wifi'] else 'No WiFi'} • "
            f"Price: {bus['price']} NPR"
        )
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
        # Get filtered bus data for the specific route and date
        filtered_buses = self.get_filtered_buses()

        # Read additional information from the bus_info.txt file
        try:
            with open('bus_info.txt', 'r') as file:
                additional_info = file.read()
        except FileNotFoundError:
            additional_info = "No additional bus information available."

        if not filtered_buses:
            # If no buses are available, set a specific prompt
            input_text = (
                f"There are no buses available from {self.departure} to {self.destination} on {self.date}.\n"
                f"{additional_info}\n"
                f"Please suggest alternative travel options or notify the user."
            )
        else:
            # Construct a detailed description of the available buses
            bus_info = "\n".join([
                f"Bus {bus['bus_number']} by {bus['service_company']} - {bus['bus_model']}, "
                f"{bus['seat_capacity']} seats, {'AC' if bus['ac'] else 'Non-AC'}, "
                f"{'WiFi' if bus['wifi'] else 'No WiFi'}, Price: {bus['price']} NPR."
                for bus in filtered_buses
            ])

            # Prepare the input for Cohere with more context
            input_text = (
                f"Limit the response to 200 words.\n"
                f"Available buses from {self.departure} to {self.destination} on {self.date}:\n"
                f"{bus_info}\n"
                f"{additional_info}\n"
                f"Find the best option for a {self.gender} traveler."
                f"Always inform the user about construction or natural hazards on the route."
            )

        # Call Cohere's API
        response = self.cohere_client.generate(
            model='command-r-plus',
            prompt=input_text,
            max_tokens=500  # Adjust if needed
        )

        # Add AI's Result heading
        result_label = ctk.CTkLabel(
            self.root,
            text="AI's Recommendation:",
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        result_label.pack(anchor="w", padx=20, pady=(10, 0))

        

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