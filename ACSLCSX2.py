


def findnth(input_string, character, n):
    start = input_string.find(character)
    while start >= 0 and n > 1:
        start = input_string.find(character, start + len(character))
        n -= 1
    return start


def encodeMessage(text, message):
    
    holder = []
    
    cnt1 = 0
    while cnt1 < len(message):

        letter = message[cnt1]
        alnumtester = letter.isalnum()

        if letter == " ":
            holder.append("_")
            cnt1 = cnt1 + 1
        elif alnumtester == False and letter != " ":
            holder.append(letter)
            cnt1 = cnt1 + 1
        else:
            #instance finder FIC THIS
            cnt2 = 0
            divider = cnt1 + 1
        
            while cnt2 != "stop":
                counter = text.count(letter)
                if counter >= (divider):
                    inst = findnth(text, letter, divider)
                    cnt2 = "stop"
                else:
                    divider = int(divider / 2)
         

        #make a variable equal the sentence
        #front
            specialletter = letter + "&%$"
            specialsentenceholder = [specialletter]
            sentenceholder = [letter]

            cnt3 = 1
            while cnt3 != "stop":
                if (inst + cnt3)>= len(text):
                    cnt3 = "stop"
                else:
                    next = text[inst+cnt3]
                    if next == "." or next == "?" or next == "!":
                        specialsentenceholder.append(next) ########CHECK
                        cnt3 = "stop"
                    else: 
                        sentenceholder.append(next)
                        specialsentenceholder.append(next)
                        cnt3 = cnt3 + 1
            #back
            cnt4 = 1
            while cnt4 != "stop":
                ender = inst - cnt4
                if ender == -1:
                    cnt4 = "stop"
                else: 
                    before = text[ender]
                    if before == "." or before == "?" or before == "!":
                        cnt4 = "stop"
                    else: 
                        sentenceholder.insert(0, before)
                        specialsentenceholder.insert(0, before)
                        cnt4 = cnt4 + 1
                    
            sentenceholder = "".join(sentenceholder)
            specialsentenceholder = "".join(specialsentenceholder)

            #find sentence number
            cnt5 = 0
            punctext = [*text]
            while cnt5 <len(punctext):
                punc = text[cnt5]
                if punc == "." or punc == "?" or punc == "!":
                    punctext[cnt5] = "$%&#$&#*"
                    cnt5 = cnt5 + 1
                else:
                    cnt5 = cnt5 + 1
            
            punctext = "".join(punctext)
            sentences = punctext.split("$%&#$&#*")
            if sentences[len(sentences) -1] == "":
                sentences.pop(len(sentences) -1)
            
            s = sentences.index(sentenceholder) + 1

            #find word
            specialword = [specialletter]
            cnt6 = 1
            #front
            while cnt6 != "stop":
                if (inst + cnt6)>= len(text):
                    cnt6 = "stop"
                else:
                    another = text[inst + cnt6]
                    if another == " ":
                        cnt6 = "stop"
                    else:
                        specialword.append(another)
                        cnt6 = cnt6 + 1

            #back
            cnt7 = 1
            while cnt7 != "stop":
                ender = inst - cnt7
                if ender == -1:
                    cnt7 = "stop"
                else: 
                    again = text[ender]
                    if again == " ":
                        cnt7 = "stop"
                    else: 
                        specialword.insert(0, again)
                        cnt7 = cnt7 + 1
            
            specialword = "".join(specialword)
            specialsentenceholder = specialsentenceholder.split()
            if type(specialsentenceholder is list) == False:
                specialsentenceholder = [specialsentenceholder]
            
            w = specialsentenceholder.index(specialword) + 1

            #find c

            c = specialword.find(specialletter) + 1

            s = str(s)
            w = str(w)
            c = str(c)

            part = s + "." + w + "." + c + " "

            holder.append(part)
            cnt1 = cnt1 + 1


    answer = "".join(holder)
    cnt8 = 0
    answers = []
    while cnt8 < len(answer):
        answers.append(answer[cnt8])
        cnt8 = cnt8 + 1


    cnt9 = 0
    while cnt9 < len(answers):
        char = answers[cnt9]
        checker = char.isalnum()
        if checker == False and checker != " ":
            if answers[cnt9 - 1] == " ":
                answers.pop(cnt9 -1)
                cnt9 = cnt9 + 1
            else: 
                cnt9 = cnt9 + 1
        else:
            cnt9 = cnt9 + 1

    answers = "".join(answers)
    return answers    



def main():

    text = "ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League."
    message = "American Computer Science League (ACSL) is fun!"
    answer = encodeMessage(text, message)
    print(answer)

if __name__ == "__main__":
    main()