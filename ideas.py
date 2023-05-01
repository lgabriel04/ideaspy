import os

def store_idea(count):
    with open('ideas.txt', 'a') as f:
        idea = input('What is your idea? ')
        f.write(f"{count}. {idea}\n")
        print('Idea successfully imported!')
        
count = 1
while True:
    cmd = input('Input command: ')
    if cmd == 'store-idea':
        store_idea(count)
        count += 1
        while True:
            add_another = input('Click enter if you want to add another idea, otherwise type exit: ')
            if add_another == '':
                store_idea(count)
                count += 1
            elif add_another == 'exit':
                break
    elif cmd == 'exit':
        break
    else:
        print('Invalid command!')
