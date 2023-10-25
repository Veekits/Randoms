#!/usr/bin/env python
# coding: utf-8

# In[2]:

#This code is used to calculate the new tax rates as of July 2023
def calculate_tax(taxable_income, deduction):
    tax_bands = [
        (24000, 0.10),
        (8333, 0.25),
        (467667, 0.30),
        (300000, 0.325),
        (float('inf'), 0.35)
    ]
    personal_relief = 2400

    total_tax = 0

    for band_income, tax_rate in tax_bands:
        if taxable_income <= 0:
            break
        if taxable_income <= band_income:
            total_tax += taxable_income * tax_rate
            break
        else:
            total_tax += band_income * tax_rate
        taxable_income -= band_income

    # Calculate tax payable
    tax_payable = total_tax - personal_relief - (deduction * 0.15)

    return tax_payable

def kenya_tax_calculator(income):
    NSSF = 1080
    taxable_income = income - NSSF

    # Calculate tax payable within the kenya_tax_calculator function
    tax_payable = calculate_tax(taxable_income, deduction)
    PAYE = taxable_income - tax_payable  # Calculate PAYE
    
    # Return the taxable income, tax payable, and PAYE
    return taxable_income, tax_payable, PAYE
    
def NHIF_rates(income):
    NHIF_bands = [    
        (0,5999,150),
        (6000, 7999, 300), 
        (8000, 11999, 400),
        (12000, 14999, 500),
        (15000, 19999, 600),
        (20000, 24999, 750), 
        (25000, 29999, 850), 
        (30000, 34999, 900), 
        (35000, 39999, 950), 
        (40000, 44999, 1000), 
        (45000, 49999, 1100), 
        (50000, 59999, 1200), 
        (60000, 69999, 1300), 
        (70000, 79999, 1400), 
        (80000, 89999, 1500), 
        (90000, 99999, 1600), 
        (100000, float('inf'), 1700)
    ]
    
    exc_NHIF = 0
    deduction = 0
    for lower_band, higher_band, deduction in NHIF_bands:
        if income >= lower_band and income <= higher_band:
            exc_NHIF = income - deduction
            break
    return income, exc_NHIF, deduction

income = int(input("Enter your gross pay (basic plus allowances) in KES: "))

income, exc_NHIF, deduction = NHIF_rates(income)

taxable_income, tax_payable, PAYE = kenya_tax_calculator(income)

tax_payable = calculate_tax(taxable_income, deduction)

housing_levy = income * 0.015
NET_pay = PAYE - deduction - housing_levy

# Print the results
print("\nNSSF:", 1080)
print("\nTaxable Income:", taxable_income)
print(f"\nTotal tax: {tax_payable:.2f}")
print(f"\nYour P.A.Y.E is KES: {PAYE:.2f}")
print("\nYour NHIF deduction:", deduction)
print("\nYour housing levy:", housing_levy)
print("\nYOUR NET PAY:", NET_pay)

if NET_pay <= 100000:
    print("Na unastrugleeee")
else:
    print("Mungu abariki wengine sasa")


# In[ ]:




