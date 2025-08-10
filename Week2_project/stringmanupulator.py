
class stringManupulator:
    def __init__(self,text):
        self.text=text

    def find_character(self,char):
        return self.text.find(char)

    def string_lenth(self):
        lenth= len(self.text)
        print(f"the input lenth is：{lenth}")

    def string_toupper(self):
        upper_string= str.upper(self.text)
        print(f"the input upper style is {upper_string}")

    def get_word_count(self,input_sentence):
        word_list=input_sentence.split(' ')
        count_word=len(word_list)
        print(f"input and find the number of words:{count_word}")
        


if __name__=="__main__":

    text="example"
    string_object=stringManupulator(text)
    result= string_object.find_character('x')
    print(result)

    #
    #text=input_word

    
    string_object.string_lenth()
    string_object.string_toupper()

    input_words=input("Please input a sentence:")
    string_object.get_word_count(input_words)

    
