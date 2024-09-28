import matplotlib.pyplot as plt, os, numpy as np

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

salary = 100000
pension_rate = 0.2
pension_yr = salary * pension_rate
years = 40
total_years = np.arange(0,years+1,1)
total_pension = np.arange(0,(pension_yr * (years+1)),pension_yr)

total_gov_pension = []
total_per_tax_pension = []

print("Salary: ", salary); print("Years: ", years); print("Pension per yr: ", pension_yr); print("Total Pension Untaxed: ", total_pension[-1])

plt.figure()
plt.plot(total_years,total_pension,label="Total Pension")
plt.legend(loc="best"); plt.xlabel("Salary",labelpad=0.5); plt.ylabel("Value",labelpad=0.5)
plt.savefig(dir+"/results/images/pension.png",dpi=1000)
plt.close()