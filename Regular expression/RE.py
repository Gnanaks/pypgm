import re

#fetching phn no.
data = ' I am Gnana my Number is 9663683661 & Father number is 9663683661'
#re.findall(r"patternns",data)
a = re.findall(r"\d",data)
print(a)
#o/p:['9', '6', '6', '3', '6', '8', '3', '6', '6', '1']

#
a = re.findall(r"\d{10}",data)
print(a)

# fetching roll number
data = ' my roll number is 1 , A roll number is 2 , B roll number is 3, C roll number is 4'
a = re.findall(r"\d+",data)
print(a)
#o/p:['1', '2', '3', '4']


