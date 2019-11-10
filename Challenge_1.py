class Kingdom:
    def __init__(self, name, king, allies):
        self.kingdom_name = name
        self.kingdom_king = king
        self.kingdom_logo = king
        self.kingdom_allies = allies


space = Kingdom('Space', 'Gorilla', None)

usage_count = 0


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


def user_messages(usage_count, king):  # function to display messages to user
    if usage_count == 0:
        print("Greetings King Shan!")
        print("Welcome to the Kingdom")
        print("Ruler of Southeros is {0}".format(king))
        print("Allies of the Ruler are:{0}".format(space_allies))
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
        print("Ruler of Southeros is {0}".format(king))
        print("Allies of the Ruler are:{0}".format(space_allies))


def main(king=None):
    n = 0
    global usage_count
    usage_count = 0
    user_messages(usage_count, king)
    while n <= 4:
        kingdom = input("Select Kingdom to send message (space, land, water, ice, air, fire): ")
        kingdom = kingdom.lower()  # converts inputs to specific case to simply processing
        if kingdom in Dict:
            message = input("Enter the Message from {0} Kingdom: ".format(kingdom))
            allies_test = message_process(kingdom, message)  # passes message and selected kingdom name to function
            if allies_test:  # checks if the kingdom is and allie with value from the function
                space_allies.append(kingdom)  # Adds the kingdom to Allies if found conditions is true
            if len(space_allies) >= 3:
                king = "Gorilla"  # if more than 3 allies is found Gorilla King is made the ruler
            n += 1
        else:
            print("Invalid input! ")
    usage_count += 1  # count to keep track of trials
    user_messages(usage_count, king)


if __name__ == "__main__":
    main()
