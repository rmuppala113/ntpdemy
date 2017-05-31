from random import choice

questions = ["Why is rainbow has 7 colors? :","Why is sky Blue?: ","Why is grandma in moon selling vadas?: ",
             "What shape is earth?: "]
question  = choice(questions)
answer = raw_input(question).strip().lower()
while answer != "because":
    answer = raw_input("why?: ").strip().lower()
print("Oh........Okayyyyyyiii")