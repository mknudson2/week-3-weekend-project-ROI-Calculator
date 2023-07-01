class RentalROI:
    
    def __init__(self):
        self.income_value = 0
        self.expenses_value = 0
        self.investment_value = 0
        self.cash_flow = 0
        self.annual_cash_flow = 0
        self.total_investment = 0
    
    def new_reset(self):
        self.income_value = 0
        self.expenses_value = 0
        self.investment_value = 0
        self.cash_flow = 0
        self.annual_cash_flow = 0
        self.total_investment = 0
    
    def numerical_input(self, user_input):
        while True:
            try:
                value = float(input(user_input))
                return value
            except ValueError:
                print('Please enter a valid numerical value.')
    
    def income(self):
        if self.income_value == 0:
            print('First, what is your expected monthly income?')
            user_rental_income = self.numerical_input('Monthly Rental Income: $')
            user_other_income = self.numerical_input('Other Monthly Income: $')
            income = user_rental_income + user_other_income
            print('\n')
            print(f'Your total monthly income is ${income}')
            self.income_value = income
        else:
            print(f'Your previous income information: ${self.income_value}.')
            user_income_choice = input('Are you sure you want to change the income information? [y/n] ').lower()
            if user_income_choice == 'y':
                print('\nAlright, what is your updated expected monthly income?')
                user_rental_income = self.numerical_input('Monthly Rental Income: $')
                user_other_income = self.numerical_input('Other Monthly Income: $')
                income = user_rental_income + user_other_income
                print('\n')
                print(f'Your updated total monthly income is ${income}')
                self.income_value = income
            elif user_income_choice == 'n':
                print("We'll keep using previous income information.")
                print('\n')
            else:
                print('Please enter a valid response: [y/n]')
        
        return self.income_value

    def expenses(self):
        if self.expenses_value == 0:
            print('\nNow, what are your expected monthly expenses?')
            print('If a condition does not apply to you, or if it will be covered by the tenant, please enter 0.\n')
            user_property_taxes = self.numerical_input('Estimated Property Taxes: $')
            user_property_insurance = self.numerical_input('Estimated Property Insurance: $')
            user_property_utilities = self.numerical_input('Monthly Utilities: $')
            user_property_hoa = self.numerical_input('Monthy HOA Fees: $')
            user_property_outdoor = self.numerical_input('Monthly Lawncare / Snow Removal: $')
            user_property_vacancy = self.numerical_input('Monthy Vacancy Savings: $')
            user_property_repairs = self.numerical_input('Monthy Repairs Savings: $')
            user_property_capex = self.numerical_input('Monthy Capital Expenditure Savings: $')
            user_property_management = self.numerical_input('Monthy Property Management Fees: $')
            user_property_mortgage = self.numerical_input('Monthy Mortgage: $')
            user_property_other = self.numerical_input('Other Monthly Expenses: $')
            expenses = (
                user_property_taxes + user_property_insurance + user_property_utilities +
                user_property_hoa + user_property_outdoor + user_property_vacancy +
                user_property_repairs + user_property_capex + user_property_management +
                user_property_mortgage + user_property_other
            )
            print(f'Your total monthly expenses are ${expenses}')
            print('\n')
            self.expenses_value = expenses
        else:
            print(f'Your previous expenses information: ${self.expenses_value}.')
            user_choice = input('Do you want to change the expenses information? [y/n] ').lower()
            if user_choice == 'y':
                user_property_taxes = self.numerical_input('Estimated Property Taxes: $')
                user_property_insurance = self.numerical_input('Estimated Property Insurance: $')
                user_property_utilities = self.numerical_input('Monthly Utilities: $')
                user_property_hoa = self.numerical_input('Monthy HOA Fees: $')
                user_property_outdoor = self.numerical_input('Monthly Lawncare / Snow Removal: $')
                user_property_vacancy = self.numerical_input('Monthy Vacancy Savings: $')
                user_property_repairs = self.numerical_input('Monthy Repairs Savings: $')
                user_property_capex = self.numerical_input('Monthy Capital Expenditure Savings: $')
                user_property_management = self.numerical_input('Monthy Property Management Fees: $')
                user_property_mortgage = self.numerical_input('Monthy Mortgage: $')
                user_property_other = self.numerical_input('Other Monthly Expenses: $')
                expenses = (
                    user_property_taxes + user_property_insurance + user_property_utilities +
                    user_property_hoa + user_property_outdoor + user_property_vacancy +
                    user_property_repairs + user_property_capex + user_property_management +
                    user_property_mortgage + user_property_other
                )
                print(f'Your updated total monthly expenses are ${expenses}')
                self.expenses_value = expenses
            elif user_choice == 'n':
                print("We'll keep using previous expenses information.")
                print('\n')
            else:
                print('Please enter a valid response: [y/n]')
        return self.expenses_value

    def monthly_cash_flow(self, income, expenses):
        self.cash_flow = income - expenses
        self.annual_cash_flow = self.cash_flow * 12
        if self.cash_flow > 0:
            print(f'Congratulations! You have a positive cash flow. You are earning ${self.cash_flow}/month on this property. This investment seems to be worth consideration.')
            print('\n')
        else:
            print(f"I'm sorry, you have a negative cash flow. You are losing ${self.cash_flow}/month on this property. You may want to consider a different investment or make other changes that would either lower your expenses or increase you income.")
            print('\n')
        return self.cash_flow

    def investment(self):
        if self.investment_value == 0:
            print('Lastly, please enter your total expected investment into the property.\n')
            user_investment_downpayment = self.numerical_input('Down Payment: $')
            user_investment_closing = self.numerical_input('Closing Costs: $')
            user_investment_repairs = self.numerical_input('Repairs Costs: $')
            user_investment_other = self.numerical_input('Other: $')
            self.total_investment = (
                user_investment_downpayment + user_investment_closing +
                user_investment_repairs + user_investment_other
                )
            print(f'Your total investment into the property is ${self.total_investment}.')
            print('\n')
            self.investment_value = self.total_investment
        else:
            print(f'Your previous investment information: ${self.investment_value}.')
            user_choice = input('Are you sure you want to change the investment information? [y/n] ').lower()
            if user_choice == 'y':
                print('\nAlright, what are your updated investment costs?')
                user_investment_downpayment = self.numerical_input('Down Payment: $')
                user_investment_closing = self.numerical_input('Closing Costs: $')
                user_investment_repairs = self.numerical_input('Repairs Costs: $')
                user_investment_other = self.numerical_input('Other: $')
                self.total_investment = (
                    user_investment_downpayment + user_investment_closing +
                    user_investment_repairs + user_investment_other
                )
                print('')
                print(f'Your updated total investment into the property is ${self.total_investment}.')
                print('\n')
                self.investment_value = self.total_investment
            elif user_choice == 'n':
                print('')
                print("We'll keep using your previous investment information.")
                print('\n')
            else:
                print('Please enter a valid response: [y/n]')
        return self.total_investment
        
    def roi(self):
        user_roi = (self.annual_cash_flow / self.total_investment) * 100
        print(f'Based on the information given, your Cash-on-Cash ROI for the property is {user_roi:.2f}%.')
        print('\n')


    def end_choice(self):
        while True:
            user_choice = input('Would you like to change any values, evaluate a new property, or are you done? [change/new/done] ').lower()
            if user_choice == "change":
                user_change_prompt = input('What would you like to change? \nIncome | Expenses | Investments | Back\n').lower()
                if user_change_prompt == "income":
                    income = self.income()  # Update income information
                    self.monthly_cash_flow(income, self.expenses_value)
                    self.roi()  # Recalculate ROI using existing total investment
                elif user_change_prompt == "expenses":
                    expenses = self.expenses()  # Update expenses information
                    self.monthly_cash_flow(self.income_value, expenses)  # Recalculate monthly cash flow using existing income
                    self.roi()  # Recalculate ROI using existing total investment
                elif user_change_prompt == "investments":
                    self.investment()  # Update investment information
                    self.roi()  # Recalculate ROI
                elif user_change_prompt == "back":
                    self.end_choice()  # Go back to the previous menu
                else:
                    print('Sorry, please check your spelling or enter a valid response: Income/Expenses/Investment or back')
            elif user_choice == "new":
                self.new_reset() # Resets the values so the user can start fresh
                self.driver()  # Start a new evaluation
            elif user_choice == "done":
                print('')
                print('Thank you for using our calculator! I hope you have a good day. \n Happy Investing!')
                break

    def driver(self):
        print('\n')
        print("Hello! Let's figure out the return on investment (ROI) for your rental property.\n")
        income = self.income()
        expenses = self.expenses()
        self.cash_flow = self.monthly_cash_flow(income, expenses)
        self.investment()  # Update the total investment value
        self.annual_cash_flow = self.cash_flow * 12  # Calculate annual cash flow
        self.roi()  # Pass the actual cash flow and total investment
        self.end_choice()

roi_calculator = RentalROI()
roi_calculator.driver()
