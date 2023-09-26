print(type("Hello World"))
print(type(17))
print(type("17"))
print(type('''and even this...''') )
print (42,000)
message = "Hi, it's me."
n = 17
print (message)
print (n)
y = 3.14
x = len("hello")
print(x)
print(y)
print (2**3)
print (7//2)
les= 7%2
print (les)
n = input("Please enter your name: ")
print("Hello", n)
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x)

n=input("Please tell me what time it is:")
y=input("How many hours are left till the alarm?:" )
z=((n+y)%24) #jak počítat s těmi proměnnými? 
print ("It is currently",z, "o'clock.")

print ((6*(1-2))) 