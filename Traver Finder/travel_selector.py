import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import customtkinter as ctk
from tkcalendar import Calendar
from bus_results import BusResultsPage

class ModernTravelSelector:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Travel Finder")
        self.root.geometry("600x700")
        
        # Define colors
        self.bg_color = "#FFFFFF"  # Pure white background
        self.container_color = "#C9E6F0"  # Light blue
        
        # Configure color theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Sample locations
        self.locations = ["Kathmandu", "Pokhara", "Biratnagar", "Lumbini", "Sikkim", "Darjeeling"]
        
        # Configure style for dropdowns
        self.style = ttk.Style()
        self.style.theme_use('default')
        
        # Configure colors and other properties
        self.style.configure('Rounded.TCombobox',
            background=self.bg_color,
            fieldbackground=self.bg_color,
            selectbackground=self.bg_color,
            selectforeground="black",
            arrowcolor='black',
            borderwidth=0,
            relief="flat",
            padding=15,
            highlightthickness=0
        )
        
        self.style.map('Rounded.TCombobox',
            fieldbackground=[('readonly', self.bg_color), ('active', self.bg_color)],
            selectbackground=[('readonly', self.bg_color), ('active', self.bg_color)],
            selectforeground=[('readonly', 'black'), ('active', 'black')],
            borderwidth=[('readonly', 0), ('active', 0), ('focus', 0)],
            relief=[('readonly', 'flat'), ('active', 'flat'), ('focus', 'flat')]
        )
        
        # Remove the default border
        self.style.layout('Rounded.TCombobox', [
            ('Combobox.field', {'children': [
                ('Combobox.padding', {'children': [
                    ('Combobox.textarea', {'sticky': 'nswe'})
                ], 'sticky': 'nswe'})
            ], 'sticky': 'nswe', 'border': 0}),
            ('Combobox.arrow', {'side': 'right', 'sticky': 'ns'})
        ])
        
        # Configure the listbox style for dropdown
        self.root.option_add('*TCombobox*Listbox.font', ('Arial', 16))
        self.root.option_add('*TCombobox*Listbox.selectBackground', self.bg_color)
        self.root.option_add('*TCombobox*Listbox.selectForeground', 'black')
        self.root.option_add('*TCombobox*Listbox.background', self.bg_color)
        self.root.option_add('*TCombobox*Listbox.foreground', 'black')
        self.root.option_add('*TCombobox*Listbox.relief', 'flat')
        self.root.option_add('*TCombobox*Listbox.borderWidth', '0')
        self.root.option_add('*TCombobox*Listbox.highlightthickness', '0')
        self.root.option_add('*TCombobox*Listbox.activestyle', 'none')
        self.root.option_add('*TCombobox*Listbox.selectBorderWidth', '0')
        self.root.option_add('*TCombobox*Listbox.highlightThickness', '0')
        
        # Define fonts
        self.title_font = ("Helvetica", 32, "bold")
        self.heading_font = ("Helvetica", 18, "bold")
        self.body_font = ("Helvetica", 16)
        self.small_font = ("Helvetica", 12)
        
        # Add variables for radio buttons
        self.gender = tk.StringVar(value="male")
        self.bus_type = tk.StringVar(value="sleeper")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Set root background color
        self.root.configure(fg_color=self.bg_color)
        
        # Title - reduce top padding from 40 to 20
        title_label = ctk.CTkLabel(
            self.root, 
            text="Where would you like\nto go?",
            font=self.title_font,
            justify="left",
            text_color="black"
        )
        title_label.pack(pady=(20, 20), padx=30, anchor="w")
        
        # Create a container frame - reduce padding
        container_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        container_frame.pack(fill="x", padx=30, pady=5)
        
        # Move the entries_frame into the container
        entries_frame = ctk.CTkFrame(container_frame, fg_color=self.container_color, corner_radius=20)
        entries_frame.pack(side="left", fill="both", expand=True, ipady=5)
        
        # Radio buttons frame with proper padding
        radio_frame = ctk.CTkFrame(container_frame, fg_color="transparent")
        radio_frame.pack(side="right", padx=(25, 0), fill="y", pady=5)
        
        # Gender selection - adjust top padding to align with blue box
        gender_label = ctk.CTkLabel(
            radio_frame,
            text="Gender",
            font=self.small_font,
            text_color="gray"
        )
        gender_label.pack(anchor="w", pady=(5, 5))

        male_radio = ctk.CTkRadioButton(
            radio_frame,
            text="Male",
            variable=self.gender,
            value="male",
            font=self.small_font,
            border_width_checked=6,
            fg_color="black",
            hover_color="#333333"
        )
        male_radio.pack(anchor="w", pady=2)

        female_radio = ctk.CTkRadioButton(
            radio_frame,
            text="Female",
            variable=self.gender,
            value="female",
            font=self.small_font,
            border_width_checked=6,
            fg_color="black",
            hover_color="#333333"
        )
        female_radio.pack(anchor="w", pady=2)
        
        # Bus type selection
        bus_type_label = ctk.CTkLabel(
            radio_frame,
            text="Bus Type",
            font=self.small_font,
            text_color="gray"
        )
        bus_type_label.pack(anchor="w", pady=(15, 5))

        sleeper_radio = ctk.CTkRadioButton(
            radio_frame,
            text="Sleeper Bus",
            variable=self.bus_type,
            value="sleeper",
            font=self.small_font,
            border_width_checked=6,
            fg_color="black",
            hover_color="#333333"
        )
        sleeper_radio.pack(anchor="w", pady=2)

        luxury_radio = ctk.CTkRadioButton(
            radio_frame,
            text="Luxury Coach",
            variable=self.bus_type,
            value="luxury",
            font=self.small_font,
            border_width_checked=6,
            fg_color="black",
            hover_color="#333333"
        )
        luxury_radio.pack(anchor="w", pady=2)
        
        # From dropdown - reduce padding
        self.from_var = tk.StringVar()
        self.from_combo = ttk.Combobox(
            entries_frame,
            textvariable=self.from_var,
            values=["Departure"] + self.locations,
            state="readonly",
            font=self.body_font,
            style='Rounded.TCombobox'
        )
        self.from_combo.set("Departure")
        self.from_combo.pack(fill="x", padx=20, pady=(30, 4))
        
        # Change to bigger and bolder down arrow
        arrow_label = ctk.CTkLabel(
            entries_frame,
            text="↓",  # Unicode long down arrow
            font=("Arial", 28, "bold"),  # Increased size to 28 and kept bold
            text_color="#444444",  # Slightly darker gray for more emphasis
            fg_color="transparent"
        )
        arrow_label.pack(pady=6)  # Increased padding for better spacing
        
        # To dropdown with reduced padding
        self.to_var = tk.StringVar()
        self.to_combo = ttk.Combobox(
            entries_frame,
            textvariable=self.to_var,
            values=["Destination"] + self.locations,
            state="readonly",
            font=self.body_font,
            style='Rounded.TCombobox'
        )
        self.to_combo.set("Destination")
        self.to_combo.pack(fill="x", padx=20, pady=(20, 8))
        
        # Calendar container frame
        calendar_container = ctk.CTkFrame(self.root, fg_color=self.container_color, corner_radius=20)
        calendar_container.pack(fill="x", padx=30, pady=20)
        
        # Selected date label
        self.date_label = ctk.CTkLabel(
            calendar_container,
            text="Select Date",
            font=self.small_font,
            text_color="gray",
            anchor="w"
        )
        self.date_label.pack(fill="x", padx=20, pady=(15, 5))
        
        # Calendar frame
        calendar_frame = ctk.CTkFrame(calendar_container, fg_color=self.bg_color, corner_radius=15)
        calendar_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        # Calendar widget with custom styling
        self.calendar = Calendar(
            calendar_frame,
            selectmode='day',
            date_pattern='y-mm-dd',
            showweeknumbers=False,
            background=self.bg_color,
            foreground='black',
            selectforeground='white',
            selectbackground='black',
            normalforeground='black',
            normalbackground=self.bg_color,
            headersbackground=self.bg_color,
            headersforeground='black',
            bordercolor=self.bg_color,
            othermonthforeground='#CCCCCC',
            othermonthbackground=self.bg_color,
            font=self.small_font,
            borderwidth=0,
            weekendbackground=self.bg_color,
            weekendforeground='black',
            disabledselectbackground=self.bg_color,
            disableddaybackground=self.bg_color
        )
        
        # Add custom styling for date elements
        def style_calendar(event=None):
            # Get all calendar elements
            for widget in calendar_frame.winfo_children():
                if isinstance(widget, tk.Label):
                    # Create a frame for each date
                    if widget.winfo_name() == "!label":  # Only date labels
                        date_frame = ctk.CTkFrame(
                            widget.master,
                            width=30,
                            height=30,
                            corner_radius=15,
                            fg_color=self.bg_color
                        )
                        
                        # Move the date label into the frame
                        widget.configure(
                            background=self.bg_color,
                            padx=0,
                            pady=0
                        )
                        
                        # Bind hover effects
                        widget.bind('<Enter>', lambda e, w=widget: self.on_date_hover(e, w))
                        widget.bind('<Leave>', lambda e, w=widget: self.on_date_leave(e, w))
                        
                        # Position the frame
                        date_frame.place(
                            x=widget.winfo_x(),
                            y=widget.winfo_y(),
                            width=30,
                            height=30
                        )
                        
                        # Move label to front
                        widget.lift()
        
        # Apply styling after calendar is fully loaded
        self.root.after(100, style_calendar)
        
        self.calendar.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Bind date selection
        self.calendar.bind('<<CalendarSelected>>', self.on_date_select)
        
        # Search button
        search_btn = ctk.CTkButton(
            self.root,
            text="Search",
            height=50,
            fg_color="black",
            hover_color="#333333",
            font=self.heading_font,
            corner_radius=15,
            command=self.search_buses
        )
        search_btn.pack(fill="x", padx=30, pady=20)
        
        # Bind combobox events
        self.from_combo.bind('<<ComboboxSelected>>', lambda e: self.on_from_select(e))
        self.to_combo.bind('<<ComboboxSelected>>', lambda e: self.on_to_select(e))
    
    def search_buses(self):
        departure = self.from_var.get()
        destination = self.to_var.get()
        selected_date = self.calendar.selection_get()
        date = selected_date.strftime("%Y-%m-%d")
        gender = self.gender.get()
        bus_type = self.bus_type.get()
        
        if departure == "Departure" or destination == "Destination" or not date:
            # Show error message
            error_label = ctk.CTkLabel(
                self.root,
                text="Please select departure, destination, and date",
                text_color="red",
                font=self.small_font
            )
            error_label.pack(pady=(0, 10))
            self.root.after(3000, error_label.destroy)
            return
            
        # Open results page
        results_page = BusResultsPage(departure, destination, date, gender, bus_type)
        results_page.run()
    
    def on_from_select(self, event):
        if self.from_var.get() == "Departure":
            self.from_combo.set("")
    
    def on_to_select(self, event):
        if self.to_var.get() == "Destination":
            self.to_combo.set("")
    
    def on_date_hover(self, event, widget):
        if not widget['text'].strip():  # Skip empty cells
            return
        widget.configure(background='#f0f0f0')
    
    def on_date_leave(self, event, widget):
        if not widget['text'].strip():  # Skip empty cells
            return
        widget.configure(background=self.bg_color)
    
    def on_date_select(self, event=None):
        selected_date = self.calendar.selection_get()
        self.date_label.configure(text=selected_date.strftime("%B %d, %Y"))  # Display format
        return selected_date.strftime("%Y-%m-%d")  # Return format for searching
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ModernTravelSelector()
    app.run() 