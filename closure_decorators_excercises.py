#Closures-Decorators Excercises

#Closure Excercise
#Using a closure, create a function, multiples_of(n) which we can use to
#create generators that generate multiples of n less than a given number.
def multiples_of(n):
    def multiples(m):
      for item in range(1,m):
          if item%n ==0:
            yield item
            
    return multiples

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)


print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)
# output: 7 14 21 28
#----------------------------------------------------------------------

#Decorators Excercise 1
#@make_upper – make every letter of a string returned from the decorated
#function uppercase.
def mark_upper(func):
  def wapper():
    return func().upper()
  return wapper

def hello_world():
    return 'hello young, good day!!'

hello_world=mark_upper(hello_world)

print(hello_world()) # output: HELLO YOUNG, GOOD DAY!!
#-----------------------------------------------------------------------

#Decorators Excercise 2
#@print_func_name – print the name of the decorated function before
#executing the function.
def print_func_name(func): 
  def wapper():
    print(func.__name__, "is running...")
    return func()
  return wapper

def my_func():
    print('Python is fun!!')

my_func= print_func_name(my_func)
my_func() # output: my_func is running...
            #Python is fun
#----------------------------------------------------------------------

#Decoratos Excercise 3
#@give_name(name) – concatenate the given name at the end of a string
#returned from the decorated function.
def give_name(name):
  def dec(func):
    def wrapper():
      return func() + ' ' + name
    return wrapper
  return dec

def greeting():
    return 'Hello'
greeting=give_name('Theresa')(greeting)
print(greeting()) # output: Hello Theresa
#---------------------------------------------------------------------

#Decorators Excercise 4
#@print_input_type – print a data type of the input argument before
#executing the decorated function.
def print_input_type(func):
  def wapper(num):
    print('The input data type is ', type(num))
    return func(num)
  return wapper

def square(n):
    return n ** 2

square=print_input_type(square)
print(square(3.5)) # output: The input data type is <class 'float'>
                    #12.25
#-------------------------------------------------------------------

#Decorators Excercise 5
#@check_return_type(return_type) – check if the return type of the
#decorated function is return_type and print the result before executing
#the function.
def check_return_type(func,test_type):
  def return_type(item):
    result=func(item)
    if not isinstance(result, test_type):
      print('==========Error!!')
      print('The return type is NOT', test_type)
    else:
      print('The return type is ',type(item))
    return result
  return return_type

#pass in a string
def square(n):
    return n ** 2
square=check_return_type(square, str)
print(square(6)) # output: =========Error!!
                    #The return type is NOT <class 'str'>
                    #36

#pass in a float
def square(n):
    return n ** 2
square=check_return_type(square, float)
print(square(2.9)) # output: The return type is <class 'float'>
                    #8.41
#------------------------------------------------------------------------

#Decorators Excercise 6
#@execute_log – write a function execution log on the log file. (log below)
import datetime
def execute_log(func):
  def wapper(*args):
    print(datetime.datetime.now(), func.__name__)
    return func(*args)
  return wapper

def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult

def hello_world():
    return 'hello world!!'

multiply=execute_log(multiply)
hello_world=execute_log(hello_world)
print(multiply(6, 2, 3)) # 36
print(hello_world()) # hello world!!
print(multiply(2.2, 4)) # 8.8
print(hello_world()) # hello world!!


#function_execution.log
#2020-05-01 13:55:53.059315 multiply
#2020-05-01 13:55:53.060312 hello_world
#2020-05-01 13:55:53.060314 multiply
#2020-05-01 13:55:53.060323 hello_world