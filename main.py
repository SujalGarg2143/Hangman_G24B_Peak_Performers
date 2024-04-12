import tkinter as tk
from tkinter import messagebox
import random

#list of words
words = ["banana","elephant","computer","universe","chocolate","rainbow","guitar","mountain","oxygen","balloon","library","butterfly","sunshine","adventure","diamond","symphony","fireworks","kangaroo","elephant","telephone","umbrella","watermelon","telescope","penguin","dragonfly","strawberry","parrot","hurricane","lighthouse","basketball","firecracker","caterpillar","bubblegum","lightning","waterfall","volleyball","bubble","coconut","spider","helicopter","octopus","pineapple","telephone","adventure","lollipop","strawberry","lemonade","kangaroo","butterfly","library","snowflake","dragonfly","honeybee","jellyfish","marshmallow","sunflower","campfire","crocodile","pinecone","tornado","snowball","seashell","blueberry","pineapple","popcorn","cupcake","rainbow","sausage","spaceship","turtle","coconut","snowman","firefly","cucumber","scarecrow","lemonade","mosquito","pancake","rainbow","starfish","buttercup","bubblegum","watermelon","popcorn","strawberry","snowflake","hamburger","waterfall","fireworks","snowman","dragonfly","caterpillar","pineapple","sunflower","butterflies","telephone","telescope","basketball","pinecone","campfire"]

#intialize variables 
word_to_guess = random.choice(words)
guessed_letters = []
attempts = 6

#create a window
window = tk.Tk()
window.title("Hangman Game Peak Performers")

#function to check if game is over 
def is_game_over():
    return check_win() or check_loss()

#function to check if player has won
def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)

#function to check if player has lost 
def check_loss():
    return attempts == 0

#function to handle a letter guess
def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            messagebox.showinfo("Hangman" , f"You've already guessed '{letter}")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                messagebox.showinfo("Hangman" , "Congratulation! You Win!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_attempts_display()
            draw_hangman()
            if check_loss():
                 messagebox.showinfo("Hangman" , "You lose! You let a good man die , The word was: " + word_to_guess)
                 reset_game()
        letter_entry.delete(0 , tk.END) #it clears the input field
    else:
        messagebox.showinfo("Hangman" , "Please make valid entry.")

#function to reset the game 
def reset_game():
    global word_to_guess , guessed_letters , attempts
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6
    update_word_display()
    update_attempts_display()
    draw_hangman()

#function to update the word display
def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
        display_word += " "
    word_label.config(text = display_word)


#function to update the attempts display
def update_attempts_display():
    attempts_label.config(text = f"Attempts left: {attempts}")


#function to draw hangman figure
def draw_hangman():
    canvas.delete("hangman")

    if attempts < 6:
        canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman")  #head
    if attempts < 5:
        canvas.create_line(150, 175, 150, 225, width=4, tags="hangman") #body
    if attempts < 4:
        canvas.create_line(150, 200, 125, 175, width=4, tags="hangman")  #left am
    if attempts < 3:
        canvas.create_line(150, 200, 175, 175, width=4, tags="hangman")  #right arm
    if attempts < 2:
        canvas.create_line(150, 225, 125, 250, width=4, tags="hangman")  #left leg
    if attempts < 1:
        canvas.create_line(150, 225, 175, 250, width=4, tags="hangman") #right leg


#create gui elements
word_label = tk.Label(window , text="" , font=("Arial", 24))
attempts_label = tk.Label(window, text="", font=("Arial", 16))
letter_entry = tk.Entry(window, width=5, font=("Arial", 16))
guess_button = tk.Button(window, text="Guess", command=guess_letter)
reset_button = tk.Button(window, text="Reset", command=reset_game)
canvas = tk.Canvas(window, width=300, height=300)
canvas.create_line(50, 250, 250, 250, width=4) #baseline
canvas.create_line(200, 250, 200, 100, width=4) #post
canvas.create_line(100, 100, 200, 100, width=4)  #beam
canvas.create_line(150, 100, 150, 120, width=4)  #beam
canvas.pack()

#pack gui elements
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guess_button.pack()
reset_button.pack()

#update initial displays
update_word_display()
update_attempts_display()
draw_hangman()

#run application
window.mainloop()

