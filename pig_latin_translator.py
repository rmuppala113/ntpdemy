user_inpt = input("Please enter you sentence: ")
words_list = user_inpt.strip().split()
myword = []
for i in words_list:
    latin = i[:2]
    pig = i[2:]
    mylang = pig + latin + "ay"
    x = myword.append(mylang)
print("\n{}\n".format(" ".join(myword)))
