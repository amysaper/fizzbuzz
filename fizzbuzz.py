import sys

#hard-coded limit. Default to this if the user does not supply arguments
#(or any arguments >0) when calling the script, or does not enter any raw input. 
limit = 10
arguments = sys.argv

#Debugger #1 to test if any arguments are supplied- working
print (sys.argv)
#Checks to see if the user entered any arguments when calling the argument, and then only reassigns limit to that number if the number is greater than 0.

if len(arguments)>1:
#if (sys.argv[1:] > 0):
  #debugger #2 to test if an argument is supplied. not working! 
  print ("Argument supplied.")
  for arg in sys.argv[1:]:
   if (int(arg) >0):
     limit = int(arg)
else:
  #Supposed to prompt the user to manually enter a limit, but it's not working :(
     #debugger #3: never gets here
  print ("asking user for input")
  user_limit = input("Please set an integer limit ")
  if (int(user_limit)>0):
    limit = int(user_limit)
    print (limit)

#Main program, follows the rules of the FizzBuzz game, up to the limit
print (("Fizz buzz counting up to ") + str(limit))
for i in range (1,int(limit)+1):
  if i%3 ==0 and i%5 ==0:
      print ("fizzbuzz")
  elif i%3 ==0:
      print ("fizz")
  elif i%5 ==0:
      print ("buzz")
  else:
      print (i)