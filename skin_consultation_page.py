import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import Text, END
import cohere  # Import Cohere

class SkinConsultationPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="white")
        self.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header = ctk.CTkLabel(
            self, 
            text="Skin Consultation", 
            font=("Helvetica", 24, "bold"),
            text_color="black"
        )
        self.header.pack(pady=(20,10), padx=20, anchor='w')
        
        # Main content in scrollable frame
        self.content = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.content.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Form elements
        self.create_form_elements()
        
        # Submit button
        self.submit_btn = ctk.CTkButton(
            self,
            text="Submit Consultation",
            height=50,
            corner_radius=25,
            fg_color="#FF9F67",
            hover_color="#FF8B4D",
            command=self.submit_consultation
        )
        self.submit_btn.pack(pady=20, padx=20, fill=tk.X)

        # Add response text box at the bottom
        self.response_label = ctk.CTkLabel(
            self,
            text="AI Doctor's Recommendation:",
            font=("Helvetica", 16, "bold"),
            text_color="black"
        )
        self.response_label.pack(pady=(20,5), padx=20, anchor='w')

        self.response_text = Text(
            self,
            wrap=tk.WORD,
            height=10,
            width=50,
            font=("Helvetica", 12),
            bg="#F5F5F5",
            fg="black"
        )
        self.response_text.pack(pady=(0,20), padx=20, fill=tk.X)

    def create_form_elements(self):
        # Age field
        self.create_section_label("Age")
        self.age_entry = self.create_entry_field("Enter your age")
        
        # Skin type selection
        self.create_section_label("Skin Type")
        self.skin_type_var = tk.StringVar(value="Normal")
        skin_types = ["Normal", "Dry", "Oily", "Combination", "Sensitive"]
        self.create_radio_group(skin_types, self.skin_type_var)
        
        # Main concern selection
        self.create_section_label("Main Concern")
        concerns = ["Acne", "Aging", "Pigmentation", "Redness", "Dryness"]
        self.concern_vars = {}
        self.create_checkbox_group(concerns)
        
        # Duration of problem
        self.create_section_label("How long have you had this condition?")
        self.duration_entry = self.create_entry_field("e.g., 2 weeks, 3 months")
        
        # Previous treatments
        self.create_section_label("Previous Treatments (if any)")
        self.treatments_entry = self.create_text_area("List any treatments you've tried...")
        
        # Allergies
        self.create_section_label("Known Allergies")
        self.allergies_entry = self.create_text_area("List any allergies...")
        
        # Current medications
        self.create_section_label("Current Medications")
        self.medications_entry = self.create_text_area("List any medications...")
        
        # Additional notes
        self.create_section_label("Additional Notes")
        self.notes_entry = self.create_text_area("Any other information you'd like to share...")

    def create_section_label(self, text):
        label = ctk.CTkLabel(
            self.content,
            text=text,
            font=("Helvetica", 16, "bold"),
            text_color="black"
        )
        label.pack(anchor='w', pady=(15,5))

    def create_radio_group(self, options, variable):
        frame = ctk.CTkFrame(self.content, fg_color="transparent")
        frame.pack(fill=tk.X, pady=5)
        
        for option in options:
            radio = ctk.CTkRadioButton(
                frame,
                text=option,
                variable=variable,
                value=option,
                fg_color="#FF9F67",
                border_color="#FF9F67"
            )
            radio.pack(side=tk.LEFT, padx=10)

    def create_checkbox_group(self, options):
        frame = ctk.CTkFrame(self.content, fg_color="transparent")
        frame.pack(fill=tk.X, pady=5)
        
        for option in options:
            var = tk.BooleanVar()
            self.concern_vars[option] = var
            checkbox = ctk.CTkCheckBox(
                frame,
                text=option,
                variable=var,
                fg_color="#FF9F67",
                hover_color="#FF8B4D",
                border_color="#FF9F67"
            )
            checkbox.pack(side=tk.LEFT, padx=10)

    def create_entry_field(self, placeholder):
        entry = ctk.CTkEntry(
            self.content,
            placeholder_text=placeholder,
            height=40,
            corner_radius=10,
            border_color="#E0E0E0",
            fg_color="#F5F5F5"
        )
        entry.pack(fill=tk.X, pady=5)
        return entry

    def create_text_area(self, placeholder):
        text_area = ctk.CTkTextbox(
            self.content,
            height=80,
            corner_radius=10,
            border_color="#E0E0E0",
            fg_color="#F5F5F5"
        )
        text_area.pack(fill=tk.X, pady=5)
        text_area.insert("1.0", placeholder)
        text_area.bind("<FocusIn>", lambda e: self.clear_placeholder(text_area, placeholder))
        text_area.bind("<FocusOut>", lambda e: self.restore_placeholder(text_area, placeholder))
        return text_area

    def clear_placeholder(self, widget, placeholder):
        if widget.get("1.0", "end-1c") == placeholder:
            widget.delete("1.0", tk.END)

    def restore_placeholder(self, widget, placeholder):
        if not widget.get("1.0", "end-1c").strip():
            widget.delete("1.0", tk.END)
            widget.insert("1.0", placeholder)

    def get_ai_consultation(self, user_inputs):
        try:
            # Initialize the Cohere client with the correct API key
            co = cohere.Client("W6jMlPJCOXkjsh1R71fayjnNrSyKEexCtjoyEXHT")
            
            prompt = f"""As a dermatologist, please provide skincare recommendations based on the following information:
            Age: {user_inputs['age']}
            Skin Type: {user_inputs['skin_type']}
            Main Concerns: {user_inputs['concerns']}
            Duration of Condition: {user_inputs['duration']}
            Previous Treatments: {user_inputs['treatments']}
            Allergies: {user_inputs['allergies']}
            Current Medications: {user_inputs['medications']}
            Additional Notes: {user_inputs['notes']}
            
            Please provide specific recommendations for skincare routine and products."""

            response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=300
            )
            
            # Access the response content directly
            return response.generations[0].text
        except Exception as e:
            print(f"Error calling Cohere API: {e}")
            return "Sorry, there was an error getting the AI consultation. Please try again."

    def submit_consultation(self):
        # Get selected concerns
        selected_concerns = [
            concern for concern, var in self.concern_vars.items() 
            if var.get()
        ]

        # Collect all the user inputs
        user_inputs = {
            'age': self.age_entry.get(),
            'skin_type': self.skin_type_var.get(),
            'concerns': ", ".join(selected_concerns),
            'duration': self.duration_entry.get(),
            'treatments': self.treatments_entry.get("1.0", tk.END).strip(),
            'allergies': self.allergies_entry.get("1.0", tk.END).strip(),
            'medications': self.medications_entry.get("1.0", tk.END).strip(),
            'notes': self.notes_entry.get("1.0", tk.END).strip()
        }

        # Get AI response
        ai_response = self.get_ai_consultation(user_inputs)
        
        # Print to terminal
        print("AI Doctor's Response:")
        print(ai_response)
        
        # Update response text box
        self.response_text.delete(1.0, END)
        self.response_text.insert(1.0, ai_response) 