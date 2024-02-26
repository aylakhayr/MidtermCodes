#question1
a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)

#question2
print((2+3)*6/2 and 18.0)

#question3
import datetime
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

#question4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
numbers = [
    "6892149109325320763773670235239019412986",
    "6800923757255865070000705685527573290086",
    "9847255590886266818998186626880955527489",
    "1414884937242655719669145562427394884141"
]
not_palindromes = []
for num in numbers:
    if not palindrome(num):
        not_palindromes.append(num)

print("Numbers that are not palindromes:", not_palindromes)

#question5
def find_pattern_occurrences(text):
    count = 0
    for i in range(len(text)):
        if text[i:i + 2] == 'un':
            if 'an' in text[i + 2:]:
                count += 1
    return count
text = "i hope i pass my programming midterm with no misunderstandings"
print("Number of occurrences:", find_pattern_occurrences(text))

#question6
  #for list
my_list = [1, 2, 3, 4]
print("Original list:", my_list)
my_list[2] = 99
print("Modified list:", my_list)
my_list.append(5)
print("List after adding an element:", my_list)
my_list.remove(99)
print("List after removing an element:", my_list)
  #for string
my_string = "hello"
print("Original string:", my_string)
modified_string = my_string.replace("e", "a")
print("Modified string:", modified_string)

#question7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
modified_numbers = []
for number in random_numbers:
    if number % 2 == 0:
        modified_numbers.append(number * 2)
print(modified_numbers)

#question8
def is_valid_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        if "." in url:
            if url.rfind(".") > url.find("//") + 2:
                return True
    return False
print(is_valid_url("http://example.com"))
print(is_valid_url("https://example"))
print(is_valid_url("example.com"))

#question9
def calculate_days_since_birthday():
    birthday = input("Enter your birthday (DD-MM-YYYY): ")
    year = int(birthday.split("-")[2])
    current_year = int(input("Enter the current year (YYYY): "))
    full_years_since_birthday = current_year - year - 1
    days = full_years_since_birthday * 365
    print(
        f"Approximately {days} days have passed since your birthday, not including the days in your birth year and the current year.")
calculate_days_since_birthday()

