class ROI():
    def __init__(self):
        self.total_monthly_income = 0
        self.total_monthly_expenses = 0
        self.total_monthly_cashflow = 0
        self.total_annual_cashflow = 0
        self.total_investment = 0
        self.CoC_return = 0
        
    def monthly_income(self):
        # Income Greeting
        print('\nWelcome to the monthly income section.  Please answer the following questions to the')
        print('best of your ability.  The following information will be used to calculate your')
        print('total monthly income.\n')

        # Income inputs, variables and total monthly income calculation
        self.laundry_income = float(input('Please provide your laundry income (if any): '))
        self.storage_income = float(input('Please provide your storage income (if any): '))
        self.misc_income = float(input('Please provide your miscellaneous income (if any): '))
        self.total_monthly_income = round(self.laundry_income + self.storage_income + self.misc_income, 2)

        # Print out of all the input information to guarantee correctness
        print(f'\nYour laundry income is ${self.laundry_income}, your storage income is ${self.storage_income}')
        print(f'and your miscellaneous income is ${self.misc_income}.')
        print(f'\nYour Total Monthly Income is ${self.total_monthly_income}.')

    def monthly_expenses(self):
        # Expenses Greeting
        print('\nWelcome to the monthly expenses section.  Please answer the following questions to the')
        print('best of your ability.  The following information will be used to calculate your')
        print('total monthly expense.\n')

        # Expenses inputs, variables and total monthly expenses calculation
        self.insurance = float(input('Please provide your insurance expenses (if any): '))
        self.water_sewer = float(input('Please provide your water/sewer expenses (if any): '))
        self.garbage = float(input('Please provide your garbage expenses (if any): '))
        self.electric_gas = float(input('Please provide your electric/gas expenses (if any): '))
        self.HOA_fee = float(input('Please provide your HOA expenses (if any): '))
        self.lawn_snow = float(input('Please provide your lawn/snow expenses (if any): '))
        self.vacancy = float(input('Please provide your vacancy expenses/allowance (if any): '))
        self.repairs = float(input('Please provide your repair expenses/allowance (if any): '))
        self.cap_ex = float(input('Please provide your capital expenditures (if any): '))
        self.prop_mgmt = float(input('Please provide your property management expenditures (if any): '))
        self.mortgage = float(input('Please provide your mortgage expenditures (if any): '))
        self.total_monthly_expenses = round(self.insurance + self.water_sewer + self.garbage + self.electric_gas + self.HOA_fee + self.lawn_snow + self.vacancy + self.repairs + self.cap_ex + self.prop_mgmt + self.mortgage, 2)
                                      
        # Print out of all the expense information to guarantee correctness
        print(f'\nYour insurance expense is ${self.insurance}, your water/sewer expenses are ${self.water_sewer},')
        print(f'your garbage expenses are ${self.garbage}, your electric/gas expenses are ${self.electric_gas},')
        print(f'your HOA expenses are ${self.HOA_fee}, your lawn/snow expenses are ${self.lawn_snow},')
        print(f'your vacancy expense/allowance is {self.vacancy}, your repair expense/allowance is ${self.repairs},')
        print(f'your capital expenditures are ${self.cap_ex}, your property management expenses are ${self.prop_mgmt},')
        print(f'and your mortgage expenses are ${self.mortgage}.')
        print(f'\nTotal Monthly Expenses are: ${self.total_monthly_expenses}.')

    def cashflow(self):
        # Total Monthly Cashflow calculation
        self.total_monthly_cashflow = round(self.total_monthly_income - self.total_monthly_expenses, 2)
        print(f'\nYour Total Monthly Cashflow is: ${self.total_monthly_cashflow}')

        # Total Annual Cashflow calculation
        self.total_annual_cashflow = self.total_monthly_cashflow * 12
        print(f'\nYour Total Annual Cashflow is: ${self.total_annual_cashflow}')
    
    def cashOnCash(self):
        # Cash on Cash intro text
        print('\nWelcome to the cash on cash section.  Please answer the following questions to the')
        print('best of your ability.  The following information will be used to calculate your')
        print('cash on cash return.\n')

        # Cash on Cash variables and inputs
        self.down_payment = float(input('Please provide your down payment amount (if any): '))
        self.closing_cost = float(input('Please provide your closing cost (if any): '))
        self.rehab_budget = float(input('Please provide your rehab budget (if any): '))
        self.other = float(input('Please provide your other costs (if any): '))

        # Print out of all cash on cash information to guarantee correctness
        print(f'\nYour down payment was ${self.down_payment}, your closing costs were ${self.closing_cost},')
        print(f'your rehab budget is ${self.rehab_budget}, and your other costs were ${self.other}.')
        
        # Calculate total investment
        self.total_investment = self.down_payment + self.closing_cost + self.rehab_budget + self.other
        print(f'\nYour total investment is: ${self.total_investment}')

        # Calculate cash on cash return %
        self.CoC_return = (self.total_annual_cashflow / self.total_investment) * 100
        print(f'\nYour cash on cash return percent is: {self.CoC_return}%')

calc_ROI = ROI()

def calculateROI():
    while True:
        response = input('\nWould you like to calculate your ROI (Yes/No)? ')
        
        if response.lower() == 'yes':
            calc_ROI.monthly_income()
            calc_ROI.monthly_expenses()
            calc_ROI.cashflow()
            calc_ROI.cashOnCash()
        
        elif response.lower() =='no':
            print('\nThank you, please come again!')
            break
        
        elif response.lower() != 'yes' or 'no':
            print('\nPlease reply with yes or no.  Thank you very much')

calculateROI()