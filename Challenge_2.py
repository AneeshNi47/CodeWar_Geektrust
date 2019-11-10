import random

usage_count = 0
kingdoms = ["space", "land", "water", "ice", "air", "fire"]
kings = {'space': 'gorilla', 'land': 'panda', 'water': 'octopus', 'ice': 'mammoth', 'air': 'owl', 'fire': 'dragon'}
random_messages = ["Summer is coming",
                   "a1d22n333a4444p",
                   "oaaawaala",
                   "zmzmzmzaztzozh",
                   "Go, risk it all",
                   "Let's swing the sword together",
                   "Die or play the tame of thrones",
                   "Ahoy! Fight for me with men and money",
                   "Drag on Martin!",
                   "When you play the tame of thrones, you win or you die.",
                   "What could we say to the Lord of Death? Game on?",
                   "Turn us away, and we will burn you first",
                   "Death is so terribly final, while life is full of possibilities.",
                   "You Win or You Die",
                   "His watch is Ended",
                   "Sphinx of black quartz, judge my dozen vows",
                   "Fear cuts deeper than swords, My Lord.",
                   "Different roads sometimes lead to the same castle.",
                   "A DRAGON IS NOT A SLAVE.",
                   "Do not waste paper",
                   "Go ring all the bells",
                   "Crazy Fredrick bought many very exquisite pearl, emerald and diamond jewels.",
                   "The quick brown fox jumps over a lazy dog multiple times.",
                   "We promptly judged antique ivory buckles for the next prize.",
                   "Walar Morghulis: All men must die."]
space_allies = []
land_allies = []
water_allies = []
ice_allies = []
air_allies = []
fire_allies = []

ruler_allies = []
ruler = None


def user_messages(usage_count, ruler):   # function to display messages to user
    if usage_count == 0:
        print("Greetings User!")
        print("Welcome to the Kingdom")
        print("Ruler of Southeros is {0}".format(ruler))
        print("Allies of the Ruler are:{0}".format(ruler_allies))
    elif king is None and usage_count != 0:
        print("Greetings Once again King!")
        print("Sadly the you dint not gain enough Allies to Rule Southeros")
        response = input("Would you like to send out message again? [y] or [n]")
        if response == 'y' or response == 'Y':
            main()
        else:
            print("Good Day King Shan!")
    else:
        print("Greetings once again King Shan!")
        print("Ruler of Southeros is {0}".format(ruler))
        print("Allies of the Ruler are:{0}".format(ruler_allies))


def message_process(kingdom, message):  # function tp process message to kingdom and check for the condition
    flag = 0
    # print("Message to {0} kingdom : ".format(kingdom), message)
    split_msg = list(message)
    split_animal = list(Dict[kingdom])
    for i in range(len(split_animal)):
        for j in range(len(split_msg)):
            if split_animal[i] == split_msg[j]:
                flag = 1
                break
            else:
                flag = 0
    return flag


print(random_messages[random.randrange(0, len(random_messages))])


def main():
    global usage_count
    usage_count = 0
    # user_messages(usage_count, ruler)
    competing_kingdoms = input("Select Kingdoms to enter competing (space, land, water, ice, air, fire): ")
    competing_kingdoms_split = competing_kingdoms.split(" ")
    print(kings)





if __name__ == "__main__":
    main()