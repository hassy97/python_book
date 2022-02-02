'''Write a program that asks the user to input 10 integers, and then
prints the largest odd number that was entered. If no odd number was entered, it
should print a message to that effect.'''

# these are some restriction use only if-else,while,variable assignment,operators and typecast
ans = None
y = 10
itersLeft = y 


while(itersLeft > 0):
    user_input = int(input('Type a integer number'))

    if  itersLeft == 10  or (user_input % 2 and user_input > ans):   
        ans = user_input
    if user_input % 2 == 0:   # even case
        ans = user_input
    itersLeft = itersLeft - 1

if ans%2 ==1: ## largest odd case 
    print("The largets odd number is : ", str(ans))
else:
    print("no odd number was entered")
    
