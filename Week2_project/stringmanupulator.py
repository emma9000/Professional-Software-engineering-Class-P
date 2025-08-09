
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


if __name__=="__main__":

    text="example"
    string_object=stringManupulator(text)
    result= string_object.find_character('x')
    print(result)

    #input_word=input("Please input a word:")
    #text=input_word

    
    string_object.string_lenth()
    string_object.string_toupper()
    
