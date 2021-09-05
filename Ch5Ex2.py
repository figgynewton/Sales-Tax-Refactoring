Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
	amount = float(input( "Enter amount of purchase: $" ))
	state_tax = 0.05
	county_tax = 0.025
	total_tax = state_tax + county_tax
	sales_total = total_tax + amount

	
>>> def display_totals(amount, state_tax, county_tax, total_tax, sales_total):
	print( " Amount is: $", format(amount, '.2f'), sep = "")
	print( " State sales tax is: $", format(state_tax, '.2f'), sep = "")
	print( " County sales tax is: $", format(county_tax, '.2f'), sep = "")
	print( " Total sales tax is: $", format(total_tax, '.2f'), sep = "")
	print( " Total is: $", format(sales_total, '.2f'), sep = "")

	
>>> main()
Enter amount of purchase: $7.89
>>> 
