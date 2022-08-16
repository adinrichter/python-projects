#
# Python: 3.10.6
#
# Author: Adin Richter
#
# Purpose: Learning Python.
#
#
#
#
#
#
#


def start(name):
    initialize(name)
    

def initialize(name):
    score['kind'] = score['neutral'] = score['inconsiderate'] = score['selfish'] = score['mallicious'] = 0  
    if name != '':
        print('\nWelcome back {}.'.format(name))
        input('Continue? (enter): ')
    else:
        stop = True
        while stop:
            if name == '':
                name = input('\nEnter your character\'s name: ').capitalize()
                if name != '':
                    print('\nWelcome, {}!'.format(name))
                    print('\nIn this game, you will encounter \na number of different scenarios. \nYou can make the decisions you want, \nbut your actions have consequences.\n')
                    input('Continue? (enter): ')
                    stop = False
    game(name)

def end(name):
    print('Kindness:', score['kind'], 'Neutral:', score['neutral'], 'Inconsiderate:', score['inconsiderate'], 'Selfish:', score['selfish'], 'Mallicious:', score['mallicious'])
    kindness = score['kind'] - score['inconsiderate']
    print('\n\nYou\'ve made your choices, and you had a rich time.')
    if kindness >= 1:
        print('You\'re a good person.')
    if score['inconsiderate'] > 0 or score['selfish'] > 0:
        print('But you aren\'t perfect.')
    if score['mallicious'] > 0:
        print('But you put yourself first.')
    answered = False
    while not answered:
        answer = input('Would you like to play again? (Y/N): ').lower()
        if answer == 'y':
            answered = True
            initialize(name)
        elif answer == 'n':
            answered = True
            quit()
        else: print('Invalid Input')
        continue

def keepScore(action):
    score[action] += 1
    print('\n[' + action.capitalize() + ']\n')


