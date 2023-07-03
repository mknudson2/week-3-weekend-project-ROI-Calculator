The purpose of this program is to create an app that will show the user the ROI percentage upon filling out the necessary information:
    1. Monthly Income
    2. Monthly Expenses
    3. Investment costs (down-payment, closing costs, repairs/rehab, etc.)
    
In turn, the calculator will show them:
    a. Monthly Cashflow (Income - Expenses)
    b. Cash-on-Cash ROI Percentage (the percentage of the return on what they have invested into the property)
    
Ideally, it would also pull in information from Zillow, allowing the user to gain additional data related to the desired area.
Things that it can include could be:
    I. the Zestimate (i.e., Zillow's best estimate of the home's market value, this takes into account factors like neighborhood details, home fact, listing price, etc.)
    II. estimated mortgage rate
    III. Monthly cost estimates
        i. principal and interest
        ii. mortage insurance
        iii. property taxes
        iv. home insurance
        v. HOA fees
        vi. utilities
    IV. Zillow's Rental Estimate (Rent Zestimate)
    V. Information about local schools (if desired)
    VI. Neighborhood Score

Lastly, it would be ideal to turn this into an accessible, user-friendly package by having a GUI that the user can easily access, input information, and view the results. This would require some extra work, but Tkinter + JS might work, or we could explore other GUIs.

Steps:
1. Create a program that performs the necessary calculations to produce the ROI while checking validation and error handling.
2. Incorporate Zillow API to access the necessary data
3. Lay out our GUI with the desired look, feel, needs, and features that we want to incorporate
4. Build the GUI and test

##############

35. Establish a class to house the ROI Calculator functionality

37. Setting universal attributes for the class, which becomes especially important as the user has the option to update their input data. This took time to get right, since I wanted the user to be able to access their previous data to update it and then recalculate the ROI based off their new input with respect to what they had previously entered (i.e., they could alter the income info without needing to re-enter expense and investment info too).
38. Attribute for total income calculation, used especially in updating information since it checks if the value is 0 (i.e., no info has been input), which determines the path of the income method (lins 61-87). This also holds the total income info as a variable to be recalled.
39. Attribute for total expense calculation, used especially in updating information since it checks if the value is 0 (i.e., no info has been input), which determines the path of the income method (lins 89-141). This also holds the total income info as a variable to be recalled.
40. Attribute for investment calculation, used especially in updating information since it checks if the value is 0 (i.e., no info has been input), which determines the path of the investment method (lins 154-91)
41. Attribute for cash flow calculation (income - expense = month cash flow)
42. Attribute for total annual cash flow calculation (cash flow * 12)
43. Attribute for total investment calculation


NEW_RESET METHOD (lines 45-51)
Provides default values of 0 for each attribute so that if the user chooses to start a new calculation that all previous data is cleared and does not interfere with the new input. Lines 46-51 respectively correspond to each value stored in the calculator.


NUMERICAL_INPUT METHOD (lines 53-59)
A method to specifically handle the ValueError that would occur should a user not input a numerical value where required. 

53. Sets up the method, requiring the arguments of self and user_input.
54. Utilizes a while loop to check through input and allow it to continue until the requirements are checked, otherwise the program would stop once the Error was reached and the user would not have a chance to reconcile it.
55 / 58. Utilizes try and except to 1) look for the specific error and 2) allow the program to keep running should the error be found instead of simply breaking.
56. Assign the user_input to a value while ensuring that the input will be converted to a float, allowing for decimal places to be used with regards to monetary values.
57. The value is returned when successful
59. Upon finding the ValueError specified in line 58, the user is prompted to re-enter a valid input. Since this is found under the while loop, the user is subsequently prompted to enter a numerical value, which pattern will continue until True.


#Note that the income, expenses, and investment methods all have the same pattern as one another. Each is set up to both take in information as well as to go back and alter it should the user choose “change”. The following pattern applies to all three methods:
A conditional if statement is introduced to check whether the initial amount of the respective variables (self.income_value, etc.) are set to 0. If they are, which means this is the first time the user is going through, the user is led through a series of prompts that ask for the given information. 
If the conditional statement is not True, then the user has a different set of prompts to, first, show them their current input totals and ask for confirmation that they want to change. 
Each input option is set to the NUMERICAL_INPUT method to ensure that a float is received.
All values are stored in the previously named class attributes so they can be accessible and altered without needing to revisit all the prompts from all sections again.

MONTHLY_CASH_FLOW METHOD (lines 142-51)
142. Defines the method taking in self, income, and expenses
143. Sets the attribute to the calculation of 
