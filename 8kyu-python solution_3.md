# Python Codewars Solution - 8kyu(3)

> [name=Liu, Yu-Chun] [time=Tue, Apr 26, 2021 09:24 PM]
###### tags: `Python` `codewars`

---

## Difference of Volumes of Cuboids
> [See on CodeWars.com](https://www.codewars.com/kata/58cb43f4256836ed95000f97)

### **Definition**  
In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

#### **Example:**
```
find_difference([2, 2, 3], [5, 4, 1]) => 8.
```
:sparkles: [2,2,3] = 12, [5,4,1] = 20, 20-12=8

### **Given Code**
```python
def find_difference(a, b):
    # Your code here!
```

### **Solution Code**
```python
def find_difference(a, b):
    a = a[0]*a[1]*a[2]
    b = b[0]*b[1]*b[2]
    return abs(a-b)
```

:arrow_down_small: 
```python
# math.prod()方法返回給定迭代器中元素的乘積
import math
def find_difference(a, b):
    return abs(math.prod(a)-math.prod(b))
```

![](https://i.imgur.com/ls0AvMB.png)

---

## Stringy Strings
> [See on CodeWars.com](https://www.codewars.com/kata/563b74ddd19a3ad462000054)

### **Definition**  
write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

#### **Example:**
```
stringy(6) => '101010'
stringy(4) => '1010'
stringy(12) => '101010101010'
```
:sparkles:

### **Given Code**
```python
def stringy(size):
    # Good Luck!
```

### **Solution Code**
```python
def stringy(size):
    result = ''
    for i in range(size):
        if i % 2 == 0:
            result = result+'1'
        else:
            result = result+'0'
    return result
```

:arrow_down_small: 
```python
def stringy(size):
    return "10" * (size / 2) + "1" * (size % 2)
```

![](https://i.imgur.com/Oo4n9PG.png)

---

## A wolf in sheep's clothing
> [See on CodeWars.com](https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15)

### **Definition**  
Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array:  
![](https://i.imgur.com/f0xXnGN.png)

If the wolf is the closest animal to you, return `"Pls go away and stop eating my sheep"`. Otherwise, return `"Oi! Sheep number N! You are about to be eaten by a wolf!"` where N is the sheep's position in the queue.

#### **Example:**
```
warn_the_sheep(["sheep", "sheep", "sheep", "wolf", "sheep"])
=> "Oi! Sheep number 1! You are about to be eaten by a wolf!"

warn_the_sheep(["sheep", "sheep", "wolf"])
=> "Pls go away and stop eating my sheep"
```
:sparkles:

### **Given Code**
```python
def warn_the_sheep(queue):
    pass
```

### **Solution Code**
```python
def warn_the_sheep(queue):
    count = len(queue)
    if queue[len(queue)-1] == 'wolf':
        return "Pls go away and stop eating my sheep"
    
    for i in range(len(queue)):
        count = count-1
        if queue[i] == 'wolf':
            return f'Oi! Sheep number {count}! You are about to be eaten by a wolf!'
```

:arrow_down_small: 
```python
def warn_the_sheep(queue):    
    queue.reverse()
    wolfnum = queue.index("wolf")
    if wolfnum == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return f"Oi! Sheep number {wolfnum}! You are about to be eaten by a wolf!"
```

![](https://i.imgur.com/nXwjKDQ.png)

---

## Convert a Boolean to a String
> [See on CodeWars.com](https://www.codewars.com/kata/551b4501ac0447318f0009cd)

### **Definition**  
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

#### **Example:**
```
boolean_to_string(True) => "True"
boolean_to_string(False) => "False"
```
:sparkles:

### **Given Code**
```python
def boolean_to_string(b):
    #your code here
```

### **Solution Code**
```python
def boolean_to_string(b):
    if b:
        return 'True'
    else:
        return 'False'
```

:arrow_down_small: 
```python
def boolean_to_string(b):
    return str(b)
```

![](https://i.imgur.com/3VEXAbN.png)

---

## The Feast of Many Beasts
> [See on CodeWars.com](https://www.codewars.com/kata/5aa736a455f906981800360d)

### **Definition**  
All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the same letters as the animal's name.  
For example, the `great blue heron` is bringing `garlic naan` and the `chickadee` is bringing `chocolate cake`.

Write a function `feast` that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.

Assume that `beast` and `dish` are always lowercase strings, and that each has at least two letters.  
`beast` and `dish` may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numerals.

#### **Example:**
```
feast("chickadee", "chocolate cake") => True
feast("brown bear", "bear claw") => False
```
:sparkles:

### **Given Code**
```python
def feast(beast, dish):
    # your code here
    pass
```

### **Solution Code**
```python
def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    return False
```

:arrow_down_small: 
```python
def feast(beast, dish):
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])
```

![](https://i.imgur.com/8Ij4JEA.png)

---

## Return Negative
> [See on CodeWars.com](https://www.codewars.com/kata/55685cd7ad70877c23000102)

### **Definition**  
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

#### **Example:**
```
make_negative(1);  => -1
make_negative(-5); => -5
make_negative(0);  => 0
```
:sparkles:

### **Given Code**
```python
def make_negative( number ):
    # ...
```

### **Solution Code**
```python
def make_negative( number ):
    if number > 0:
        return number*(-1)
    return number
```

:arrow_down_small: 
```python
def make_negative( number ):
    return (-1) * abs(number)
```

![](https://i.imgur.com/4N1IYbt.png)

---

## Reversed Words
> [See on CodeWars.com](https://www.codewars.com/kata/51c8991dee245d7ddf00000e)

### **Definition**  
Complete the solution so that it reverses all of the words within the string passed in.

#### **Example:**
```
"The greatest victory is that which requires no battle" 
=> "battle no requires which that is victory greatest The"
```
:sparkles:

### **Given Code**
```python
def reverse_words(s):
    return s
```

### **Solution Code**
```python
def reverse_words(s):
    a = s.split(' ')
    a.reverse()
    return ' '.join(a)
```

:arrow_down_small: 
```python
def reverseWords(str):
    return ' '.join(reversed(str.split(' ')))
```

![](https://i.imgur.com/mpodwv9.png)

---

## Reversed Strings
> [See on CodeWars.com](https://www.codewars.com/kata/5168bb5dfe9a00b126000018)

### **Definition**  
Complete the solution so that it reverses the string passed into it.

#### **Example:**
```
'world'  =>  'dlrow'
```
:sparkles:

### **Given Code**
```python
def solution(string):
    pass
```

### **Solution Code**
```python
def solution(string):
    arr = []
    for i in range(len(string)):
        arr.append(string[i])
    
    return ''.join(reversed(arr))
```

:arrow_down_small: 
```python
def solution(string):
    return str[::-1]
```

![](https://i.imgur.com/oqYwCvK.png)

---

## Is he gonna survive?
> [See on CodeWars.com](https://www.codewars.com/kata/59ca8246d751df55cc00014c)

### **Definition**  
A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

`Return True if yes, False otherwise :)`

#### **Example:**
```
'world'  =>  'dlrow'
```
:sparkles:

### **Given Code**
```python
def hero(bullets, dragons):
    return
```

### **Solution Code**
```python
def hero(bullets, dragons):
    return bool(dragons * 2 <= bullets)
```

![](https://i.imgur.com/RJ8ty5P.png)

---

## Summation?
> [See on CodeWars.com](https://www.codewars.com/kata/55d24f55d7dd296eb9000030)

### **Definition**  
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

#### **Example:**
```
summation(2) -> 3
summation(8) -> 36
```
>:sparkles:
    summation(2): 1 + 2
    summation(8): 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

### **Given Code**
```python
def summation(num):
    pass # Code here
```

### **Solution Code**
```python
def summation(num):
    sum = 0
    for i in range(num+1):
        sum = sum+i
    return sum
```

乾...用梯形公式就好了齁= =
:arrow_down_small: 
```python
def solution(string):
    return (num+1)*num / 2
```

![](https://i.imgur.com/PlKIK1b.png)

---

## Sum of positive
> [See on CodeWars.com](https://www.codewars.com/kata/5715eaedb436cf5606000381)

### **Definition**  
You get an array of numbers, return the sum of all of the positives ones.

Note: if there is nothing to sum, the sum is default to 0.

#### **Example:**
```
[1,-4,7,12] => 1 + 7 + 12 = 20
```
>:sparkles:

### **Given Code**
```python
def positive_sum(arr):
    # Your code here
    return 0
```

### **Solution Code**
```python
def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum = sum+i
    return sum
```

![](https://i.imgur.com/FAz85bo.png)

---

## Total pressure calculation
> [See on CodeWars.com](https://www.codewars.com/kata/5b7ea71db90cc0f17c000a5a)

### **Definition**  
Given the molecular mass of two molecules M~1~ and M~2~ , their masses present m~1~ and m~2~ in a vessel of volume Vat a specific temperature T, find the total pressure P~total~ exerted by the molecules.  
Formula to calculate the pressure is:  
![](https://i.imgur.com/uomTaTy.png)

#### **Example:**
```
solution(44, 30, 3, 2, 5, 50) => 0.7146511212121212
```
>:sparkles:

### **Given Code**
```python
def solution(M1, M2, m1, m2, V, T) :
    # your code goes here
```

### **Solution Code**
```python
def solution(M1, M2, m1, m2, V, T) :
    M1 = m1 * 0.001/M1;
    M2 = m2 * 0.001/M2;
    T = T + 273.15;
    R = 0.082;
    
    return (((M1 + M2) * R * T) / V) * 1000;
```

![](https://i.imgur.com/b6fNBAQ.png)

---

## Function 1 - hello world
> [See on CodeWars.com](https://www.codewars.com/kata/523b4ff7adca849afe000035)

### **Definition**  
Description:  
Make a simple function called greet that returns the most-famous "hello world!".

Style Points  
Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of? What is a "hello world" solution you would want to show your friends?

#### **Example:**
```
solution(44, 30, 3, 2, 5, 50) => 0.7146511212121212
```
>:sparkles:

### **Given Code**
```python
# Write a function `greet` that returns "hello world!"
```

### **Solution Code**
```python
def greet():
    return 'hello world!'
```

![](https://i.imgur.com/AuxhI9g.png)

---

## Function 2 - squaring an argument
> [See on CodeWars.com](https://www.codewars.com/kata/523b623152af8a30c6000027)

### **Definition**  
Now you have to write a function that takes an argument and returns the square of it.

#### **Example:**
```
square(3) => 9
```

### **Given Code**
```python
def square(n):
    pass
```

### **Solution Code**
```python
def square(n):
    return n**2
```

![](https://i.imgur.com/BGBnj1I.png)

---

## Function 3 - multiplying two numbers
> [See on CodeWars.com](https://www.codewars.com/kata/523b66342d0c301ae400003b)

### **Definition**  
Implement a function which multiplies two numbers.

#### **Example:**
```
multiply(2, 3) -> 6
```

>:sparkles: 寫一個方法讓值相乘

### **Given Code**
```python
#your code here
```

### **Solution Code**
```python
def multiply(a, b):
    return a*b
```

![](https://i.imgur.com/ejZETL9.png)

---

## UEFA EURO 2016
> [See on CodeWars.com](https://www.codewars.com/kata/57613fb1033d766171000d60)

### **Definition**  
Finish the uefaEuro2016() function so it return string just like in the examples below.

#### **Example:**
```
uefa_euro_2016(['Germany', 'Ukraine'],[2, 0])
=> "At match Germany - Ukraine, Germany won!"
uefa_euro_2016(['Belgium', 'Italy'],[0, 2])
=> "At match Belgium - Italy, Italy won!"
uefa_euro_2016(['Portugal', 'Iceland'],[1, 1])
=> "At match Portugal - Iceland, teams played draw."
```
>:sparkles:

### **Given Code**
```python
def uefa_euro_2016(teams, scores):
    pass
```

### **Solution Code**
```python
def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!'
    elif scores[0] < scores[1]:
        return f'At match {teams[0]} - {teams[1]}, {teams[1]} won!'
    elif scores[0] == scores[1]:
        return f'At match {teams[0]} - {teams[1]}, teams played draw.'
```

![](https://i.imgur.com/ZBIqWc1.png)

---

## Grasshopper - Grade book
> [See on CodeWars.com](https://www.codewars.com/kata/55cbd4ba903825f7970000f5)

### **Definition**  
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

#### **Example:**
```
get_grade(82, 85, 87) => "B"
get_grade(44, 55, 52) => "F"
```

>:sparkles:
![](https://i.imgur.com/k9t7g8W.png)

### **Given Code**
```python
def get_grade(s1, s2, s3):
    # Code here
    return "F"
```

### **Solution Code**
```python
def get_grade(s1, s2, s3):
    avg = (s1+s2+s3)/3
    if 90 <= avg <= 100:
        return 'A'
    elif 80 <= avg < 90:
        return 'B'
    elif 70 <= avg < 80:
        return 'C'
    elif 60 <= avg < 70:
        return 'D'
    return "F"
```

![](https://i.imgur.com/jrdJcGO.png)

---

## Grasshopper - Variable Assignment Debug
> [See on CodeWars.com](https://www.codewars.com/kata/5612e743cab69fec6d000077)

### **Definition**  
Fix the variables assigments so that this code stores the string 'devLab' in the variable name.

#### **Example:**
```
name = a+b
```

>:sparkles:
![](https://i.imgur.com/k9t7g8W.png)

### **Given Code**
```python
a == "dev"
b == "Lab"

name == a + b
```

### **Solution Code**
```python
a ="dev"
b ="Lab"

name =a + b
```

![](https://i.imgur.com/quM5jfx.png)

---

## Beginner - Reduce but Grow
> [See on CodeWars.com](https://www.codewars.com/kata/57f780909f7e8e3183000078)

### **Definition**  
Given a non-empty array of integers, return the result of multiplying the values together in order. 

#### **Example:**
```
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```

>:sparkles:

### **Given Code**
```python
def grow(arr):
    pass
```

### **Solution Code**
```python
def grow(arr):
    result = 1
    for i in arr:
        result = result * i
    return result
```

![](https://i.imgur.com/eOkOpIB.png)

---

## Beginner - Lost Without a Map
> [See on CodeWars.com](https://www.codewars.com/kata/57f781872e3d8ca2a000007e)

### **Definition**  
Given an array of integers, return a new array with each value doubled. 

For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.

#### **Example:**
```
[1, 2, 3] --> [2, 4, 6]
```

>:sparkles: 輸出array內兩倍的值

### **Given Code**
```python
def maps(a):
    pass
```

### **Solution Code**
:speech_balloon: [Lambda用法參考](https://www.learncodewithmike.com/2019/12/python-lambda-functions.html)
```python
def maps(a):
    return list(map(lambda a: a * 2, a))
```

![](https://i.imgur.com/77KvA3T.png)

---

## Get the mean of an array
> [See on CodeWars.com](https://www.codewars.com/kata/563e320cee5dddcf77000158)

### **Definition**  
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy !  
You just need to write a script.

Return the average of the given array `rounded down` to its nearest integer.

The array will never be empty.

#### **Example:**
```
get_average([1, 5, 87, 45, 8, 8]) => 25
```

>:sparkles: 

### **Given Code**
```python
def get_average(marks):
    raise NotImplementedError("TODO: get_average")

```

### **Solution Code**
```python
import math
def get_average(marks):
    sum = 0
    for i in marks:
        sum += i
    avg = sum/len(marks)
    return math.floor(avg)
    raise NotImplementedError("TODO: get_average")
```

:arrow_down_small: 
```python
def get_average(marks):
    return sum(marks)//len(marks)
```

![](https://i.imgur.com/ANXXrud.png)

---

## Do I get a bonus?
> [See on CodeWars.com](https://www.codewars.com/kata/56f6ad906b88de513f000d96)

### **Definition**  
It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?

Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "£" (= "\u00A3", JS, Go, Java and Julia), `"$" (C#, C++, Ruby, Clojure, Elixir, PHP, Python, Haskell and Lua)` or "¥" (Rust).
#### **Example:**
```
bonus_time(2, True) => '$20'
bonus_time(78, False) => '$78'
```

>:sparkles: 

### **Given Code**
```python
def bonus_time(salary, bonus):
    #your code here
```

### **Solution Code**
```python
def bonus_time(salary, bonus):
    if bonus:
        salary = salary*10
    return f'${salary}'
```

:arrow_down_small: 
簡化寫法QQ
```python
def bonus_time(salary, bonus):
    return f'${salary * 10 if bonus else salary}'
```

![](https://i.imgur.com/ANXXrud.png)

---

## Find the first non-consecutive number
> [See on CodeWars.com](https://www.codewars.com/kata/58f8a3a27a5c28d92e000144)

### **Definition**  
Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

If the whole array is consecutive then return null2.

The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!
#### **Example:**
```
first_non_consecutive([4,5,6,7,8,9,11]) => 11
first_non_consecutive([31,32]) => None
```

>:sparkles: 

### **Given Code**
```python
def first_non_consecutive(arr):
    #your code here
```

### **Solution Code**
```python
def first_non_consecutive(arr):
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i] != 1:
            return arr[i+1]
    return None
```

![](https://i.imgur.com/yXuT071.png)

---

## get character from ASCII Value
> [See on CodeWars.com](https://www.codewars.com/kata/55ad04714f0b468e8200001c)

### **Definition**  
Write a function which takes a number and returns the corresponding ASCII char for that value.

#### **Example:**
```
get_char(65) => 'A'
```

>:sparkles: 

### **Given Code**
```python
def get_char(c):
  # Your code goes here ^_^
  return
```

### **Solution Code**
```python
def get_char(c):
  return chr(c)
```

![](https://i.imgur.com/auFWpyv.png)

---

## L1: Bartender, drinks!
> [See on CodeWars.com](https://www.codewars.com/kata/568dc014440f03b13900001d)

### **Definition**  
Complete the function that receives as input a string, and produces outputs according to the following table:  
![](https://i.imgur.com/VoiOyOx.png)


#### **Example:**
```
get_char(65) => 'A'
```

>:sparkles: 

### **Given Code**
```python
def get_drink_by_profession(param):
    # code me!
```

### **Solution Code**
```python
def get_drink_by_profession(param):
    if param.title() == 'Jabroni':
        return 'Patron Tequila'
    elif param.title() == 'School Counselor':
        return 'Anything with Alcohol'
    elif param.title() == 'Programmer':
        return 'Hipster Craft Beer'
    elif param.title() == 'Bike Gang Member':
        return 'Moonshine'
    elif param.title() == 'Politician':
        return 'Your tax dollars'
    elif param.title() == 'Rapper':
        return 'Cristal'
    else:
        return 'Beer'
```

![](https://i.imgur.com/oH9iEuj.png)

---

## Gravity Flip
> [See on CodeWars.com](https://www.codewars.com/kata/5f70c883e10f9e0001c89673)

### **Definition**  
If you've completed this kata already and want a bigger challenge, here's the 3D version

Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. The box is special because it has the ability to change gravity.


#### **Example:**
```
flip('R', [3, 2, 1, 2])     =>  [1, 2, 2, 3]
flip('L', [1, 4, 5, 3, 5])  =>  [5, 5, 4, 3, 1]
```

>:sparkles: 

### **Given Code**
```python
def flip(d, a):
    # Do some magic
```

### **Solution Code**
```python
def flip(d, a):
    if d == 'R':
        a.sort()
    elif d == 'L':
        a.sort(reverse=True)
    return a
```

![](https://i.imgur.com/oH9iEuj.png)

---

## Super Duper Easy
> [See on CodeWars.com](https://www.codewars.com/kata/55a5bfaa756cfede78000026)

### **Definition**  
Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

#### **Example:**
```
problem("hello") => "Error"
problem(1) => 56
```

>:sparkles: 

### **Given Code**
```python
def problem(a):
    #Easy Points ^_^
```

### **Solution Code**
```python
def problem(a):
    if type(a) == str:
        return 'Error'
    else:
        return a*50+6
```

![](https://i.imgur.com/kSswPLb.png)

---

## Are arrow functions odd?
> [See on CodeWars.com](https://www.codewars.com/kata/559f80b87fa8512e3e0000f5)

### **Definition**  
Time to test your basic knowledge in functions!  
Return the odds from a list:

#### **Example:**
```
[1, 2, 3, 4, 5]  -->  [1, 3, 5]
[2, 4, 6]        -->  []
```

>:sparkles: 

### **Given Code**
```python
odds = lambda: 
```

### **Solution Code**
```python
def odds(x):
    arr = []
    for i in x:
        if i % 2 != 0:
            arr.append(i)
    return arr
```

![](https://i.imgur.com/CnwYqkI.png)

---

## Parse nice int from char problem
> [See on CodeWars.com](https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1)

### **Definition**  
Ask a small girl - "How old are you?". She always says strange things... Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.

#### **Example:**
```
get_age("4 years old") =>4
get_age("5 years old") =>5
```

>:sparkles: 

### **Given Code**
```python
def get_age(age):
    #your code here
```

### **Solution Code**
```python
def get_age(age):
    return int(age[0])
```

![](https://i.imgur.com/niTGGl1.png)

---

## N-th Power
> [See on CodeWars.com](https://www.codewars.com/kata/57d814e4950d8489720008db)

### **Definition**  
This kata is from check py.checkio.org

You are given an array with positive numbers and a non-negative number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

#### **Example:**
```
array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.
```

>:sparkles: 

### **Given Code**
```python
def index(array, n):
```

### **Solution Code**
```python
def index(array, n):
    if n >= len(array):
        return -1
    else:
        return array[n]**n
```

![](https://i.imgur.com/Hi7lkyH.png)

---

## Ensure question
> [See on CodeWars.com](https://www.codewars.com/kata/5866fc43395d9138a7000006)

### **Definition**  
Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question mark, in which case, returns the original string.

#### **Example:**
```
ensure_question("Yes") == "Yes?" 
ensure_question("No?") == "No?"
```

>:sparkles: 

### **Given Code**
```python
def ensure_question(s):
    # Code here
```

### **Solution Code**
```python
def ensure_question(s):
    if len(s)>0:
        if s[-1] == '?':
            return s
    return f'{s}?'
```

:arrow_down_small: 
```python
def ensure_question(s):
    if not s.endswith("?"):
            return s + "?"
        return s
```

![](https://i.imgur.com/UXu9xKL.png)




