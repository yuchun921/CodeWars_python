# Python Codewars Solution - 8kyu(2)

> [name=Liu, Yu-Chun] [time=Tue, Apr 26, 2021 09:24 PM]
###### tags: `Python` `codewars`

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

---

## Invert values
> [See on CodeWars.com](https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad)

### **Definition**  
Given a set of numbers, return the additive inverse of each.  
Each positive becomes negatives, and the negatives become positives.

#### **Example:**
```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```
:sparkles: 

### **Given Code**
```python
def invert(lst):
    pass
```

### **Solution Code**
```python
def invert(lst):
    arr = []
    for i in range(0,len(lst)):
        i = lst[i]*(-1)
        arr.append(i)
    return arr
```

![](https://i.imgur.com/8SQymuP.png)

---

## Find numbers which are divisible by given number
> [See on CodeWars.com](https://www.codewars.com/kata/55edaba99da3a9c84000003b)

### **Definition**  
Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of `numbers` and the second is the `divisor`.

#### **Example:**
```
divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
```
:sparkles: 

### **Given Code**
```python
def divisible_by(numbers, divisor):
    pass
```

### **Solution Code**
```python
def divisible_by(numbers, divisor):
    arr = []
    for i in range(0, len(numbers)):
        if numbers[i]%divisor == 0:
            arr.append(numbers[i])
    return arr
```

![](https://i.imgur.com/XcweOe8.png)

---

## I love you, a little , a lot, passionately ... not at all
> [See on CodeWars.com](https://www.codewars.com/kata/57f24e6a18e9fad8eb000296)

### **Definition**  
Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

* I love you
* a little
* a lot
* passionately
* madly
* not at all  

When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where `nb_petals > 0`

#### **Example:**
```
how_much_i_love_you(3) => 'a lot'
how_much_i_love_you(6) => 'not at all'
```
:sparkles: 

### **Given Code**
```python
def how_much_i_love_you(nb_petals):
    # your code
```

### **Solution Code**
```python
def how_much_i_love_you(nb_petals):
    if nb_petals % 6 == 0:
        return "not at all"
    elif nb_petals % 6 == 1:
        return "I love you"
    elif nb_petals % 6 == 2:
        return "a little"
    elif nb_petals % 6 == 3:
        return "a lot"
    elif nb_petals % 6 == 4:
        return "passionately"
    elif nb_petals % 6 == 5:
        return "madly"
```


:arrow_down_small: 別種解法
```python
def how_much_i_love_you(nb_petals):
    dic = {
        0:"not at all",
        1:"I love you",
        2:"a little",
        3:"a lot",
        4:"passionately",
        5:"madly"
    }
    return dic[nb_petals%6]
```

![](https://i.imgur.com/z6vRRZM.png)

---

## Convert a string to an array
> [See on CodeWars.com](https://www.codewars.com/kata/57e76bc428d6fbc2d500036d)

### **Definition**  
Write a function to split a string and convert it into an array of words.

#### **Example:**
```
"Robin Singh" ==> ["Robin", "Singh"]
"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
```
:sparkles: 

### **Given Code**
```python
def string_to_array(s):
    # your code here
```

### **Solution Code**
```python
def string_to_array(s):
    return s.split(" ")
```

![](https://i.imgur.com/wZi1IPM.png)

---

## Can we divide it?
> [See on CodeWars.com](https://www.codewars.com/kata/577a98a6ae28071780000989)

### **Definition**  
Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.

#### **Example:**
```
(45, 1, 6)    ->  false
(45, 5, 15)   ->  true

(4, 1, 4)     ->  true
(15, -5, 3)   ->  true
```
:sparkles: 

### **Given Code**
```python
def is_divide_by(number, a, b):
    return # good luck
```

### **Solution Code**
```python
def is_divide_by(number, a, b):
    if number%a==0 and number%b==0:
        return True
    else:
        return False
```

![](https://i.imgur.com/wZi1IPM.png)

---

## Find Maximum and Minimum Values of a List
> [See on CodeWars.com](https://www.codewars.com/kata/5a2b703dc5e2845c0900005a)

### **Definition**  
Your task is to make two functions, `max` and `min` (`maximum` and `minimum` in PHP and Python, maxi and mini in Julia) that take a(n) array/vector of integers `list` as input and outputs, respectively, the largest and lowest number in that array/vector.

#### **Example:**
```
maximun([4,6,2,1,9,63,-134,566]) => 566
minimun([-52, 56, 30, 29, -54, 0, -110]) => -110
maximun([5]) => 5
minimun([42, 54, 65, 87, 0]) => 0
```
:sparkles: 

### **Given Code**
```python
def minimum(arr):
    #your code here...

def maximum(arr):
    #...and here
```

### **Solution Code**
```python
def minimum(arr):
    minN = min(arr)
    return minN

def maximum(arr):
    maxN = max(arr)
    return maxN
```

![](https://i.imgur.com/wC9cssB.png)

---

## Count of positives / sum of negatives
> [See on CodeWars.com](https://www.codewars.com/kata/576bb71bbbcf0951d5000044)

### **Definition**  
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

#### **Example:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15] => [10, -65]
```
:sparkles: 

### **Given Code**
```python
def count_positives_sum_negatives(arr):
    #your code here
```

### **Solution Code**
```python
def count_positives_sum_negatives(arr):
    p = 0
    n = 0
    ar = []
    if len(arr) == 0:
        return ar
    for i in range(0, len(arr)):
        if arr[i] > 0:
            p = p+1
        elif arr[i] < 0:
            n = n+arr[i]
    ar.append(p)
    ar.append(n)
           
    return ar
```

![](https://i.imgur.com/wC9cssB.png)

---

## Remove String Spaces
> [See on CodeWars.com](https://www.codewars.com/kata/57eae20f5500ad98e50002c5)

### **Definition**  
Simple, remove the spaces from the string, then return the resultant string.

#### **Example:**
```
no_space('8aaaaa dddd r     ') => '8aaaaaddddr
```
:sparkles: 

### **Given Code**
```python
def no_space(x):
    #your code here
```

### **Solution Code**
```python
def no_space(x):
    return x.replace(" ",'')
```

:arrow_down_small: 
```python
def no_space(x):
    char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            char = char + x[i]
    return char
```

![](https://i.imgur.com/4wWmcsj.png)

---

## Merge two sorted arrays into one
> [See on CodeWars.com](https://www.codewars.com/kata/5899642f6e1b25935d000161)

### **Definition**  
You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.

#### **Example:**
```
arr3 = [1, 3, 5, 7, 9];
arr4 = [10, 8, 6, 4, 2];
merge_arrays(arr3, arr4);  // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
:sparkles: 

### **Given Code**
```python
def merge_arrays(arr1, arr2):
    pass
```

### **Solution Code**
```python
def merge_arrays(arr1, arr2):
    result = []
    for i in arr1:
        if i not in result:
            result.append(i)
    for i in arr2:
        if i not in result:
            result.append(i)
    result.sort()
    return result
```

:arrow_down_small: 
```python
def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))
```

![](https://i.imgur.com/Yjv6xSQ.png)


<style>.markdown-body { max-width: 1000px; }</style>
