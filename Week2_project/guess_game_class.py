import random 
import string

class String_Extand:
    def __init__(self,s):
        self.s=s
    # replace a letter in a string word
    def replace_char(self, index, char):
        if 0 <= index < len(self.s):
            self.s = self.s[:index] + char + self.s[index+1:]
        return self.s  
        

class Guess_Game:

    chance_plus = 3
    def __init__(self):
        pass

    def letter_position(self,letter,source_word,new_word):
        # check the count of the letter show in the word
        positions = []
        pos=-1
        while True:
            pos = source_word.find(letter, pos + 1)
            if pos == -1:
                break  # 

            if new_word.s[pos] == '_':
                positions.append(pos)
        return positions


    def check_letter(self,letter,new_word,source_word):
        is_finish = False

        positions = self.letter_position(letter, source_word, new_word)

        # index_num = source_word.find(letter)
        if not positions:
            if letter in source_word:
                print(f"You already tried all '{letter}' in the word.")
            else:
                print("You were wrong")
            return False
        
        # replace the first letter witch didn't replace
        new_word.replace_char(positions[0], letter)
        print(new_word.s)

        if new_word.s==source_word:
            print("Congratulation! You win!")
            is_finish=True
        return is_finish
        
    def game_body(self,source_word,blank_word):
        
        max_chance=len(source_word) + self.chance_plus
        new_word = String_Extand(blank_word)
        
        while max_chance > 0:
            
            guess_letter=input(f"please input a letter you'll have {max_chance} chances:").lower()
            # check lenth
            if len(guess_letter)!=1:
                print("Please input one letter")
                continue

            # check if the letter was tried
            if(new_word.s.find(guess_letter)!=-1 and new_word.s.count(guess_letter)==source_word.count(guess_letter)):
                print("You already tried that letter")

            if(self.check_letter(guess_letter,new_word,source_word)):
                break

            max_chance-=1
            if(max_chance==0):
                print("You finished your chances")
                print(f"The correct word was: {source_word}")


def generate_word():
    word_list=["cat","dog","fish","bird","rabbit","banana"]
    result_word=random.choice(word_list)
    return result_word  


if __name__=="__main__":
    # generage a random word
    source_word = generate_word()
    # generate blanks
    word_lenth = len(source_word)
    blank_word = "_"*word_lenth

    print("Let's play the word guessing game!")
    print(f"This this the blanked word:{blank_word}")
    # 
    
    game = Guess_Game()
    game.game_body(source_word.lower(),blank_word)
