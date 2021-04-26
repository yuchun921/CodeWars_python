# Python Codewars Solution - 8kyu

> [name=Liu, Yu-Chun] [time=Tue, Apr 26, 2021 09:24 PM]
###### tags: `python` `codewars`

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
> 
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
