import customtkinter
from customtkinter import *
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class FrameText:
    label_font = ("inter", 12)
    entry_font = ("inter", 26)
    entry_height = 28
    entry_width = 200
    entry_justify = 'center'
    fg_color = 'transparent'

    def __init__(self, parent_frame, label_text, border_color):
        self.frame = customtkinter.CTkFrame(parent_frame, 
                                            corner_radius=24, 
                                            fg_color='transparent')
        self.frame.pack(padx=10, pady=5, anchor='nw')

        self.label = customtkinter.CTkLabel(self.frame, 
                                            text=label_text, 
                                            text_color="#FFFFFF", 
                                            font=self.label_font, 
                                            fg_color="transparent",
                                            
                                            )
        self.label.pack(anchor='nw')

        self.entry = customtkinter.CTkEntry(self.frame,
                                            fg_color="transparent",
                                            border_color=border_color,
                                            text_color="#ffffff",
                                            font=self.entry_font,
                                            justify=self.entry_justify 
                                        )
        self.entry.pack(padx=10, pady=10)



window = customtkinter.CTk()
window.title("ROI Rental Calculator")
window.geometry("1200x950")
window.grid_columnconfigure((0, 2), weight=1)
window.grid_rowconfigure((0, 2), weight=1)
# window.iconbitmap('/Users/michaelknudson/Documents/Coding Temple/Course/week-3/weekend-project/house-circle-check-solid.ico')


# Top display
top_display_frame = customtkinter.CTkFrame(window, corner_radius=24, fg_color="#855AE1")
top_display_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
top_display_frame.columnconfigure((0,2), weight=1)
top_display_frame.rowconfigure((0,2), weight=1)
top_display_roi_label = customtkinter.CTkLabel(top_display_frame, text="Total ROI:", text_color="#FFFFFF", font=("inter", 48), justify='left', anchor='sw')
top_display_roi_label.grid(row=2, column=0, columnspan=2, padx=(0,50))
# logo_img = customtkinter.CTkImage(logo_img=Image.open("/Users/michaelknudson/Documents/Coding Temple/Course/week-3/weekend-project/house-circle-check-solid.svg"))


# Income column
income_display_frame = customtkinter.CTkFrame(window, corner_radius=24, fg_color="transparent")
income_display_frame.grid(row=1, column=0, rowspan=2, pady=20, sticky="nsew")
income_display_frame.columnconfigure(0, weight=1)

income_label = customtkinter.CTkLabel(income_display_frame, text="Income", text_color="#FFFFFF", font=("inter", 32))
income_label.grid(row=0, column = 0, pady=(0,20))

# income frames w/in income_display_frame
rental_income_frame = customtkinter.CTkFrame(
    income_display_frame,
    corner_radius=24,
    fg_color="#0A4D68",
    height=65,
    width=231,
)
rental_income_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
rental_income_entry_label = customtkinter.CTkLabel(
    rental_income_frame, 
    text="Monthly Rental Income", 
    text_color="#FFFFFF", 
    font=("inter", 12), 
    fg_color="transparent"
    )
rental_income_entry_label.pack(padx=22, anchor ='nw')

rental_income_entry = customtkinter.CTkEntry(
    rental_income_frame,  
    fg_color="transparent",
    height=28, 
    width=184, 
    border_color="#0A4D68", 
    text_color="#ffffff", 
    font=("inter", 26),
    justify='center'
    )
rental_income_entry.pack(padx=10, pady=10)

fees_income_frame = customtkinter.CTkFrame(
    income_display_frame,
    corner_radius=24,
    fg_color="#088395",
    height=65,
    width=231,
)
fees_income_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

other_income_frame = customtkinter.CTkFrame(
    income_display_frame,
    corner_radius=24,
    fg_color="#05BFDB",
    height=65,
    width=231,
)
other_income_frame.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

total_income_frame = customtkinter.CTkFrame(
    income_display_frame,
    corner_radius=24,
    fg_color="#04A583",
    height=95,
    width=231,
)
total_income_frame.grid(row=4, column=0, padx=10, pady=(20, 10), sticky="nsew")
total_income_entry_label = customtkinter.CTkLabel(
    total_income_frame, 
    text="Total Income", 
    text_color="#FFFFFF", 
    font=("inter", 12), 
    fg_color="transparent"
    )
total_income_entry_label.pack(padx=22, anchor ='nw')


