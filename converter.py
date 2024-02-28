'''
Created on Dec 1, 2023

@author: CCaliboso24
'''

def findnth(input_string, character, n):
    start = input_string.find(character)
    while start >= 0 and n > 1:
        start = input_string.find(character, start + len(character))
        n -= 1
    return start

def main():
    text = "mmmm. fart."
    letter = "m"
    
    cnt1 = 9
    cnt2 = 0
    divider = cnt1
    while cnt2 != "stop":
        counter = text.count(letter)
        if counter >= (divider):
            inst = findnth(text, letter, divider)
            cnt2 = "stop"
        else:
            divider = int(divider / 2)
    
    print(inst)

if __name__ == "__main__":
    main()