# Python Codewars Solution - 8kyu

> [name=Liu, Yu-Chun] [time=Tue, Apr 26, 2021 09:24 PM]
###### tags: `Python` `codewars`

---

## Convert a Number to a String!
> [See on CodeWars.com](https://www.codewars.com/kata/5265326f5fda8eb1160004c8)

### **Definition**  
We need a function that can transform a number into a string.  
What ways of achieving this do you know?

#### **Example:**
```
123 --> "123"
999 --> "999"
```

### **Given Code**
```python
def number_to_string(num):
    # your code here
```

### **Solution Code**
```python
def number_to_string(num):
    return str(num)
```

![](https://i.imgur.com/TqEzfLF.png)

---

## Are You Playing Banjo?
> [See on CodeWars.com](https://www.codewars.com/kata/53af2b8861023f1d88000832)

### **Definition**  
Create a function which answers the question "Are you playing banjo?".  
If your **name starts with the letter "R" or lower case "r"**, you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

#### **Example:**
```
name + " plays banjo" 
name + " does not play banjo"
```
```
name = martin 
→ martin does not play banjo

name = Rikke
→ Rikke plays banjo
```

### **Given Code**
```python
def are_you_playing_banjo(name):
    # Implement me!
    return name
```

### **Solution Code**
```python
def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name
```

![](https://i.imgur.com/ChfKj7M.png)

---

## Jenny's secret message
> [See on CodeWars.com](https://www.codewars.com/kata/53af2b8861023f1d88000832)

### **Definition**  
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?

#### **Example:**
```
name = Amy 
→ Hello, Amy!

name = Johnny
→ Hello, my love!
```

### **Given Code**
```python
def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
```

### **Solution Code**
```python
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
```

![](https://i.imgur.com/E7fVdi0.png)

---

## Convert boolean values to strings 'Yes' or 'No'
> [See on CodeWars.com](https://www.codewars.com/kata/53369039d7ab3ac506000467)

### **Definition**  
Complete the method that takes a **boolean value and return a "Yes" string for true, or a "No" string for false**

#### **Example:**
```
boolean = 'Trun'
return 'yes'

boolean = 'False'
return 'No'
```

### **Given Code**
```python
def bool_to_word(boolean):
    # TODO
```

### **Solution Code**
```python
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'
```

![](https://i.imgur.com/p4TVnHL.png)

---

## Counting sheep...
> [See on CodeWars.com](https://www.codewars.com/kata/54edbc7200b811e956000556)

### **Definition**  
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

The correct answer would be 17.

Hint: Don't forget to check for bad values like `null/undefined`
#### **Example:**
```
[True,  True,  True,  False,
  True,  True,  True,  True,
  True,  False, True,  False,
  True,  False, False, True,
  True,  True,  True,  True,
  False, False, True,  True]
```
:sparkles: True => 有羊 / False => 沒羊
### **Given Code**
```python
def count_sheeps(sheep):
  # TODO May the force be with you
  pass
```

### **Solution Code**
```python
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count +=1
    return count
```

![](https://i.imgur.com/WWMZ5NU.png)

---

## Convert number to reversed array of digits
> [See on CodeWars.com](https://www.codewars.com/kata/5583090cbe83f4fd8c000051)

### **Definition**  
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

#### **Example:**
```
348597 => [7,9,5,8,4,3]
```
:sparkles: 先反轉在一個一個存入array

### **Given Code**
```python
def digitize(n):
    return
```

### **Solution Code**
```python
def digitize(n):
    result = []
    for i in reversed(str(n)):
        result.append(int(i))
    return result
```

![](https://i.imgur.com/s5pvQzc.png)

---

## String repeat
> [See on CodeWars.com](https://www.codewars.com/kata/57a0e5c372292dd76d000d7e)

### **Definition**  
Write a function called repeatStr which repeats the given string string exactly n times.

#### **Example:**
```
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
```

### **Given Code**
```python
def repeat_str(repeat, string):
    return ''
```

### **Solution Code**
```python
def repeat_str(repeat, string):
    return repeat*string
```

![](https://i.imgur.com/kVDkWVi.png)

---

## Calculate BMI
> [See on CodeWars.com](https://www.codewars.com/kata/57a429e253ba3381850000fb)

### **Definition**  
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"  
if bmi <= 25.0 return "Normal"  
if bmi <= 30.0 return "Overweight"  
if bmi > 30 return "Obese"

#### **Example:**
```
bmi<18.5 ==> 'Underweight'
```

### **Given Code**
```python
def bmi(weight, height):
    #your code here
```

### **Solution Code**
```python
def bmi(weight, height):
    bmi = weight / height**2
    #your code here
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
```

![](https://i.imgur.com/fjmbGvF.png)

---

## Returning Strings
> [See on CodeWars.com](https://www.codewars.com/kata/55a70521798b14d4750000a4)

### **Definition**  
Make a function that will return a greeting statement that uses an input; your program should return, ``"Hello, <name> how are you doing today?".``

#### **Example:**
```
name = Shingles
→ "Hello, Shingles how are you doing today?"
```

### **Given Code**
```python
def greet(name):
    #Good Luck (like you need it)
```

### **Solution Code**
```python
def greet(name):
    return "Hello, "+name+" how are you doing today?"
```

![](https://i.imgur.com/Q9U9xr3.png)

---

## Remove First and Last Character
> [See on CodeWars.com](https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0)

### **Definition**  
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

#### **Example:**
```
Google
→ oogl
```
:sparkles: 刪除字串的第一個和最後一個字元

### **Given Code**
```python
def remove_char(s):
    #your code here
```

### **Solution Code**
```python
def remove_char(s):
    c = s[1:-1]
    return c
```

![](https://i.imgur.com/aZn0D79.png)

---

## Abbreviate a Two Word Name
> [See on CodeWars.com](https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3)

### **Definition**  
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

#### **Example:**
```
Sam Harris => S.H
Patrick Feeney => P.F
```
:sparkles: 以空格分界，抓取每個字串的第一個字元

### **Given Code**
```python
def abbrev_name(name):
    return
```

### **Solution Code**
```python
def abbrev_name(name):
    s = name[0:1].upper()
    for i in range(len(name)):
        if name[i] == ' ':
            n = name[i+1].upper()
    chr = s+'.'+n
    return chr
```

![](https://i.imgur.com/fbRg1YI.png)

---

## Calculate average
> [See on CodeWars.com](https://www.codewars.com/kata/57a2013acf1fa5bfc4000921)
 
### **Definition**  
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.

#### **Example:**
```
[1, 2, 3] => avg: 2
[] => avg: 0
```
:sparkles: 以空格分界，抓取每個字串的第一個字元

### **Given Code**
```python
def find_average(numbers):
    # your code here
    pass
```

### **Solution Code**
```python
def find_average(numbers):
    sum = 0
    if len(numbers) == 0:
        return 0
    else:
        for i in range(len(numbers)):
            sum = sum+numbers[i]
        avg = sum/len(numbers)
        return avg
```

![](https://i.imgur.com/F30HcHb.png)

---

## Area or Perimeter
> [See on CodeWars.com](https://www.codewars.com/kata/5ab6538b379d20ad880000ab)

### **Definition**  
You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.  
If it is a square, return its area.  
If it is a rectangle, return its perimeter. 

Note: It is a square if its length and width are equal, otherwise it is a rectangle. 

#### **Example:**
```
area_or_perimeter(6, 10) => 32
area_or_perimeter(3, 3) => 9
```
:sparkles: 長寬相等=>正方形, 不相等=>矩形

### **Given Code**
```python
def area_or_perimeter(l , w):
    # return your answer
```

### **Solution Code**
```python
def area_or_perimeter(l , w):
    if l==w:
        return l*w
    else:
        return (l+w)*2
```

![](https://i.imgur.com/FML73mZ.png)

---

## Enumerable Magic #25 - Take the First N Elements
> [See on CodeWars.com](https://www.codewars.com/kata/545afd0761aa4c3055001386)

### **Definition**  
Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements from the list/array.

#### **Example:**
```
take([0, 1, 2, 3, 5, 8, 13], 3) => [0, 1, 2], #should return the first 3 items
take([2, 4, 14, 18, 55], 2) => [2, 4], #should return the first 2 items
```

### **Given Code**
```python
def take(arr,n):
    pass
```

### **Solution Code**
```python
def take(arr,n):
     return arr[:n]
```

![](https://i.imgur.com/4KsRgCJ.png)

---

## Beginner Series #1 School Paperwork
> [See on CodeWars.com](https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd)

### **Definition**  
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. `If n < 0 or m < 0 return 0.`

#### **Example:**
```
n= 5, m=5 => 25
n=-5, m=5 => 0
```

### **Given Code**
```python
def paperwork(n, m):
    # Happy Coding! ^_^
```

### **Solution Code**
```python
def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        return n*m
```

![](https://i.imgur.com/SICadDp.png)

---

## Beginner Series #2 Clock
> [See on CodeWars.com](https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a)

### **Definition**  
Clock shows `h` hours, `m` minutes and `s` seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

#### **Example:**
```
h = 0
m = 1
s = 1

result = 61000
```
:sparkles: Input constraints:  
　　0 <= h <= 23  
　　0 <= m <= 59  
　　0 <= s <= 59

### **Given Code**
```python
def past(h, m, s):
    # Good Luck!
```

### **Solution Code**
```python
def past(h, m, s):
    return (h*3600+m*60+s)*1000
```

![](https://i.imgur.com/atYrYzb.png)

---

## MakeUpperCase
> [See on CodeWars.com](https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7)

### **Definition**  
Write a function which converts the input string to uppercase.

#### **Example:**
```
make_upper_case("hello") => "HELLO"
make_upper_case("function"), "FUNCTION")
```

### **Given Code**
```python
def make_upper_case(s):
    # Code here
```

### **Solution Code**
```python
def make_upper_case(s):
    return s.upper()
```

![](https://i.imgur.com/sVYiy3F.png)

---

## Will there be enough space?
> [See on CodeWars.com](https://www.codewars.com/kata/5875b200d520904a04000003)

### **Definition**  
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.

You have to write a function that accepts three parameters:

`cap` is the amount of people the bus can hold excluding the driver.  
`on` is the number of people on the bus excluding the driver.  
`wait` is the number of people waiting to get on to the bus excluding the driver.  
If there is **enough space, return 0**, and if there isn't, return the number of passengers he can't take.

#### **Example:**
```
cap = 10, on = 5, wait = 5 => 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 => 10 # He can't fit 10 of the 50 waiting
```
:sparkles: 如果車位足夠，return 0；不夠的話，return 無法上車的人數。

### **Given Code**
```python
def enough(cap, on, wait):
    # Your code here
```

### **Solution Code**
```python
def enough(cap, on, wait):
    if on+wait<=cap:
        return 0
    else:
        return wait-(cap-on)
```

![](https://i.imgur.com/ogz5vwU.png)

---

## Powers of 2
> [See on CodeWars.com](https://www.codewars.com/kata/57a083a57cb1f31db7000028)

### **Definition**  
Complete the function that takes a non-negative integer `n` as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).

#### **Example:**
```
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
```

### **Given Code**
```python
def powers_of_two(n):
    return []
```

### **Solution Code**
```python
def powers_of_two(n):
    arr = []
    for i in range(0,n+1):
        arr.append(2**i)
    return arr
```

![](https://i.imgur.com/Er8Qxl3.png)

---

## Drink about
> [See on CodeWars.com](https://www.codewars.com/kata/56170e844da7c6f647000063)

### **Definition**  
Make a function that receive age, and return what they drink.
> Kids drink toddy.  
> Teens drink coke.  
> Young adults drink beer.  
> Adults drink whisky.

#### **Example:**
```
13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
```
 :sparkles: constraints  
　　Children under 14 old.  
　　Teens under 18 old.  
　　Young under 21 old.  
　　Adults have 21 or more.
### **Given Code**
```python
def people_with_age_drink(age):
    return ''
```

### **Solution Code**
```python
def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age <18:
        return 'drink coke'
    elif age <21:
        return 'drink beer'
    elif age >= 21:
        return 'drink whisky'
```

![](https://i.imgur.com/tKvBg0U.png)

---

## Pre-FizzBuzz Workout #1
> [See on CodeWars.com](https://www.codewars.com/kata/569e09850a8e371ab200000b)

### **Definition**  
This is the first step to understanding FizzBuzz.

Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.

Your expected output is an array of positive integers from 1 to n (inclusive).

Your job is to write an algorithm that gets you from the input to the output.

#### **Example:**
```
pre_fizz(3) => [1,2,3]
pre_fizz(4) => [1,2,3,4]
```

### **Given Code**
```python
def pre_fizz(n):
    #your code here
```

### **Solution Code**
```python
def pre_fizz(n):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    return arr
```

![](https://i.imgur.com/IiJ6R1S.png)

---

## Swap Values
> [See on CodeWars.com](https://www.codewars.com/kata/5388f0e00b24c5635e000fc6)

### **Definition**  
I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.

Can you figure out what's wrong here?

#### **Example:**
```
arr = [1, 2] => [2, 1]
```

### **Given Code**
```python
def swap_values(args): 
    args[0] = args[1]
    args[1] = args[0]
```

### **Solution Code**
```python
def swap_values(args): 
    args[0], args[1] = args[1], args[0]
    return args
```

![](https://i.imgur.com/Xildcxi.png)

---

## Filter out the geese
> [See on CodeWars.com](https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7)

### **Definition**  
Write a function, `gooseFilter / goose-filter / goose_filter / GooseFilter`, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.

#### **Example:**
```
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
→ ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
```

### **Given Code**
```python
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #your code here
```

### **Solution Code**
```python
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    ans = []
    global geese
    for i in birds:
        if not i in geese:
            ans.append(i)
    return ans
```

![](https://i.imgur.com/uyk0a6Y.png)

---

## Generate range of integers
> [See on CodeWars.com](https://www.codewars.com/kata/55eca815d0d20962e1000106)

### **Definition**  
Implement a function named generateRange(min, max, step), which takes three arguments and generates a range of integers from min to max, with the step.  
The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)

#### **Example:**
```
generate_range(2, 10, 2) => [2,4,6,8,10]
generate_range(1, 10, 3) => [1,4,7,10]
```

### **Given Code**
```python
def generate_range(min, max, step):
    pass
```

### **Solution Code**
```python
def generate_range(min, max, step):
    result = []
    for i in range (min, max + 1, step):
        result.append(i)
    return result
```

![](https://i.imgur.com/QGwhMj3.png)

---

## The Wide-Mouthed frog!
> [See on CodeWars.com](https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89)

### **Definition**  
The wide mouth frog is particularly interested in the eating habits of other creatures.

He just can't stop asking the creatures he encounters what they like to eat. But then he meet the alligator who just LOVES to eat wide-mouthed frogs!

When he meets the alligator, it then makes a tiny mouth.

Your goal in this kata is to create complete the mouth_size method this method take one argument animal which corresponds to the animal encountered by frog. If this one is an alligator (case insensitive) return small otherwise return wide.

#### **Example:**
```
mouth_size("ant bear") => "wide"
mouth_size("alligator") => "small"
```

### **Given Code**
```python
def mouth_size(animal): 
  # code here
```

### **Solution Code**
```python
def mouth_size(animal): 
    if animal.lower() == "alligator":
        return 'small'
    else:
        return 'wide'
```

![](https://i.imgur.com/PPsyjKR.png)

---

## Quarter of the year
> [See on CodeWars.com](https://www.codewars.com/kata/5ce9c1000bab0b001134f5af)

### **Definition**  
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

#### **Example:**
```
quarter_of(8) => 3
```

### **Given Code**
```python
def quarter_of(month):
    # your code here
```

### **Solution Code**
```python
def quarter_of(month):
    if month <= 3:
        return 1
    elif month <=6:
        return 2
    elif month <=9:
        return 3
    elif month <=12:
        return 4
```

![](https://i.imgur.com/KdD9BEE.png)

---

## Miles per gallon to kilometers per liter
> [See on CodeWars.com](https://www.codewars.com/kata/557b5e0bddf29d861400005d)

### **Definition**  
Sometimes, I want to quickly be able to convert miles per imperial gallon into kilometers per liter.

Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).

Make sure to round off the result to two decimal points. If the answer ends with a 0, it should be rounded off without the 0. So instead of 5.50, we should get 5.5.

Some useful associations relevant to this kata: `1 Imperial Gallon = 4.54609188 litres 1 Mile = 1.609344 kilometres`

#### **Example:**
```
converter(12), 4.25
```

### **Given Code**
```python
def converter(mpg):
    #your code here
```

### **Solution Code**
```python
def converter(mpg):
    result=(mpg*(1.609344/4.54609188))
    return round(result, 2)
```

![](https://i.imgur.com/HC7kz2F.png)

---

## FIXME: Replace all dots
> [See on CodeWars.com](https://www.codewars.com/kata/596c6eb85b0f515834000049)

### **Definition**  
The code provided is supposed replace all the dots . in the specified String str with dashes - But it's not working properly.

#### **Example:**
```
replace_dots("one.two.three") => "one-two-three"
```

### **Given Code**
```python
import re
def replace_dots(str):
    return re.sub(r".", "-", str)
```

### **Solution Code**
```python
def replace_dots(str):
    s = str.replace('.', '-')
    return s
```

![](https://i.imgur.com/ZwachFs.png)

---

## Cat years, Dog years
> [See on CodeWars.com](https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b)

### **Definition**  
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was `humanYears` years ago.

Return their respective ages now as `[humanYears,catYears,dogYears]`

NOTES:

humanYears >= 1  
humanYears are whole numbers only

**Cat Years**  
15 cat years for first year  
+9 cat years for second year  
+4 cat years for each year after that

**Dog Years**  
15 dog years for first year  
+9 dog years for second year  
+5 dog years for each year after that

#### **Example:**
```
human_years_cat_years_dog_years(2) => [2,24,24]
human_years_cat_years_dog_years(10) => [10,56,64]
```

### **Given Code**
```python
def human_years_cat_years_dog_years(human_years):
    # Your code here
    return [0,0,0]
```

### **Solution Code**
```python
def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    elif human_years >= 3:
        cat_years = 24 + (human_years-2)*4
        dog_years = 24 + (human_years-2)*5
        
    return [human_years, cat_years, dog_years]
```

![](https://i.imgur.com/PjCbHqy.png)

---

## Reversed sequence
> [See on CodeWars.com](https://www.codewars.com/kata/5a00e05cc374cb34d100000d)

### **Definition**  
Build a function that returns an array of integers from `n` to 1 where `n`>0.

#### **Example:**
```
n=5 => [5,4,3,2,1]
```

### **Given Code**
```python
def reverse_seq(n):
    pass
```

### **Solution Code**
```python
def reverse_seq(n):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    arr.reverse()
    return arr
```

![](https://i.imgur.com/A40DUkb.png)

---

## Remove exclamation marks
> [See on CodeWars.com](https://www.codewars.com/kata/57a0885cbb9944e24c00008e)

### **Definition**  
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

#### **Example:**
```
n=5 => [5,4,3,2,1]
```

### **Given Code**
```python
def reverse_seq(n):
    pass
```

### **Solution Code**
```python
def reverse_seq(n):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    arr.reverse()
    return arr
```

![](https://i.imgur.com/A40DUkb.png)

---

## Template Strings
> [See on CodeWars.com](https://www.codewars.com/kata/55a14f75ceda999ced000048)

### **Definition**  
Template Strings, this kata is mainly aimed at the new JS ES6 Update introducing Template Strings

#### **Example:**
```
temple_strings("Animals","Good") => 'Animals are Good'
```

### **Given Code**
```python
def temple_strings(obj, feature): 
    # your code here
    pass
```

### **Solution Code**
```python
def temple_strings(obj, feature): 
    s = obj + ' are ' + feature
    return s
```

![](https://i.imgur.com/iulO7Zq.png)

---

## Lario and Muigi Pipe Problem
> [See on CodeWars.com](https://www.codewars.com/kata/56b29582461215098d00000f)

### **Definition**  
Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

The pipes connecting your level's stages together need to be fixed before you receive any more complaints. Each pipe should be connecting, since the levels ascend, you can assume every number in the sequence after the first index will be greater than the previous and that there will be no duplicates.

#### **Example:**
```
Input: 1,3,5,6,7,8

Output: 1,2,3,4,5,6,7,8
```

### **Given Code**
```python
def pipe_fix(nums):
	return []
```

### **Solution Code**
```python
def pipe_fix(nums):
    arr = []
    for i in range(nums[0],nums[len(nums)-1]+1):
        arr.append(i)
    return arr
```

![](https://i.imgur.com/l7QZ2Vx.png)

---

## Find the smallest integer in the array
> [See on CodeWars.com](https://www.codewars.com/kata/55a2d7ebe362935a210000b2)

### **Definition**  
Given an array of integers your solution should find the smallest integer.

#### **Example:**
```
[34, 15, 88, 2] => 2
[34, -345, -1, 100] => -345
```

### **Given Code**
```python
def find_smallest_int(arr):
    # Code here
```

### **Solution Code**
```python
def find_smallest_int(arr):
    return min(arr)
```

![](https://i.imgur.com/BudRqUe.png)

---

## You Can't Code Under Pressure #1
> [See on CodeWars.com](https://www.codewars.com/kata/53ee5429ba190077850011d4)

### **Definition**  
Code as fast as you can! You need to double the integer and return it.

#### **Example:**
```
double_integer(2) => 4
```
:sparkles: output = 兩倍input值

### **Given Code**
```python
def double_integer(i):
    pass # Double the integer and return it!
```

### **Solution Code**
```python
def double_integer(i):
    return 2*i
```

![](https://i.imgur.com/UUkhVBC.png)

---

## Grasshopper - Personalized Message
> [See on CodeWars.com](https://www.codewars.com/kata/5772da22b89313a4d50012f7)

### **Definition**  
Create a function that gives a personalized greeting. This function takes two parameters: `name` and `owner`.

#### **Example:**
```
name equals owner => 'Hello boss'
otherwise         => 'Hello guest'
```

### **Given Code**
```python
def greet(name, owner):
    # Add code here
```

### **Solution Code**
```python
def greet(name, owner):
    return 'Hello boss' if name==owner else 'Hello guest'
```

![](https://i.imgur.com/UUkhVBC.png)

---

## Sort and Star
> [See on CodeWars.com](https://www.codewars.com/kata/57cfdf34902f6ba3d300001e)

### **Definition**  
You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have ``"***"`` between each of its letters.

You should not remove or add elements from/to the array.

#### **Example:**
```
two_sort(["bitcoin", "take", "over", "knows", "perhaps"]) => 'b***i***t***c***o***i***n'
```

### **Given Code**
```python
def two_sort(array):
    # your code here
```

### **Solution Code**
```python
def two_sort(array):
    array.sort()
    result = '***'.join(array[0])
    return result
```

![](https://i.imgur.com/JDYq1Fg.png)

---

## Is there a vowel in there?
> [See on CodeWars.com](https://www.codewars.com/kata/57cff961eca260b71900008f)

### **Definition**  
Given an array of numbers, check if any of the numbers are the character codes for lower case vowels `(a, e, i, o, u)`.

If they are, change the array value to a string of that vowel.

Return the resulting array.
>ASCII:  
　　a: 97  
　　e: 101  
　　i: 105  
　　o: 111  
　　u: 117

#### **Example:**
```
is_vow([107, 105, 110, 107, 101, 102, 105]) => [107, 'i', 110, 107, 'e', 102, 'i']
```
:sparkles: 若array中有母音的ASCII轉成母音，其餘正常輸出

### **Given Code**
```python
def is_vow(inp):
    pass
```

### **Solution Code**
```python
def is_vow(inp):
    l=[]
    for each in inp:
        if each == 97:
            l.append('a')
        elif each == 101:
            l.append('e')
        elif each == 105:
            l.append('i')
        elif each == 111:
            l.append('o')
        elif each == 117:
            l.append('u')
        else:
            l.append(each)
    return l
```

![](https://i.imgur.com/aQytt64.png)

---

## 101 Dalmatians - squash the bugs, not the dogs!
> [See on CodeWars.com](https://www.codewars.com/kata/56f6919a6b88de18ff000b36)

### **Definition**  
Your friend has been out shopping for puppies (what a time to be alive!)... He arrives back with multiple dogs, and you simply do not know how to respond!

By repairing the function provided, you will find out exactly how you should respond, depending on the number of dogs he has.

The number of dogs will always be a number and there will always be at least 1 dog.

#### **Example:**
```
how_many_dalmatians(8) => "Hardly any"
how_many_dalmatians(100) => "Woah that's a lot of dogs!
```
:sparkles:

### **Given Code**
```python
def how_many_dalmatians(n):
  dogs ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
  
  respond = if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
  
return respond
```

### **Solution Code**
```python
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    
    if n <= 10:
        s=dogs[0]
    elif n <= 50:
        s=dogs[1]
    elif n == 101:
        s=dogs[3]
    else:
        s=dogs[2]
        
    return s
```

![](https://i.imgur.com/bB6QArX.png)

---

## Squash the bugs
> [See on CodeWars.com](https://www.codewars.com/kata/56f173a35b91399a05000cb7)

### **Definition**  
Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. `Output should be the length of the longest word, as a number.`

There will only be one 'longest' word.

#### **Example:**
```
find_longest("Sausage chops") => 7
find_longest("Hello world") => 5
```
:sparkles:

### **Given Code**
```python
def find_longest(string):
    spl = str.split(" ")
    longest = 0
    i=0
    while (i > spl.length):
    if (spl(i).length > longest): longest = spl[i].length
    return longest
```

### **Solution Code**
```python
def find_longest(string):
    spl = string.split(" ")
    longest = 0
    for i in range(0, len(spl)):
        if len(spl[i])> longest:
            longest = len(spl[i])
    
    return longest
```

![](https://i.imgur.com/33cdlYR.png)

---

## You only need one - Beginner
> [See on CodeWars.com](https://www.codewars.com/kata/57cc975ed542d3148f00015b)

### **Definition**  
You will be given an array a and `a` value `x`.  
All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return `true` if the array contains the value, `false` if not.

#### **Example:**
```
check([66, 101], 66) => True, ()),
check([78, 117, 110, 99, 104, 117, 107, 115], 8) => False
```
:sparkles:elem在seq中，就True

### **Given Code**
```python
def check(seq, elem):
    pass
```

### **Solution Code**
```python
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False
```

![](https://i.imgur.com/qnv6Y7W.png)

---

## Sum Mixed Array
> [See on CodeWars.com](https://www.codewars.com/kata/57eaeb9578748ff92a000009)

### **Definition**  
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

#### **Example:**
```
sum_mix([9, 3, '7', '3']) => 22
```
:sparkles:將str轉成int相加

### **Given Code**
```python
def sum_mix(arr):
    #your code here
```

### **Solution Code**
```python
def sum_mix(arr):
    s = 0
    for i in range(0,len(arr)):
        s = s+int(arr[i])
    return s
```

![](https://i.imgur.com/9fsAz7u.png)

---

## Is this my tail?
> [See on CodeWars.com](https://www.codewars.com/kata/56f695399400f5d9ef000af5)

### **Definition**  
Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be strings, and normal letters.

For Haskell, body has the type of `String` and tail has the type of `Char`.  
For Go, body has type string and tail has type rune.

#### **Example:**
```
correct_tail("Meerkat", "t") => True
correct_tail("Emu", "t") => False
```
:sparkles:

### **Given Code**
```python
def correct_tail(body, tail):
     sub = body.substr(len(body)-len(tail.length)
        if sub = tai:
    return True
        else:
    return False
```

### **Solution Code**
```python
def correct_tail(body, tail):
    c = body[len(body)-1:]
    if c == tail:
        return True
    else:
        return False
```

![](https://i.imgur.com/xEAzmyz.png)

---

## Fake Binary
> [See on CodeWars.com](https://www.codewars.com/kata/57eae65a4321032ce000002d)

### **Definition**  
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.  
Return the resulting string.

#### **Example:**
```
fake_bin("45385593107843568") => "01011110001100111"
fake_bin("345678") => "001111"
```
:sparkles:>=5 : 1 ; <5 : 0

### **Given Code**
```python
def fake_bin(x):
    pass
```

### **Solution Code**
```python
def fake_bin(x):
    ans = ''
    for i in x:
        if int(i) < 5:
            ans = ans+'0'
        else:
            ans = ans+'1'
    return ans
```

![](https://i.imgur.com/2CkTGiD.png)

---

## My head is at the wrong end!
> [See on CodeWars.com](https://www.codewars.com/kata/56f699cd9400f5b7d8000b55)

### **Definition**  
You're at the zoo... all the meerkats look weird. Something has gone terribly wrong - someone has gone and switched their heads and tails around!

Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).

Same goes for all the other arrays/lists that you will get in the tests: you have to change the element positions with the same exact logics

Simples!

#### **Example:**
```
fix_the_meerkat(["tail", "body", "head"]) => ["head", "body", "tail"]
```
:sparkles: reverse array

### **Given Code**
```python
def fix_the_meerkat(arr):
    #your code here
```

### **Solution Code**
```python
def fix_the_meerkat(arr):
    arr.reverse()
    return arr
```

![](https://i.imgur.com/JH7W3XM.png)

---

## Get Nth Even Number
> [See on CodeWars.com](https://www.codewars.com/kata/5933a1f8552bc2750a0000ed)

### **Definition**  
Return the Nth Even Number

#### **Example:**
```
1 --> 0 (the first even number is 0)
3 --> 4 (the 3rd even number is 4 (0, 2, 4))
100 --> 198
1298734 --> 2597466
```
:sparkles: 

### **Given Code**
```python
def nth_even(n):
    #your code here
```

### **Solution Code**
```python
def nth_even(n):
    return (n-1)*2
```

![](https://i.imgur.com/U9Ajumu.png)


---

## What is between?
> [See on CodeWars.com](https://www.codewars.com/kata/55ecd718f46fba02e5000029)

### **Definition**  
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

#### **Example:**
```
a = 1, b = 4 => [1, 2, 3, 4]
```
:sparkles: 

### **Given Code**
```python
def between(a,b):
    # good luck
    pass
```

### **Solution Code**
```python
def between(a,b):
    arr = []
    for i in range(a, b+1):
        arr.append(i)
    return arr
```

![](https://i.imgur.com/t23UNqA.png)

---

## DNA to RNA Conversion
> [See on CodeWars.com](https://www.codewars.com/kata/5556282156230d0e5e000089)

### **Definition**  
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.
#### **Example:**
```
"GCAT"  =>  "GCAU"
```
:sparkles: 

### **Given Code**
```python
def dna_to_rna(dna):
    return
```

### **Solution Code**
```python
def dna_to_rna(dna):
    s ='' 
    for i in dna:
        if i == 'T':
            s = s + "U"
        else:
            s = s + i
    return s
```

```python
def dna_to_rna(dna):
    arr = dna.replace('T', 'U')
    return arr
```

![](https://i.imgur.com/UuRKVA7.png)

---

## Opposites Attract
> [See on CodeWars.com](https://www.codewars.com/kata/555086d53eac039a2a000083)

### **Definition**  
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.  
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
#### **Example:**
```
lovefunc(2,2) => False
lovefunc(0,1) => True
```
:sparkles: 

### **Given Code**
```python
def lovefunc( flower1, flower2 ):
    # ...
```

### **Solution Code**
```python
def lovefunc( flower1, flower2 ):
    if (flower1+flower2)%2 != 0:
        return True
    else:
        return False
```

![](https://i.imgur.com/3G0I0Ft.png)

---

## Transportation on vacation
> [See on CodeWars.com](https://www.codewars.com/kata/568d0dd208ee69389d000016)

### **Definition**  
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs 40.  
If you rent the car for 7 or more days, you get 50 off your total.  
Alternatively, if you rent the car for 3 or more days, you get 20 off your total.
 
Write a code that gives out the total amount for different days(d).

#### **Example:**
```
rental_car_cost(4) => 140
rental_car_cost(8) => 270
```
:sparkles: 

### **Given Code**
```python
def rental_car_cost(d):
    # your code
```

### **Solution Code**
```python
def rental_car_cost(d):
    price = 0
    if d >=7:
        price = 40*d-50
    elif d >=3:
        price = 40*d-20
    else:
        price = 40*d
    return price
```

![](https://i.imgur.com/Atan9ym.png)

---

## Beginner Series #4 Cockroach
> [See on CodeWars.com](https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6)

### **Definition**  
The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

#### **Example:**
```
1.08 --> 30
```
:sparkles: 速度: km/hr => cm/s

### **Given Code**
```python
def cockroach_speed(s):
    # Good Luck!
```

### **Solution Code**
```python
def cockroach_speed(s):
    # Good Luck!
    return int((s*1000*100)/(1*60*60))
```

![](https://i.imgur.com/REb8rPy.png)





<style>.markdown-body { max-width: 1000px; }</style>
