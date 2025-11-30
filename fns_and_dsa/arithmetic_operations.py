# def perform_operation(num1, num2, operation):
#     operation = operation.lower().strip()

#     if operation == "add":
#         return num1 + num2

#     elif operation == "subtract":
#         return num1 - num2

#     elif operation == "multiply":
#         return num1 * num2

#     elif operation == "divide":
#         if num2 == 0:
#             return "Error, cannot divide by zero"
#         return num1 / num2

#     else:
#         return "Invalid operation"



def perform_operation(num1,num2,operation):

    match operation:
        case 'add':
            result = num1 + num2
        
        case 'subtract':
            result = num1 - num2

        case 'multiply':
            result = num1 * num2

        case 'divide':

            if num1 == 0 or num2 == 0:
                print("Can't divide zero")
                return

            else:
                result = num1 / num2
    print(f'The result of {num1} {operation} {num2} is {result}')



perform_operation(5,3,"add")