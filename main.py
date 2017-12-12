#!/usr/bin/env python3
# coding: utf-8


text ={"invalid": ["Invalid input", "Option invalide"],
       "colors": ["\nR : Red\n"
                  "G : Green\n"
                  "B : Blue\n"
                  "BL : Black\n"
                  "Y : Yellow\n"
                  "W : White\n",
                  "\nR : Rouge\n"
                  "V : Vert\n"
                  "B : Bleu\n"
                  "N : Noir\n"
                  "J : Jaune\n"
                  "BL : Blanc\n"],
       "colors_shortened":[["R", "G", "B", "BL", "Y", "W"], ["R", "V", "B", "N", "J", "BL"]],
       "enter_colors": ["Enter the colors you have from top to bottom (only the first letter(s) as shown above) then "
                        "enter \n",
                        "Entrez les couleurs de haut en bas (seulement la/les première(s)) lettre(s) comme montré "
                        "ci-dessus)\npuis rentrer "],
       "end": ["END", "FIN"],
       "correct": ["\nYou have to press the ", "\nVous devez appuyer sur le "],
       "th_button": [["first", "second", "third", "fourth", "fifth", "sixth"],
                     ["premier", "deuxième", "troisième", "quatrième", "cinquième", "sixième"]],
       "button": [" button", " bouton"],
       "exit": ["1. Exit\n2. Redo", "1. Quitter\n2. Recommencer\n"],
        "colors_length": ["There should be between 3 and 6 buttons, do it again",
                          "Il devrait y avoir entre 3 et 6 boutons. Recommencez"]
       }


def valid_option(prompt, options):
    return prompt in options


def get_language():
    print("\n ==============================="
          "\n|Program written by Kenshin9977|"
          "\n================================\n"
          "\n1. English"
          "\n2. Français\n")
    language_chosen = input("Choose your language / Choisissez votre langue\n")
    while not valid_option(language_chosen, ["1", "2"]):
        print("Invalid input / Option invalide")
        language_chosen = input("Choose your language / Choisissez votre langue\n")
    return int(language_chosen)


def get_sum(language, colors, color_index):
    return colors.count(text["colors_shortened"][language][color_index])


def get_last_color(language, colors, color_index):
    return len(colors) - colors[::-1].index(text["colors_shortened"][language][color_index])


def get_w(colors):
    w = 0
    for x in range(0, 5):
        if get_sum(0, colors, x) > 1:
            w += 1
    return w


def get_s(colors):
    return get_w(colors)


def get_colors(language):
    colors = []
    print(text["colors"][language] + text["enter_colors"][language] + text["end"][language])
    prompt = input().upper()
    while prompt != text["end"][language]:
        if valid_option(prompt, text["colors_shortened"][language]):
            colors.append(prompt)
        else:
            print(text["invalid"][language])
        prompt = input().upper()
    return colors


def compute_answer(language, colors):
    if len(colors) == 3:
        if text["colors_shortened"][language][3] not in colors:
            answer = 3
        elif colors[-1] == text["colors_shortened"][language][1]:
            answer = 1
        elif get_sum(language, colors, 0) > 1:
            answer = get_last_color(language, colors, 0)
        else:
            answer = 2

    elif len(colors) == 4:
        if get_sum(language, colors, 4) > 1 and get_s(colors) >= 2:
            answer = get_last_color(language, colors, 4)
        elif colors[-1] == text["colors_shortened"][language][5] and get_sum(language, colors, 2) == 0:
            answer = 1
        elif colors.count(text["colors_shortened"][language][3]) > 1:
            answer = len(colors)
        else:
            answer = 3

    elif len(colors) == 5:
        if get_w(colors) <= 3:
            return 1
        elif get_sum(language, colors, 5) == 1 and get_sum(language, colors, 2) > 1:
            return 2
        elif get_sum(language, colors, 0) == 1 and get_w(colors) % 2 == 0 and get_s(colors) < 4:
            return len(colors)
        else:
            answer = 1

    elif len(colors) == 6:
        if get_sum(language, colors, 4) != 0:
            answer = 3
        elif get_sum(language, colors, 4) != 0:
            answer = 4
        elif get_s(colors) >= 1 and get_sum(language, colors, 0) > 1:
            answer = 5
        else:
            answer = len(colors)
    return answer


def display_answer(language, colors):
    if len(colors) < 3 or len(colors) > 6:
        print(text["colors_length"][language])
        exit()
    else:
        print(text["correct"][language] +
              text["th_button"][language][compute_answer(language, colors) - 1] +
              text["button"][language])


def exit_program(language):
    print(text["exit"][language])
    prompt = input()
    while not valid_option(prompt, ["1", "2"]):
        print(text["invalid"][language])
    if prompt == 1:
        exit()
    else:
        solver(language)


def solver(language):
    colors = get_colors(language)
    display_answer(language, colors)
    exit_program(language)


def main():
    language = get_language() - 1
    solver(language)
    exit()

if __name__ == '__main__':
    main()