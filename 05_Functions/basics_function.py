# Built in function
# 1. sum() used to calculate the sum of all elements in an iterable, such as list or tuple or set.
# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)

# Coercion in Python: 
# x = 10     # int  
# y = 3.5    # float  
# print(x + y)   # int + float → float  # Output: 13.5

# # Coercion in list
# numbers = [1, 2.5, 3, 5.7]
# print(sum(numbers)) # integer are coerced to float

# without import in buit function
# print(abs(-5)) 
# print(round(3.124))
# print(round(3.124345,2)) # round(x, ndigit)
# print(max(1,2,34,5,39)) # return maximum value
# print(min(1,2,34,5,39)) # return minimum value
# print(pow(2,5)) # pow(x,y) return x power y
# print(sum([1,2,3,4]))

# Combining positional,Keyword and arbitery argument

def order_summary(order_id, *items, **customer_info):
    print(f"Order ID: {order_id}")
    print("Items Ordered:")
    for item in items:
        print(f"- {item}")
    
    print("Customer Information:")
    for key, value in customer_info.items():
        print(f"{key}: {value}")

order_summary(101,"apple","banana","orange", name="John Doe", address="123 Main St", phone="555-1234")