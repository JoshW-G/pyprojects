<<<<<<< HEAD
per = str.upper(input("Is your pay Weekly, Monthly or yearly? W/M/Y "))
per = 'week' if per=='W' else 'month' if per=='M' else 'year'
perCost = int(input("Salary per {}? ".format(per)))
sal = perCost*52 if per=='week' else perCost*12 if per=='month' else perCost
print("\nYour salary is £{} per year\n".format(sal))

per = str.upper(input("Is your rent Weekly or Monthly? (N to skip) W/M "))
pa= 12570 #personal allowance
if per!="N":
    per = 'week' if per=='W' else 'month'
    perCost = int(input("Cost per {}? ".format(per)))
    rent = perCost*52 if per=='week' else perCost*12
    print("\nYour rent is £{} per year".format(rent))
    for i in range(2):
        r = sal-rent
        print("\nMinus your rent (£{}), you will have £{}".format(rent,r))
        print("\nBreakdown\nThats £{:.2f} per month and £{:.2f} per week (£{:.2f} per day)\n".format(r/12,r/52,(r/52)/7))
        
        if i == 0:
            print("\nNow minus income tax:\n")
            tax = 0 if sal<=pa else (sal-pa)*0.4 if (sal-pa)>50270 else sal*0.2
            sal = sal-tax
            print("Remaning income after tax (£{}): £{}".format(tax,sal))
else:
    print("\nNow minus income tax:\n")
    tax = 0 if sal<=pa else (sal-pa)*0.4 if (sal-pa)>50270 else sal*0.2
    sal = sal-tax
=======
per = str.upper(input("Is your pay Weekly, Monthly or yearly? W/M/Y "))
per = 'week' if per=='W' else 'month' if per=='M' else 'year'
perCost = int(input("Salary per {}? ".format(per)))
sal = perCost*52 if per=='week' else perCost*12 if per=='month' else perCost
print("\nYour salary is £{} per year\n".format(sal))

per = str.upper(input("Is your rent Weekly or Monthly? (N to skip) W/M "))
pa= 12570 #personal allowance
if per!="N":
    per = 'week' if per=='W' else 'month'
    perCost = int(input("Cost per {}? ".format(per)))
    rent = perCost*52 if per=='week' else perCost*12
    print("\nYour rent is £{} per year".format(rent))
    for i in range(2):
        r = sal-rent
        print("\nMinus your rent (£{}), you will have £{}".format(rent,r))
        print("\nBreakdown\nThats £{:.2f} per month and £{:.2f} per week (£{:.2f} per day)\n".format(r/12,r/52,(r/52)/7))
        
        if i == 0:
            print("\nNow minus income tax:\n")
            tax = 0 if sal<=pa else (sal-pa)*0.4 if (sal-pa)>50270 else sal*0.2
            sal = sal-tax
            print("Remaning income after tax (£{}): £{}".format(tax,sal))
else:
    print("\nNow minus income tax:\n")
    tax = 0 if sal<=pa else (sal-pa)*0.4 if (sal-pa)>50270 else sal*0.2
    sal = sal-tax
>>>>>>> 178107df5c03ef0398df43bb946ef264356e93b6
    print("Remaning income after tax (£{}): £{}".format(tax,sal))