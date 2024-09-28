salary = 80000.00

# Tax Brackets
tax_free = 12571.00
low_tax = 50271.00
high_tax = 125141.00

tax_free_mon = 12571.00/12
low_tax_mon = 50271.00/12
high_tax_mon = 125141.00/12

# National Insurance Calculations
ni_con = salary/12
if ni_con < tax_free_mon:
    ni = 0.00
elif (ni_con >= tax_free_mon) and (ni_con < low_tax_mon):
    ni = (ni_con-tax_free_mon)* 0.1 
elif (ni_con >= low_tax_mon) and (ni_con < high_tax_mon):
    ni = ((ni_con-low_tax_mon) * 0.02) + (((ni_con-(ni_con-low_tax_mon))-tax_free_mon) * 0.1)
ni = ni*12

'''
# UK Income Tax Calculations
tax_pay = salary - tax_free
if salary <= tax_free:
    taxed = 0.00
elif (salary > tax_free+1.00) and (salary <= low_tax):
    taxed = (salary-tax_free)* 0.2
elif (salary >= low_tax+1.00) and (salary <= high_tax):
    taxed = ((salary-low_tax) * 0.4) + (((salary-(salary-low_tax))-tax_free) * 0.2)
elif (salary >= high_tax+1.00):
    taxed = ((salary-high_tax) * 0.45) + (((salary-(salary-high_tax))-low_tax) * 0.4) + ((((salary-(salary-high_tax))-(salary-(salary-low_tax))-tax_free)) * 0.2)

'''

print(salary, ni)
# Print Results
#print(" Salary: ", salary,"\n Total Tax: ", total_tax, "\n NI: ", ni,"\n Take Home: ", th_pay,"\n Total Loss:", loss, "\n Monthly Pay: ", th_monthly, tax_monthly)