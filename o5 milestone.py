print("You're running late for work. You are going 5 over the speed limit and the light turns yellow.")
stop_red = 'STOP'
run_yellow = 'SPEED'
first = input(f'Do you stop for the red light or speed to go through the light? {stop_red} or {run_yellow}? ')
tie_shoe = 'TIE'
keep_going = 'FORGET'
if first == stop_red.lower():
    print('You sit and wait for the light and it only takes 1 minutes')
    print('After the light you see a cop sitting there and you are so grateful you waited at the light.')
    print('You make it to work with 1 minute to spare but your shoe is untied.')
    second = input(f'Do you stop and tie your shoe or forget about it and keep going? {tie_shoe} or {keep_going}? ')
    if second == tie_shoe.lower():
        print('You tie your shoe and walk inside')
        print('Your boss looks at you and yells for you being 2 minutes late')
        yell_back = 'YELL'
        sorry = 'SORRY'
        quit = 'QUIT'
        third = input(f'Do you yell back or apologize or quit on the spot? {yell_back} or {sorry} or {quit}? ')

        if third == yell_back.lower():
            print('Your boss is furious and fires you.')

        elif third == sorry.lower():
            print('Your boss walks away and you get to work.')
        elif third == quit.lower():
            print ('You quit right then and your boss says he was going to fire you anyway.')
        else:
            print('INVALID RESPONSE')
    elif second == keep_going.lower():
        print('You run inside and make it right on time')
        print('Your boss smiles at you and wants to talk in his office')
        print('Your boss offers you a raise for always being on time and being so efficient.')
    else:
        print('INVALID RESPONSE')
elif first == run_yellow.lower():
    print('You speed up and the light turns red. There is a cop sitting there and flips on his lights')
    print('The cop pulls you over and walks up to your car and asks if you know why he pulled you over.')
    yes = 'YES'
    no = 'NO'
    fourth = input(f'Do you say {yes} or {no}? ')
    if fourth == yes.lower():
        print ('The officer gives you a warning and lets you on your way')
        print ('You are late for work and dont know if you should go or not')
        dont_go = 'HOME'
        go =  'WORK'
        fifth = input(f'Do you go to work or go home and call in sick? {go} or {dont_go}? ')
        if fifth == go.lower():
            print('You get to work and your boss immediately fires you for being late.')
        elif fifth == dont_go.lower():
            print('Your boss calls you and tells you to feel better.')
        else:
            print('INVALID RESPONSE')
    elif fourth == no.lower():
        print('The officer takes this offensively and gives you a ticket.')
        print('The officer asks how fast were you going?')
        speed = int(input('How fast were you going?'))
        if speed >= 70:
            print('The cop gives you another ticket')
        else:
            print('The cop tells you to just go home.')
else:
    print('INVALID RESPONSE')