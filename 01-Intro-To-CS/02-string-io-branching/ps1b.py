import math

# User inputs
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Constants
portion_down_payment = 0.25
r = 0.05  # Annual return rate
monthly_return = r / 12  # Monthly interest rate

# Calculate required down payment
down_payment = portion_down_payment * cost_of_dream_home

# First 6 months
monthly_salary = yearly_salary / 12
monthly_savings = monthly_salary * portion_saved
savings_6_months = (monthly_savings * ((1 + monthly_return) ** 6 - 1) / monthly_return)

# If goal is reached in first 6 months
if savings_6_months >= down_payment:
    months = math.ceil(math.log(1 + (monthly_return * (down_payment / monthly_savings))) / math.log(1 + monthly_return))
else:
    # Second 6 months (after salary increase)
    yearly_salary *= (1 + semi_annual_raise)
    monthly_salary = yearly_salary / 12
    monthly_savings = monthly_salary * portion_saved
    savings_12_months = savings_6_months + (monthly_savings * ((1 + monthly_return) ** 6 - 1) / monthly_return)

    # If goal is reached in second 6-month period
    if savings_12_months >= down_payment:
        remaining_needed = down_payment - savings_6_months
        extra_months = math.log(1 + (monthly_return * (remaining_needed / monthly_savings))) / math.log(1 + monthly_return)
        months = 6 + math.ceil(extra_months)
    else:
        # Third 6 months (after another salary increase)
        yearly_salary *= (1 + semi_annual_raise)
        monthly_salary = yearly_salary / 12
        monthly_savings = monthly_salary * portion_saved
        savings_18_months = savings_12_months + (monthly_savings * ((1 + monthly_return) ** 6 - 1) / monthly_return)

        # If goal is reached in third 6-month period
        if savings_18_months >= down_payment:
            remaining_needed = down_payment - savings_12_months
            extra_months = math.log(1 + (monthly_return * (remaining_needed / monthly_savings))) / math.log(1 + monthly_return)
            months = 12 + math.ceil(extra_months)
        else:
            # Fourth 6 months (another salary increase)
            yearly_salary *= (1 + semi_annual_raise)
            monthly_salary = yearly_salary / 12
            monthly_savings = monthly_salary * portion_saved
            savings_24_months = savings_18_months + (monthly_savings * ((1 + monthly_return) ** 6 - 1) / monthly_return)

            # If goal is reached in fourth 6-month period
            if savings_24_months >= down_payment:
                remaining_needed = down_payment - savings_18_months
                extra_months = math.log(1 + (monthly_return * (remaining_needed / monthly_savings))) / math.log(1 + monthly_return)
                months = 18 + math.ceil(extra_months)
            else:
                # Fifth 6 months (another salary increase)
                yearly_salary *= (1 + semi_annual_raise)
                monthly_salary = yearly_salary / 12
                monthly_savings = monthly_salary * portion_saved
                savings_30_months = savings_24_months + (monthly_savings * ((1 + monthly_return) ** 6 - 1) / monthly_return)

                # If goal is reached in fifth 6-month period
                if savings_30_months >= down_payment:
                    remaining_needed = down_payment - savings_24_months
                    extra_months = math.log(1 + (monthly_return * (remaining_needed / monthly_savings))) / math.log(1 + monthly_return)
                    months = 24 + math.ceil(extra_months)
                else:
                    # Sixth 6 months (another salary increase)
                    yearly_salary *= (1 + semi_annual_raise)
                    monthly_salary = yearly_salary / 12
                    monthly_savings = monthly_salary * portion_saved
                    savings_36_months = savings_30_months + (monthly_savings * ((1 + monthly_return) ** 6 - 1) / monthly_return)

                    # If goal is reached in sixth 6-month period
                    if savings_36_months >= down_payment:
                        remaining_needed = down_payment - savings_30_months
                        extra_months = math.log(1 + (monthly_return * (remaining_needed / monthly_savings))) / math.log(1 + monthly_return)
                        months = 30 + math.ceil(extra_months)
                    else:
                        months = 36  # Extend further if needed

print(f"Number of months: {months}")
