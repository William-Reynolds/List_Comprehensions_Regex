# By: Billy Reynolds
import re
print("LIST COMPREHENSIONS\n-------------------------------------------------------------")
firstSentence = ["Help", "me", "stack", "overflow", "you're", "my", "only", "hope"]
secondSentence = ["I", "hope", "you're", "enjoying", "the", "riddles", "I've", "created"]
print("TEST: ",[x for x in firstSentence] )
print("1: ", [x for x in firstSentence + secondSentence if len(x) > 4])
print("2: ", [x for x in firstSentence + secondSentence if x.find("o") == 0])
print("3: ", [x[len(x)-3:] for x in firstSentence], "FIX")
print("4: ", [x for x in firstSentence + secondSentence if len(x)%2 == 1])
print("5: ", [secondSentence.index(x) for x in secondSentence if len(x)%2 == 1])
print("6: ", [x for x in firstSentence + secondSentence if x.find("y")>=0])
print("7: ",[x +", "+ y for x in firstSentence for y in firstSentence if (len(x) == 2*len(y)) and firstSentence.index(x)*2 == firstSentence.index(y)])
print("8: ", [(x) for x in firstSentence for y in secondSentence if x is y])
print("9: ", [(x.capitalize()) for x in firstSentence])
print("10: ", [x.replace("o","aa") for x in firstSentence])
print("11: ", [(x,y) for x in firstSentence[4:] for y in secondSentence[4:] if firstSentence.index(x) == secondSentence.index(y)])
print("12: ", [(x,y) for x in firstSentence for y in secondSentence if x is y])
print("13: ", [x+y for x in firstSentence for y in secondSentence if len(firstSentence[firstSentence.index(x)])>len(secondSentence[secondSentence.index(y)])])
print("14: ", [(firstSentence.index(x)) for x in firstSentence for y in secondSentence if 'e' in x and 'e' in y and x.rfind('e') == y.rfind('e') and x is not y and len(x)<7])
print("15: ", [(x[:1],y[:1]) for x in firstSentence for y in secondSentence])
print("REGEX\n","------------------------------------------------------------")

file = open("lowerwords.txt", "r")
list =[]
for line in file:
    list.append(line)
def filterList(str):
    p =[]
    for line in str:
        if re.search(r'[e]$',line):
            p.append(line)
    return p
print("1: ", len(filterList(list)), "words ending in e\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^[a-z]{3}[d]$', line):
            q.append(line)
        
    return q
print("2: ",len(filterList(list)), "4 letter words ending in d\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^[aeiou]', line):
            q.append(line)
        
    return q

print("3: ", len(filterList(list)), "words staring with a vowel\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'[aeiou]{2}$', line):
            q.append(line)
        
    return q

print("4: ", len(filterList(list)), "words ending with 2 vowels\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^[a][a-z]*[a]$|^[e][a-z]*[e]$|^[i][a-z]*[i]$|^[o][a-z]*[o]$|^[u][a-z]*[u]$', line):
            q.append(line) #Probably not the most efficient way, but it works
        
    return q

print("5: ", len(filterList(list)), "starting and ending with the same vowel\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^.*[aeiou]{4}.*$', line):
            q.append(line)
        
    return q
print("6: ", len(filterList(list)), "words that contain 4 consecutive vowels\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^.*(er).*\1.*\1.*$', line):
            q.append(line)
        
    return q
print("7: ", len(filterList(list)), "words with 3 instancs of 'er'\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^.*(\w\w).*\1.*\1.*$', line):
            q.append(line)
        
    return q

print("8: ",len(filterList(list)), "words with a set of 2 letters repeating three times\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^.*(\w)(\w).*(\2)(\1).*$', line):
            q.append(line)
        
    return q

print("9: ", len(filterList(list)), "words with a substring and its subsequent reversal\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^.*(\w)\1.*(\w)\2.*(\w)\3.*$', line):
            q.append(line)
        
    return q

print("10: ", len(filterList(list)), "words with 3 sets of double letters\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^.*(\w)(\w)\1.*\1\2\1.*$', line):
            q.append(line)
        
    return q

print("11: ", len(filterList(list)), "words that have a triple that appears twice\n")

def filterList(ball):
    q = []
    for line in ball: 
        if re.search(r'^.*(\w)(\w)\1(\w)(\w)\3(\w)(\w)\5.*$', line):
            q.append(line)
        
    return q

print("12: ", len(filterList(list)), "words that have a triple that appears three consecutive times\n")