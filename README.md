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