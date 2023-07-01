import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("ROI Rental Calculator")
window.geometry("1200x700")
window.grid_columnconfigure((0, 2), weight=1)
window.grid_rowconfigure((0, 2), weight=1)

# Top display
top_display_frame = customtkinter.CTkFrame(window, corner_radius=24, fg_color="#855AE1")
top_display_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

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

other_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#D75FAB",
    height=65,
    width=231,
)
other_expense_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

maintenance_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#F75E7B",
    height=65,
    width=231,
)
maintenance_expense_frame.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

repairs_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#FC729B",
    height=65,
    width=231,
)
repairs_expense_frame.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

total_expense_frame = customtkinter.CTkFrame(
    expense_display_frame,
    corner_radius=24,
    fg_color="#C62A88",
    height=95,
    width=231,
)
total_expense_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

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

window.mainloop()
