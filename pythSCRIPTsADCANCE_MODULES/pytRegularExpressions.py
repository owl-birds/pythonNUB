'''
part1
'''
print("dog" in "my dog is alive")
'''
what if we only looking for pattern structure of the 
string? like an email or phone number
'''
# regex : allow us to search for general patterns in text
# data
'''
for example : an email
email format
 "text" + "@" + "text" + ".com"
'''
# @ and .com is the same for any emails based on our 
# data 

'''
re library : allow us to create sepcialized pattern strings 
and then search for matches within text
'''
# focus n understanding how to look up the information
'''
ex phone number : (555)-555-5555
regex pattern : r"(\d\d\d)-\d\d\d-\d\d\d\d"
d : digit
another : r"(\d{3})-\d{3}-\d{4}"
'''
text1 = "my phone's number is 409-902-2222 CALL ME!"
print("phone" in text1)
import re
pattern = "phone"
print(re.search(pattern, text1))
print(text1[3:8])
pattern = "Not IN TEXT1"
print(re.search(pattern, text1))
pattern = "phone"
# only getting the first match FOUND
text2 = "my phone is another phone what phone" 
match1 = re.search(pattern, text2)
print(match1)
matches = re.findall(pattern, text2)
print(matches)
print("how many matches : " + str(len(matches)))
for match in re.finditer(pattern, text2):
    print(match.span())
    print(text2[match.start():match.end()])
# ABOVE FOR BASIC STRING

# Character	Description	    Example Pattern Code	Exammple Match
# \d	    A digit	         file_\d\d	           file_25
# \w	    Alphanumeric	    \w-\w\w\w	         A-b_1
# \s	    White space	        a\sb\sc	             a b c
# \D	    A non digit	        \D\D\D	              ABC
# \W    	Non-alphanumeric	\W\W\W\W\W	        *-+=)
# \S	    Non-whitespace	    \S\S\S\S	         Yoyo
text = "My phone nnumber is 408-555-1234"
phone = re.search("408-555-1234", text)
print(phone)
print(phone.group())
phone1 = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
print(phone1)
print(phone1.group())
# Character	Description	Example     Pattern Code	Exammple Match
# +	    Occurs one or more times	Version \w-\w+	Version A-b1_1
# {3}	Occurs exactly 3 times	    \D{3}	        abc
# {2,4}	Occurs 2 to 4 times	         \d{2,4}	    123
# {3,}	Occurs 3 or more	        \w{3,}	        anycharacters
# \*	Occurs zero or more times	A\*B\*C*	    AAACC
# ?	    Once or none	            plurals?	    plural
phone2 = re.search(r"\d{3}-\d{3}-\d{4,}", text)
print(phone2)
print(phone2.group())
phonePattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
phone3 = re.search(phonePattern, text)
print(phone3)
print(phone3.group())
print(phone3.group(1))
print(phone3.group(2))
print(phone3.group(3))
#print(phone3.group(4)): ERROR just 3 groups exist

'''
Additional Regex Syntax
'''
print(re.search(r"cat|dog", "The dog is here"))
print(re.findall(r"...at", "The cat in the hat sat there and went splat"))
print(re.findall(r".at", "The cat in the hat sat there"))

'''
starts and ends with
'''
# ENDS with num
print(re.findall( r"\d$", "this ends with number 9"))
# starts with num
print(re.findall(r"^\d", "1 is three minus two"))

phrase = "there are 3 numbers 34 inside 5 this sentence"
pattern = r"[^\d ]+"
print(re.findall(pattern, phrase))
testPhrase = "This is a string! But it has punctuation. How can we remove it?"
print(re.findall(r"[^!.? ]+", testPhrase))
clean = re.findall(r"[^!.? ]+", testPhrase)
print(" ".join(clean))

text = "Only find the hypen-words in this sentence. But you do not know how long-ish they are"
pattern = r"[\w]+-[\w]+"
print(re.findall(pattern, text))
text = "my email is owlisbird@gmail.com"
pattern = r"[\w]+@[\w]+[\W][\w]+" # EMAIL PATTERN
print(re.findall(pattern, text))
text = "catfish hmmmm ok some kind of fisf catnap hmmm some kind of plant caterpillar some kind of insect"
pattern = r"cat(fish|nap|erpillar)"
print(re.search(pattern, text))
