# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

thisIsaVariable = "Hello! I am a value stored in a Variable!"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('What is your name?')  # ask for their name
    personName = input()
    print('It is good to meet you, ' + personName)

    print('What is your age?')  # ask for their age
    personAge = input()
    print('You will be ' + str(int(personAge) + 1) + ' in a year.')

    print('Type something and I will count the length of that sentence?')  # ask for their age
    sentence = input()
    print('The length of your sentence is ' + str(len(sentence)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
