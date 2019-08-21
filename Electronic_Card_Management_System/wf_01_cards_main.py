#! /usr/bin/python3

import Basic_Python.Electronic_Card_Management_System.wf_02_cards_tools


# while true is called dead loop, which used in customer choice for stop loop.
while True:
    Basic_Python.Electronic_Card_Management_System.wf_02_cards_tools.display_menu()
    # TODO(Ivan) Display functions menu.

    action_str = input("Select the function you want to perform: ")
    print("The function you choose is: %s" % action_str)

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            Basic_Python.Electronic_Card_Management_System.wf_02_cards_tools.new_card()
        elif action_str == "2":
            Basic_Python.Electronic_Card_Management_System.wf_02_cards_tools.show_all()
        elif action_str == "3":
            Basic_Python.Electronic_Card_Management_System.wf_02_cards_tools.search_card()

    elif action_str == "0":
        print("Thanks for using it.Bye!")
        break

    else:
        print("Your input is wrong, please retype it.")

