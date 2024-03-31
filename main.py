import random

def hangman():
    list_of_questions = ['banana', 'elephant', 'computer', 'guitar', 'sunshine', 'chocolate', 'butterfly', 'universe', 'rainbow', 'pizza', 'octopus', 'telescope', 'library', 'adventure', 'cucumber', 'watermelon', 'dragonfly', 'umbrella', 'kangaroo', 'snowflake', 'bicycle', 'fireworks', 'telephone', 'mountains', 'backpack', 'calculator', 'pencil', 'giraffe', 'icecream', 'jellyfish', 'elephant', 'zebra', 'clock', 'rainbow', 'diamond', 'keyboard', 'dolphin', 'garden', 'snowman', 'rhinoceros', 'violin', 'robot', 'starfish', 'kangaroo', 'firetruck', 'telescope', 'pineapple', 'parrot', 'beehive', 'lemonade', 'scorpion', 'mosquito', 'motorcycle', 'telescope', 'coconut', 'sandwich', 'giraffe', 'birthday', 'bubble', 'caterpillar', 'starfruit', 'baseball', 'cupcake', 'fireworks', 'mosquito', 'apple', 'kangaroo', 'dragonfly', 'cupcake', 'scorpion', 'balloon', 'firefly', 'cookie', 'paintbrush', 'seashell', 'cupboard', 'hotdog', 'jellyfish', 'lemonade', 'pineapple', 'dolphin', 'keyboard', 'umbrella', 'bicycle', 'tomato', 'sandwich', 'rhinoceros', 'firetruck', 'calculator', 'moonlight', 'library', 'telescope', 'octopus', 'watermelon', 'dragonfly', 'backpack', 'icecream', 'seashell', 'rainbow', 'elephant', 'starfish', 'guitar', 'jellybean', 'buttercup', 'caterpillar', 'waterfall', 'hummingbird', 'raspberry', 'bubblegum', 'crocodile', 'pinecone', 'sunshine', 'snowflake', 'ladybug', 'cucumber', 'butterflies', 'snowman', 'basketball', 'paperclip', 'firecracker', 'watermelon', 'telephone', 'clockwork', 'headphones', 'pancakes', 'hamburger', 'lighthouse', 'toothbrush', 'headphones', 'crocodile', 'honeycomb', 'earthquake', 'bubblewrap', 'kangaroo', 'grasshopper', 'pineapple', 'firefighter', 'snowstorm', 'jellyfish', 'cucumber', 'lollipop', 'spaceship', 'firefighter', 'iceberg', 'fireworks', 'paperplane', 'starfruit', 'saxophone', 'snowboard', 'cupboard', 'pancakes', 'moonlight', 'seashell', 'caterpillar', 'paintbrush', 'umbrella', 'backpack', 'waterfall', 'butterflies', 'basketball', 'raspberry', 'ladybug', 'firecracker', 'telephone', 'crocodile', 'toothbrush', 'paperclip', 'hamburger', 'pinecone', 'lighthouse', 'headphones', 'pancakes', 'earthquake', 'jellyfish', 'watermelon', 'firefighter', 'jellybean', 'iceberg', 'spaceship', 'lollipop', 'fireworks', 'cupboard', 'saxophone', 'moonlight', 'paperplane', 'snowstorm', 'starfruit', 'snowboard', 'grasshopper', 'honeycomb', 'bubblewrap', 'firetruck', 'pencil', 'birthday', 'hotdog', 'lemonade', 'calculator', 'cookie', 'paintbrush', 'sandwich']
    word = random.choice(list_of_questions)
    turns = 10
    guess_made = ''
    valid_enteries = set('abcdefghijklmnopqrstuvwxyz')  #user can only enter an aplhabet and that only one time only ...
    
    while len(word)>0:
        main_word = ""

        for letter in word:
            if letter in guess_made:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        if main_word == word:        #if word guess is correct break the loop with congo message
            print(main_word)
            print("Congratulations , You Won !!")
            break


        print("Guess the word" , main_word)
        guess = input()

        if guess in valid_enteries:   #used to check if guess made is from valid enteries or not 
            guess_made = guess_made + guess  #if guess is valid it will store guess in guess_made
        else:
            print("Enter the valid characters")
            guess = input()
        

        if guess not in word:
            turns = turns -1

            if turns == 9:
                print("9 turns left !")
                print("---------------")
            
            if turns == 8:
                print("8 turns left !")
                print("---------------")
                print("       O      ")

            if turns == 7:
                print("7 turns left !")
                print("---------------")
                print("       O      ")
                print("       |      ")

            if turns == 6:
                print("6 turns left !")
                print("---------------")
                print("       O      ")
                print("       |      ")
                print("      /       ")

            if turns == 5:
                print("5 turns left !")
                print("---------------")
                print("       O      ")
                print("       |      ")
                print("      / \     ")

            if turns == 4:
                print("4 turns left !")
                print("---------------")
                print("      \O      ")
                print("       |      ")
                print("      / \     ")

            if turns == 3:
                print("3 turns left !")
                print("---------------")
                print("      \O/      ")
                print("       |      ")
                print("      / \     ")

            if turns == 2:
                print("2 turns left !")
                print("---------------")
                print("      \O/  |   ")
                print("       |      ")
                print("      / \     ")

            if turns == 1:
                print("Only 1 turn left !! hangman on his last breath")
                print("---------------")
                print("      \O/__|   ")
                print("       |      ")
                print("      / \     ")
                
            if turns == 0:
                print("You loose")
                print("You let a good man die.....")
                print("The word which was supposed to be guessed was : " , word)
                print("---------------")
                print("   DEAD     O__|   ")
                print("           /|\      ")
                print("           / \     ")
                break
                






name = input("Enter Your Name : ")
print("WELCOME",name,"!")
print("---------------")
print("Try to guess a word in less than 10 attempts \n")
print('''Main Instruction : 
Kindly enter all aplhabets in lowercase \n''')

hangman()
