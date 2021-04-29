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
1, 2, 3] --> [2, 4, 6]
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

![](https://i.imgur.com/eOkOpIB.png)
