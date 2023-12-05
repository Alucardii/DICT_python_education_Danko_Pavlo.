import random

def add_friends():
    names = ["Паша", "Артём", "Петя", "Богдан", "Влад"]
    num_friends = int(input("Enter the number of friends joining (including you):\n"))

    if num_friends <= 0:
        print("No one is joining for the party")
        return

    friends_list = names[:num_friends] + [input(f"> {friend}\n") for friend in range(len(default_names), num_friends)]
    friends_dict = {friend: 0 for friend in friends_list}

    total_amount = float(input("Enter the total amount:\n"))

    share_person = round(total_amount / num_friends, 2)

    for friend in friends_dict:
        friends_dict[friend] = share_person

    lucky_feature = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n").lower()

    print(friends_dict)

    if lucky_feature == "yes":
        lucky_one = random.choice(list(friends_dict.keys()))
        print(f"{lucky_one} is the lucky one!")
        friends_dict[lucky_one] = 0

        remaining_friends = [friend for friend in friends_dict if friend != lucky_one]
        remaining_share_per_person = round(total_amount / (num_friends - 1), 2)

        for friend in remaining_friends:
            friends_dict[friend] = remaining_share_per_person

        print(friends_dict)
    else:
        print("No one is going to be lucky")
        print(friends_dict)

add_friends()