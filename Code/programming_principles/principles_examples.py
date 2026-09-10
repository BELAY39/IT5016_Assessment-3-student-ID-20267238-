#IT5016 Assessment 3
#programming principles Examples

#KISS-keep It simple,stupid
#This function uses a simple calculation that is easy to understand.
def calculate_total(price,quantity):
    return price*quantity

#DRY-Don't Repeat yourself
#This function can be reused instead of writing the same calculation
#in different parts of the program.
def calculate_discount(price,discount):
    return price-(price*discount)

#SRP-single responsibility principle
#This function has one responsibility:
def display_message(message):
    print(message)

    #separation of concerns
    #Input,calculation and display can be kept as separate tasks.
def get_total(price,quantity):
    return price* quantity

#YAGNI-You aren't gonna need it
#only the functionality required by the program is included
def show_result(result):
    print("Result:",result)

#OCP-open/closed principle
#The function can work with different values without changing
#the function itself.
def calculate_total_with_tax(price,tax_rate):
    return price+(price*tax_rate)

#Example 
total=calculate_total(20,3)
discounted_price=calculate_discount(total,0.10)

display_message("programming principles examples")
show_result(total)
show_result(discounted_price)