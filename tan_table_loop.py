#!/usr/bin/env python3
# Created by: Katie G
# Created on: November 30th, 2022
# This program will ask the user what language they
# wish to use the program in, out of the options of english
# and french, and then the program will ask them to choose one
# extra function; either converting an angle to a tan value, or
# converting a tan value to an angle. Then, the program
# will get either the user's tan value or the user's angle in radians,
# and calculate the angle or the tan value respectively. Then,
# the program will use a while... loop to calculate the tan value of
# every single angle from 0 - 360. Every variable is subjected to
# a try...catch statement to make sure that erroneous data is not
# permitted, in both languages.
import math


# this function gets the user's language choice, their function choice,
# the angle or tan value depending on the choice, then calculates the
# inverse. This function will then use a while... loop to calculate
# the tan value for every angle from 0-360, in radians. Error checking
# is included for every variable.
def main():
    # initializing the counter and calculated_tan_loop variables
    # for the while...loop later on.
    counter = 0
    calculated_tan_loop = 0

    # getting the user's language choice.
    user_lang_choice = input(
        "Good day my friend! / Bonjour mon ami! What language "
        "would you like this program to run in? Type “en” for English "
        "and “fr” for French! / Dans quelle langue voulez-vous "
        "que ce programme fonctionne? "
        "Entrée “en” pour Anglais et “fr” pour Français! "
    )

    # if statement to make sure the user did not enter erroneous data.
    if user_lang_choice == "en" or user_lang_choice == "fr":
        if user_lang_choice == "en":
            # a little introduction text to describe
            # how the program works.
            print(
                "Thank you for choosing your language - you’ve chosen English! "
                "First, please be advised that this program runs in radians, "
                "as that is what Python and C++ operate in."
            )

            # getting the user's function choice
            user_function_choice = input(
                "Now, please select which function you would like the program to run! "
                "Enter “1” if you would like to input the angle and get the tan value, "
                "and enter “2” if you would like to input the tan value and get "
                "the corresponding angle! Please be advised: both options will generate the full "
                "tan table. This is simply an extra functionality option: "
            )

            # a try...catch statement to make sure the user input is a valid int.
            try:
                user_function_choice_int = int(user_function_choice)
                # if statement to make sure the user function choice is either 1 or 2.
                if user_function_choice_int == 1 or user_function_choice_int == 2:
                    if user_function_choice_int == 1:
                        # text confirming/restating user's choice and
                        # describing what will happen in this section.
                        print(
                            "Thank you for choosing your function! You’ve chosen '1'; "
                            "inputting an angle and getting the corresponding tan value "
                            "as your extra functionality piece! "
                        )

                        # getting the user's angle.
                        user_angle = input(
                            "Now, please input the angle in radians you "
                            "would like to get the tan value of: "
                        )

                        # try...catch statement making sure user angle is a valid int.
                        try:
                            user_angle_int = int(user_angle)
                            # if...statement making sure user angle is between 0 and 360.
                            if user_angle_int >= 0 and user_angle_int <= 360:
                                # calculates the tan value of the user's angle.
                                user_calculated_tan = math.tan(user_angle_int)

                                # displays the tan value of the user's angle back to the user.
                                print(
                                    "With the angle {}, your tan value is {}, in radians.".format(
                                        user_angle_int, user_calculated_tan
                                    )
                                )
                            else:
                                print("Please enter a valid integer from 0 - 360!")
                        except Exception:
                            print("Please enter a valid integer!")
                    else:
                        # text confirming/restating the user's function choice, and
                        # describing what will happen during this section.
                        print(
                            "Thank you for choosing your function! You’ve chosen '2'; "
                            "inputting a tan value and getting the corresponding angle "
                            "as your extra functionality piece!"
                        )

                        # getting the user's tan value.
                        user_tan = input(
                            "Now, please input the tan value in radians "
                            "you would like to get the angle of: "
                        )

                        # try..catch to make sure the user's tan value is a valid float.
                        try:
                            user_tan_float = float(user_tan)
                            # calculates the angle of the user's tan value.
                            user_calculated_angle = math.atan(user_tan_float)

                            # displays the calculated angle of the user's tan value
                            # back to the user.
                            print(
                                "With the tan value {}, your angle is {} in radians.".format(
                                    user_tan_float, user_calculated_angle
                                )
                            )
                        except Exception:
                            print("Please enter a valid number (decimals accepted!)")
                else:
                    print("Please enter either 1 or 2!")
            except Exception:
                print("Please enter a valid integer!")
        else:
            # a little introduction text to describe
            # how the program works, but in french.
            print(
                "Merci d’avoir choisi votre langue - vous avez choisi le Français! "
                "Tout d’abord, il faut que vous savez que ce programme fonctionne "
                "en radians, car c’est dans laquelle que Python et C++ fonctionnent."
            )

            # getting the user's function choice in french.
            user_function_choice = input(
                "Maintenant, veuillez sélectionnez la fonction que vous voulez "
                "que le programme se fait! Entrez '1' si vous voulez entrer l’angle "
                "et obtenir la valeur tangente, et entrez '2' si vous voulez entrer "
                "la valeur tangente et obtenir l’angle correspondant! "
                "Veuillez noter que les deux options généreront la table de tangente complète. "
                "Il s’agit simplement d’une option de fonctionnalité supplémentaire: "
            )
            # a try...catch statement to make sure the user input is a valid int.
            try:
                user_function_choice_int = int(user_function_choice)
                # if statement to make sure the user function choice is either 1 or 2.
                if user_function_choice_int == 1 or user_function_choice_int == 2:
                    if user_function_choice_int == 1:
                        # text confirming/restating user's choice and
                        # describing what will happen in this section, in french now.
                        print(
                            "Merci d’avoir choisi votre fonction! Vous avez choisi '1'; "
                            "entrez un angle et obtenez la valeur tangente correspondante "
                            "comme élément de fonctionnalité supplémentaire! "
                        )

                        # getting the user's angle.
                        user_angle = input(
                            "Maintenant, s'il vous plait, entrer l’angle en radians de laquelle "
                            "vous voulez obtenir la valeur de tangente: "
                        )

                        # try...catch statement making sure user angle is a valid int.
                        try:
                            user_angle_int = int(user_angle)
                            # if...statement making sure user angle is between 0 and 360.
                            if user_angle_int >= 0 and user_angle_int <= 360:
                                # calculates the tan value of the user's angle.
                                user_calculated_tan = math.tan(user_angle_int)

                                # displays the tan value of the user's angle back to the user in french.
                                print(
                                    "Avec l'angle {}, votre valeur tangente est {}, en radians.".format(
                                        user_angle_int, user_calculated_tan
                                    )
                                )
                            else:
                                print(
                                    "S’il vous plaît, entrez un nombre entre 0 et 360!"
                                )
                        except Exception:
                            print("S’il vous plaît, entrez un nombre valide!")
                    else:
                        # text confirming/restating the user's function choice, and
                        # describing what will happen during this section.
                        print(
                            "Merci d’avoir choisi votre fonction! Vous avez choisi '2'; "
                            "entrer une valeur tangente et obtenir l’angle correspondant "
                            "comme pièce de fonctionnalité supplémentaire!"
                        )

                        # getting the user's tan value.
                        user_tan = input(
                            "Maintenant, veuillez entrer la valeur tangente en radians "
                            "de laquelle vous voulez obtenir l’angle: "
                        )

                        # try..catch to make sure the user's tan value is a valid float.
                        try:
                            user_tan_float = float(user_tan)
                            # calculates the angle of the user's tan value.
                            user_calculated_angle = math.atan(user_tan_float)

                            # displays the calculated angle of the user's tan value
                            # back to the user.
                            print(
                                "Avec la valeur tangente de {}, votre l'angle est {} en radians.".format(
                                    user_tan_float, user_calculated_angle
                                )
                            )
                        except Exception:
                            print(
                                "S’il vous plaît, entrez un nombre valide (décimales acceptées)!"
                            )
                else:
                    print("S’il vous plaît, entrez 1 ou 2!")
            except Exception:
                print("S’il vous plaît, entrez un nombre entier valide (1 ou 2)!")
    else:
        print(
            "Please enter a valid language choice! (en or fr) / "
            "S’il vous plaît, entrez un choix de langue valide! (en ou fr)"
        )
    # checking which language the user entered again
    # for the while... loop this time.
    if user_lang_choice == "en":
        # while... loop that will calculate the tan value for each angle
        # from 0 to 360.
        while counter < 361:
            # calculates the tan value of the counter, which represents
            # the angle in this case.
            calculated_loop_tan = math.tan(counter)
            # prints the angle and tan value for each number.
            print("{} (angle) = {} (tan)".format(counter, calculated_loop_tan))
            # increments counter by 1
            counter = counter + 1
            # uses a break statement to make sure the program does not
            # crash because of an infinite loop.
            if counter == "361":
                break
            else:
                continue
    else:
        # the same while... loop as above, but in french this time.
        while counter < 361:
            # calculates the tan value of the counter, which represents
            # the angle in this case.
            calculated_loop_tan = math.tan(counter)
            # prints the angle and tan value for each number.
            print(
                "{} (l'angle) = {} (valeur tangente)".format(
                    counter, calculated_loop_tan
                )
            )
            # increments counter by 1
            counter = counter + 1
            # uses a break statement to make sure the program does not
            # crash because of an infinite loop.
            if counter == "361":
                break
            else:
                continue


if __name__ == "__main__":
    main()
