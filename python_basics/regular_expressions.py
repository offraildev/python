# can match and search for specific patterns of text
import re

# raw string: string prefixed with r, use: don't treat backslash (escape char) differently
print(r'sajid \t mashroor')
print('sajid \t mashroor')

text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# exact number of chars specificition  
pattern = re.compile(r'\d{3}[^.-]\d{3}[^.-]\d{4}')

# range of chars needed, works for range of alphabets also
pattern = re.compile(r'[4-9]\d{2}.\d{3}.\d{4}')

# match only letters of lower and uppercase
pattern = re.compile(r'[j-vJ-V]')

# match the names with titles
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# match groups 
pattern  = re.compile(r'(Mr|Ms|Mrs)(\.?\s[A-Z]\w*)')

# match emails
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z.-]+\.(com|edu|net)')

# capturing data using groups 
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# to sub a pattern in a string using back reference to captured gropus 
subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# finditer returns an iterator object of the matches
# each object contains other useful info like char location,etc
matches = pattern.finditer(urls)

# findall returns only the matches or if groups are present,
# returns the groups only of tuple of multiple groups
matches = pattern.findall(text_to_search)

for match in matches:
    print(match)

for match in matches:
    # by default the 0th group is the pattern matched
    print(f'group_0:{match.group(0)}\tgroup_1:{match.group(1)}\tgroup_2:{match.group(2)}\tgroup_3:{match.group(3)}') # match object


sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'Start')

# match on search at the begining of string, return first match or else return None
print(pattern.match(sentence))

pattern = re.compile(r'dne')

# search matches everywhere in the string, return None if not found
print(pattern.search(sentence))

# flags example: ignorecase, instead of typing [Ss][Tt]... ignore case
pattern = re.compile(r'start', re.I)
print(pattern.match(sentence))
