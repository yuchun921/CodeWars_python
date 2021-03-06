# Python Codewars Solution - 8kyu(1)

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

