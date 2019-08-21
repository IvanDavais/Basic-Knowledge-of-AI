# This list is for storing all cards.
card_list = []


def display_menu():

    """Display menu"""
    print("*"*50)
    print("")
    print("Welcome to Electronic Card Management System")
    print("")
    print("1. Add new Electronic card")
    print("2. Display all Electronic cards")
    print("3. Search Electronic card")
    print("")
    print("0. Exit")
    print("*"*50)


def new_card():

    """Add new card"""
    print("-" * 50)
    print("Added new Card.")

    # 1.Tell user enter the detailed information for the electronic card
    print("Please enter your personal information: ")
    name_str = input("Your name: ")
    phone_str = input("Your phone: ")
    s = input("Your QQ: ")
    qq_str = s
    email_str = input("Your e-mail: ")

    # 2.Define a dictionary to store the users' information
    card_dic = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "email": email_str}

    # 3.Store the dictionary above in the list
    card_list.append(card_dic)

    # 4.Notice users have successful stored individual information in the system
    print("-" * 50)
    # print(card_list)
    print("Congratulations, you had successful added your personal information in this system.")


def show_all():

    """Display all cards information"""

    # 1.if this table is empty, notice users some necessary information.
    if len(card_list) == 0:
        print("Sorry, Nobody store information in this system.")
        return

    # 2.print the header
    print("=" * 50)
    for header in ["Name", "Phone", "QQ", "Email"]:
        print(header, end="\t\t\t")

    print("")
    print("=" * 50)

    # 3.print contend
    for card_dic in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t%s" %(card_dic["name"],
                                           card_dic["phone"],
                                           card_dic["qq"],
                                           card_dic["email"]))


def search_card():

    """Search card"""
    name_searched = input("please enter the name you want to search: ")

    for name_dic in card_list:
        if name_dic["name"] == name_searched:
            print("=" * 50)

            # print the header, notice it's different from the above header print way.
            print("Name\t\tPhone\t\tQQ\t\tEmail")
            print("=" * 50)

            # print the detailed card information
            print("%s\t\t%s\t\t%s\t\t%s" % (name_dic["name"],
                                            name_dic["phone"],
                                            name_dic["qq"],
                                            name_dic["email"]))
            print("=" * 50)

            # invoke deal_card function which modify,delete card information.
            deal_card(name_dic)

            break
    # if this card didn't existed in this system, tell this truth to the user.
    else:
        print("")
        print("=" * 50)
        print("I am sorry, we don't find %s " % name_searched)


def deal_card(find_dic):
    """
    This function is for deal with the card had searched, user can continue to process next step like
    modify card, delete card and return main menu.
    :param find_dic: the card that user had found out.
    """
    #print(find_dic)
    action_str = input(("please choose your operation:"
                        "\n[1].Modify [2]Delete [3]Return main menu: "))
    if action_str == "1":
        print("")
        print("Enter: No Modify")
        print("")
        find_dic["name"] = input_card_info(find_dic["name"], "your name: ")
        find_dic["phone"] = input_card_info(find_dic["phone"], "your phone: ")
        find_dic["qq"] = input_card_info(find_dic["qq"], "your qq: ")
        find_dic["email"] = input_card_info(find_dic["email"], "your email: ")
        print("Congratulation, you had modified your information. ")
    elif action_str == "2":
        card_list.remove(find_dic)
        print("Deleted card information of %s" % find_dic["name"])


def input_card_info(dict_info,tip_message):
    """
    This function change the original input method that user can choice input or input nothing.
    :param dict_info: original value in dictionary
    :param tip_message: tip information for user when they are modifying
    :return: if user enter information,then return this information;
    if user did't enter anything, return the original value in dictionary.

    """
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_info
