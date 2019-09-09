## Iterator: 
- An Iterator is an object, which allows a programmer to traverse through all the elements of a collection, regardless of 
its specific implementation.
- Values of an Iterator can be accessed only once and in sequential order.
- It raises an StopIteration Error when there are no values to be returned.

Sample Iterator Examples:
```
Ex 1. :-
x = [1, 2, 3]
s = iter(x)            
print(next(s))      # -> 1
print(next(s))      # -> 2
print(next(s))      # -> 3
print(next(s))      # -> StopIteration Error

Ex 2. :-
y = "PYTHON"
t = iter(y)
print(next(t))      # -> P
print(next(t))      # -> Y
print(next(t))      # -> T
print(next(t))      # -> H
print(next(t))      # -> O
print(next(t))      # -> N
print(next(t))      # -> StopIteration Error
```

## List Comprehensions: 
- This is one of the important concepts when we want create a new list from some operations on list, strings or tuple.
- Syntactically, its nothing but a iterable consisting of for loop which is followed by some expression.
- This is also saves the lines of codes.
- We can also apply the comprehensions to dictionary, tuple & set as well just like list comprehensions. 

Sample List Comprehension Examples:
```
Ex 1. :- 
s = "Python"
# Using List Comprehension:
list1 = [ch for ch in s] # -> ['P', 'Y', 'T', 'H', 'O', 'N'] #Only One Line of Code

# Using For-Loop:
list2 = []
for ch in s:
  list2.append(ch)
print(list2) # -> ['P', 'Y', 'T', 'H', 'O', 'N'] #Three Lines of Code

Ex 2 :-
tuple1 = ('aaa', 'bbb', 'ccc', 'ddd')

list1 = [l for l in tuple1 if l != 'bbb']
print(list) # -> ['aaa', 'ccc', 'ddd']

Ex 3 :-
numberList = [x ** 2 for x in range(10) if x % 2 == 0]
print(numberList) # -> [0, 4, 16, 36, 64]
```

## Yields:
- Just like return statement in function, yield is used but it is quite different from return statement.
- Yield stops the execution & sends value back to caller but retain enough state to enable function to resume where it is 
left off whereas return is doesn't retain any state of function & also present at the end of function.
- Return sends a specified value back to its caller whereas Yield can produce a sequence of values.  

Sample Yield Example: 
```
# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 

# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
	i = 1; 

	# An Infinite loop to generate squares 
	while True: 
		yield i*i				 
		i += 1 # Next execution resumes 
				# from this point	 

# Driver code to test above generator 
# function 
for num in nextSquare(): 
	if num > 100: 
		break	
	print(num) 
```
## Generator: 
- Generator is an expression or function which returns an object known as generator object.
- A Generator object is an iterator, whose values are created at the time of accessing them.
- Generator as an expression:
```
l = [1, 2, 3]
g = (i**2 for i in l)  # generator expression
print(next(g))         # -> 1
print(next(g))         # -> 4
print(next(g))         # -> 9
```
- Generator as an function:
```
def generatorFunction(): 
    yield 1            
    yield 2            
    yield 3            
    
for value in simpleGeneratorFun():  
    print(value) # -> 1 2 3(Each number on separate line) 
```
