import random

def hangman():
    list_of_questions = ['Banana', 'Elephant', 'Computer', 'Guitar', 'Sunshine', 'Chocolate', 'Butterfly', 'Universe', 'Rainbow', 'Pizza', 'Octopus', 'Telescope', 'Library', 'Adventure', 'Cucumber', 'Watermelon', 'Dragonfly', 'Umbrella', 'Kangaroo', 'Snowflake', 'Bicycle', 'Fireworks', 'Telephone', 'Mountains', 'Backpack', 'Calculator', 'Pencil', 'Giraffe', 'Icecream', 'Jellyfish', 'Elephant', 'Zebra', 'Clock', 'Rainbow', 'Diamond', 'Keyboard', 'Dolphin', 'Garden', 'Snowman', 'Rhinoceros', 'Violin', 'Robot', 'Starfish', 'Kangaroo', 'Firetruck', 'Telescope', 'Pineapple', 'Parrot', 'Beehive', 'Lemonade', 'Scorpion', 'Mosquito', 'Motorcycle', 'Telescope', 'Coconut', 'Sandwich', 'Giraffe', 'Birthday', 'Bubble', 'Caterpillar', 'Starfruit', 'Baseball', 'Cupcake', 'Fireworks', 'Mosquito', 'Apple', 'Kangaroo', 'Dragonfly', 'Cupcake', 'Scorpion', 'Balloon', 'Firefly', 'Cookie', 'Paintbrush', 'Seashell', 'Cupboard', 'Hotdog', 'Jellyfish', 'Lemonade', 'Pineapple', 'Dolphin', 'Keyboard', 'Umbrella', 'Bicycle', 'Tomato', 'Sandwich', 'Rhinoceros', 'Firetruck', 'Calculator', 'Moonlight', 'Library', 'Telescope', 'Octopus', 'Watermelon', 'Dragonfly', 'Backpack', 'Icecream', 'Seashell', 'Rainbow', 'Elephant', 'Starfish', 'Guitar', 'Jellybean', 'Buttercup', 'Caterpillar', 'Waterfall', 'Hummingbird', 'Raspberry', 'Bubblegum', 'Crocodile', 'Pinecone', 'Sunshine', 'Snowflake', 'Ladybug', 'Cucumber', 'Butterflies', 'Snowman', 'Basketball', 'Paperclip', 'Firecracker', 'Watermelon', 'Telephone', 'Clockwork', 'Headphones', 'Pancakes', 'Hamburger', 'Lighthouse', 'Toothbrush', 'Headphones', 'Crocodile', 'Honeycomb', 'Earthquake', 'Bubblewrap', 'Kangaroo', 'Grasshopper', 'Pineapple', 'Firefighter', 'Snowstorm', 'Jellyfish', 'Cucumber', 'Lollipop', 'Spaceship', 'Firefighter', 'Iceberg', 'Fireworks', 'Paperplane', 'Starfruit', 'Saxophone', 'Snowboard', 'Cupboard', 'Pancakes', 'Moonlight', 'Seashell', 'Caterpillar', 'Paintbrush', 'Umbrella', 'Backpack', 'Waterfall', 'Butterflies', 'Basketball', 'Raspberry', 'Ladybug', 'Firecracker', 'Telephone', 'Crocodile', 'Toothbrush', 'Paperclip', 'Hamburger', 'Pinecone', 'Lighthouse', 'Headphones', 'Pancakes', 'Earthquake', 'Jellyfish', 'Watermelon', 'Firefighter', 'Jellybean', 'Iceberg', 'Spaceship', 'Lollipop', 'Fireworks', 'Cupboard', 'Saxophone', 'Moonlight', 'Paperplane', 'Snowstorm', 'Starfruit', 'Snowboard', 'Grasshopper', 'Honeycomb', 'Bubblewrap', 'Firetruck', 'Pencil', 'Birthday', 'Hotdog', 'Lemonade', 'Calculator', 'Cookie', 'Paintbrush', 'Sandwich']
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
                print("       O__|   ")
                print("      /|\      ")
                print("      / \     ")
                break
                






name = input("Enter Your Name : ")
print("WELCOME",name,"!")
print("---------------")
print("Try to guess a word in less than 10 attempts \n")

hangman()