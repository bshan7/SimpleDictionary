import json
from difflib import get_close_matches 

data = json.load(open(r"C:\Users\downloads\original.json","r"))  #specify the exact location of the original.json file
while True:
    word=input("Enter your word: ")
    output={}
    if word in data:
        data[word]
        output=data[word]
    else :
        if word is not word.lower():
            word = word.lower()
        else:
            word = word.high()
        if word in data:
            output=data[word]
    print()
    if not output:
        print("Your Word Is Not In The Dictionary!!Try Again.")
        match = get_close_matches(word,data.keys())
        if match:
            print("Do you want to Try Using these?")
            for i in range(len(match)):
                print(str(i+1)+"."+str(match[i]))
        choice=input("What do You want? Type The Number: ")
        if choice.isnumeric():
            if int(choice) <= len(match):
                PerfectMatch=match[int(choice)-1]
                count = 1
                for i in data[PerfectMatch]:
                    print(str(count)+"."+str(i))
                    count+=1
        elif  choice in match:
            count = 1
            for i,value in enumerate (match):
                if value == choice :
                    for k in data[match[i]]:
                        print(str(count)+"."+ str(k))
                        count+=1

        else :
            continue

    else:
        for i in range(len(output)):
            print (str(i+1)+"."+str(output[i]))
    print("\nWhether you want to continue(y/n):")
    ans=input()
    if (ans == ('y' or 'Y')):
        continue
    else:
        break