def interactions(scene, name):
    
    if scene == 1:
        print('\n')
        print('Febuary 14th, 1938 - New York City\n')
        print('You push yourself forward, your home is only a few more minutes away.')
        print('A carpet of rain is covering the twilight park, the sparse street lights barely visible.\nYou tug at your collar, hoping to pull your jacket even a small amount higher, but it won\'t budge.\n')
        print('You see a man sitting under a half-destroyed tent, shivering.\n"Excuse me Sir," he says. "Some kids came by earlier \nand tore up my tent, now it won\'t hold  water.')
        print('Could you spare a couple pence? \nI\'m only 25 away from staying at a hotel tonight."\n\n<You can INTERACT, or IGNORE. What do you do?>')
        answered = False
        while not answered:
            answer = input('').lower()
            if answer == 'interact':
                print('\nYou approach the man and pull out your wallet.')
                answered = True
                interactions(2, name)
            elif answer == 'ignore':
                print('\nThe rain is too heavy for you to stop, and you walk past the man without making eye contact.')
                answered = True
                keepScore('selfish')
            else:
                print('Invalid Input')
                continue

            
    if scene == 2:
        print('\nYou open it up and realize that you only have a dollar bill.\nYou puzzle whether to give him the whole bill or apologize and leave.')
        print('\n<You can APOLOGIZE, or GIVE. What do you do?>')
        answered = False
        while not answered:
            answer = input('').lower()
            if answer == 'give':
                print('\nYou hand the man the bill, he takes it and thanks you profusely.\nYou wish each other well, and you continue on your way.')
                answered = True
                keepScore('kind')
            elif answer == 'apologize':
                print('\n"I don\'t have anything, I\'m sorry," You say.\n"Oh it\'s okay, I appreciate you taking time to check," he replies.\nYou continue home')
                answered = True
                keepScore('neutral')
            else:
                print('Invalid Input')
                continue
            
    if scene == 3:
        print('You arrive home, drenched. After drying out, you decide you want a cigarette.')
        print('Normally you would smoke on the front steps, since your spouse hates the smell of the smoke, but the rain is still pouring.')
        print('Your spouse is asleep in the bedroom, and probably wouldn\'t know one way or another.\n\n<You can smoke on the STEPS, or INSIDE. What do you do?>')
        answered = False
        while not answered:
            answer = input('').lower()
            if answer == 'steps':
                print('\nYou grab a raincoat and walk outside to the front steps and have your cigarette.\nYou get a little bit wet, but prefer it over smoking up the house.')
                print('After you\'re done, you head back in, and head to bed.')
                answered = True
                keepScore('neutral')
            elif answer == 'inside':
                print('\nYou decide you\'ve had enough of being in the rain, and decide to smoke inside.')
                answered = True
                interactions(4, name)
            else:
                print('Invalid Input')
                continue

    if scene == 4:
        print('Before you light up, you consider opening the window to let some air flow. \nThe smoke wouldn\'t be as bad inside, but it could let some water in.')
        print('\n<You can OPEN the window, or keep it CLOSED. What do you do?>')
        answered = False
        while not answered:
            answer = input('').lower()
            if answer == 'open':
                print('\nYou open the window and light up. You blow most of the smoke out\nbut a good amount remains inside and dissipates, leaving a faint smell behind.')
                print('After you\'re done, you close the window and head to bed.')
                answered = True
                keepScore('inconsiderate')
            elif answer == 'closed':
                print('\nYou decide you\'re done with the rain, and leave the window closed.\nYou light up and fill the living room with smoke.')
                print('After you\'re done, you head to bed.')
                answered = True
                keepScore('mallicious')
            else:
                print('Invalid Input')
                continue
            
    if scene == 5:
        print('You wake up and walk to the kitchen.\nAnd see your spouse cooking breakfast.')
        print('"Hey, we\'re out of eggs. I\'ve got a meeting soon, and would love to have some can you pick some up?"')
        print('You\'re tired, and a little tight on time, but you might be able to manage it.')
        print('\n<You can either GET eggs, or DECLINE. What do you do?>')
        answered = False
        while not answered:
            answer = input('').lower()
            if answer == 'decline':
                print('\n"I don\t know if I can make it in time before work."')
                print('"Ah I see, are you at least able to on your way back?"')
                answered = True
                interactions(6, name)
            elif answer == 'get':
                print('\nYou\'re not sure if you can make it, but you\'d rather do something nice.')
                print('"Sure," You say. "I\'ll head out now and get some."')
                answered = True
                keepScore('kind')
                interactions(7, name)
            else:
                print('Invalid Input')
                continue

    if scene == 6:
        print('\n<You can either ACCEPT, or DECLINE. What do you do?>')
        answered = False
        while not answered:
            answer = input('').lower()
            if answer == 'accept':
                print('"Of course," You say. "I\'m sorry I can\'t get them for you for breakfast."')
                print('"It\'s ok, thank you for picking them up later."')
                print('You and your spouse leave for work.')
                print('\nAfter work, you pick up a carton of eggs, and cook a nice dinner before your spouse gets back.')
                print('You share the dinner and have a wonderful conversation. You both go to bed happy.')
                keepScore('kind')
                answered = True
                end(name)
            elif answer == 'decline':
                print('"That\'s too late, sorry," you say.')
                print('"Whatever." They respond, and leave for work.')
                print('After work you come home, your spouse is still out and you eat dinner alone.')
                print('You go to bed.')
                answered = True
                keepScore('selfish')
                end(name)
            else:
                print('Invalid Input')
                continue

    if scene == 7:
        print('You leave for the grocery, jogging slightly to save time.')
        print('After a couple minutes you get there, and go in.')
        print('You find a nice carton of eggs, and go to the counter.')
        print('You walk to the cashier and place down the carton of eggs behind a family with a young child.')
        if score['kind'] == 2:
            print('\nAfter the family in front of you has finished paying, \nthe cashier rings you up and you take out your wallet.')
            print('You remember that you gave away the bill you had, and forgot to bring any more.')
            print('You reach for your checkbook, but see that it\'s been completely destroyed by the rain the night before.')
            print('\nNot sure of what to do, you look to the cashier.')
            print('"My spouse has a meeting soon and I would love to make them some food, can I take these home and then bring back the money later?"')
            print('Being a regular, you hope that the cashier will trust you, and luck seems to come back to you.')
            print('"Of course', name, 'I know you\'re good for it. Bring it back over tonight."')
            print('"Thank you so much, I appreciate it." You reply.\nYou jog home with the carton, happy in your decision to be generous the night before.')
            print('\nYou arrive home and see your spouse about to leave for their meeting.')
            print('You explain the situation to them, and they find it wonderful that you helped someone out the night before.')
            print('You quickly cook an egg for them as they finish getting ready, and they eat it before they leave.')
            print('They\'re incredibly greatful that you took the time to pick up food, and you hug goodbye as they go to their meeting.')
            end(name)
        else:
            print('\nAs the family in front of you is being rung up, they realize that they\'re 50 cents short.')
            print('You think back to the night before, and feel a bit of regret for not giving the man money,\nand you consider offering to help pay for the rest of their bill.')
            print('\n<You can either offer to PAY for the rest of the family in front of you, or IGNORE them and wait for them to resolve it on their own. What do you do?>')
            answered = False
            while not answered:
                answer = input('').lower()
                if answer == 'pay':
                    print('\nYou tap on one of the parents shoulder\'s and offer to help cover the rest.')
                    print('They\'re hesitant but you assure them that it\'s okay and that you\'re happy to.')
                    print('Thanking you immensely, they finish checking out.')
                    keepScore('kind')
                    answered = True
                    interactions(8, name)
                elif answer == 'ignore':
                    print('You decide you\'d rather hold on to your money, and say nothing.')
                    answered = True
                    keepScore('selfish')
                    interactions(9, name)
                else:
                    print('Invalid Input')
                    continue
                
    if scene == 8:
        print('\nAfter paying for your eggs, you jog home quickly.')
        print('You arrive home and see your spouse about to leave for their meeting.')
        print('You quickly cook an egg for them as they finish getting ready, and they eat it before they leave.')
        print('They\'re incredibly greatful that you took the time to pick up food, and you hug goodbye as they go to their meeting.')
        end(name)
            
    if scene == 9:
        print('\nAfter paying for your eggs, you jog home quickly.')
        print('You catch your spouse leaving, and say goodbye. They thank you for picking up eggs and leave for their meeting.')
        end(name)
        

        
def game(name):
    interactions(1, name)
    interactions(3, name)
    interactions(5, name)


if __name__ == '__main__':
    score = {'kind': 0, 'neutral': 0, 'inconsiderate': 0, 'selfish': 0, 'mallicious': 0}
    start('')