# Expenses column
expense_display_frame = customtkinter.CTkFrame(window, corner_radius=24, fg_color="transparent")
expense_display_frame.grid(row=1, column=1, rowspan=2, padx=20, pady=20, sticky="nsew")
expense_display_frame.columnconfigure(0, weight=1)
expense_display_frame.rowconfigure((0, 1, 2), weight=1)

expense_label = customtkinter.CTkLabel(expense_display_frame, text="Expenses", text_color="#FFFFFF", font=("inter", 32))
expense_label.grid(row=0, column = 0, columnspan=2, pady=(0,20))

taxes_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#FF5F91",
    height=65,
    width=231,
)
taxes_expense_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

insurance_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#A267AC",
    height=65,
    width=231,
)
insurance_expense_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

utilities_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#CE7BB0",
    height=65,
    width=231,
)
utilities_expense_frame.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

repairs_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#D75FAB",
    height=65,
    width=231,
)
repairs_expense_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

mortgage_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#F75E7B",
    height=65,
    width=231,
)
mortgage_expense_frame.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

other_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#FC729B",
    height=65,
    width=231,
)
other_expense_frame.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

total_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#C62A88",
    height=95,
    width=231,
)
total_expense_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

total_expense_entry_label = customtkinter.CTkLabel(
    total_expense_frame, 
    text="Total Expenses", 
    text_color="#FFFFFF", 
    font=("inter", 12), 
    fg_color="transparent"
    )
total_expense_entry_label.pack(padx=22, anchor ='nw')


# Investments column
investment_display_frame = customtkinter.CTkFrame(window, corner_radius=24, fg_color="transparent")
investment_display_frame.grid(row=1, column=2, rowspan=2, padx=20, pady=20, sticky="nsew")
investment_display_frame.columnconfigure(0, weight=1)

investment_label = customtkinter.CTkLabel(investment_display_frame, text="Investment", text_color="#FFFFFF", font=("inter", 32))
investment_label.grid(row=0, column = 0, columnspan=2, pady=(0,20))

dwnpymt_investment_frame = customtkinter.CTkFrame(
    investment_display_frame,
    corner_radius=24,
    fg_color="#DAB88B",
    height=65,
    width=231,
)
dwnpymt_investment_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

closing_investment_frame = customtkinter.CTkFrame(
    investment_display_frame,
    corner_radius=24,
    fg_color="#C3AF96",
    height=65,
    width=231,
)
closing_investment_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

other_investment_frame = customtkinter.CTkFrame(
    investment_display_frame,
    corner_radius=24,
    fg_color="#F9B95F",
    height=65,
    width=231,
)
other_investment_frame.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

total_investment_frame = customtkinter.CTkFrame(
    investment_display_frame,
    corner_radius=24,
    fg_color="#E4941B",
    height=95,
    width=231,
)
total_investment_frame.grid(row=4, column=0, padx=10, pady=(20, 10), sticky="nsew")
total_investment_entry_label = customtkinter.CTkLabel(
    total_investment_frame, 
    text="Total Investment", 
    text_color="#FFFFFF", 
    font=("inter", 12), 
    fg_color="transparent"
    )
total_investment_entry_label.pack(padx=22, anchor ='nw')


fees_income_text_frame = FrameText(fees_income_frame, "Monthly Fees, etc.", '#088395')
other_income_text_frame = FrameText(other_income_frame, "Other Income", '#05BFDB')

taxes_expense_text_frame = FrameText(taxes_expense_frame, "Taxes", '#FF5F91')
insurance_expense_text_frame = FrameText(insurance_expense_frame, "Insurance", '#A267AC')
utilities_expense_text_frame = FrameText(utilities_expense_frame, "Utilities", '#CE7BB0')
repairs_expense_text_frame = FrameText(repairs_expense_frame, "Repairs", '#D75FAB')
mortgage_expense_text_frame = FrameText(mortgage_expense_frame, "Mortgage", '#F75E7B')
other_expense_text_frame = FrameText(other_expense_frame, "Other Expenses", '#FC729B')

dwnpymt_investment_text_frame = FrameText(dwnpymt_investment_frame, "Down Payment", '#DAB88B')
closing_investment_text_frame = FrameText(closing_investment_frame, "Closing Costs", '#C3AF96')
other_investment_text_frame = FrameText(other_investment_frame, "Repairs, etc.", '#F9B95F')


window.mainloop()
