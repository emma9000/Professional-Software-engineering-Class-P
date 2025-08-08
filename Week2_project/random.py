# generage a random word
import random as rd

def generate_word():
    word_list=["cat","dog","fish","bird"]
    result_word=rd.choice(word_list)
    # result_word=word_list[word_index]
    return result_word

def guess_letter(source_word,blanked_word):
    new_word=blanked_word
    max_chance=len(source_word)+3
    while max_chance > 0:
        
        guess_letter=input("please input a letter:").lower()
        if len(guess_letter)!=1:
            print("Please input one letter")
            continue
        if(new_word.find(guess_letter)>=0):
            print("You already tried that letter")
            continue

        index_num=source_word.find(guess_letter)
        if index_num>=0:
            new_word=new_word[:index_num]+guess_letter+new_word[index_num+1:]
            print(new_word)
        else:
            print(f"you were wrong") 

        if new_word==source_word:
            print("Congratulation! You win!")
            break
        
        max_chance-=1
        print(f"you have another {max_chance} chances")
        if(max_chance==0):
            print("You finished your chances")

    

if __name__=="__main__":
    # generage a random word
    source_word=generate_word()
    # generate blanks
    word_lenth=len(source_word)
    blanked_word="_"*word_lenth

    print("Let's play the word guessing game!")
    print(f"This this the blanked word:{blanked_word}")
    # 
    

    guess_letter(source_word,blanked_word)
