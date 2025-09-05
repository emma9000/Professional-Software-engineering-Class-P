class LibraryItem:

    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display_detail(self):
        print(f"This instance didn't override this method!")

class Book(LibraryItem):

    def __init__(self, title, author):
        super().__init__(title, author)

    def display_detail(self):
        print(f"Book information: title:{self.title} author:{self.author}")

class Magazine(LibraryItem):

    def __init__(self, title, author, frequency):
        super().__init__(title, author)

        self.frequency=frequency
    def display_detail(self):
        print(f"Magazine information: title:{self.title} author:{self.author} frequency:{self.frequency}")


class Library:

    def __init__(self):
        self._item_list: list[LibraryItem]=[]

    def add_item(self,  libray_item:LibraryItem):
        self._item_list.append(libray_item)

    def remove_item(self, libray_item:LibraryItem):
        item = None
        for i in self._item_list:
            if i.title==libray_item.title:
                self._item_list.remove(i)
                return True
        
        return False
        
    def display_items(self):
        if len(self._item_list) == 0:
            print("There is no item yet")
        else:
            for i in self._item_list:
                i.display_detail()

# decorator

if __name__=="__main__":

    book1=Book("Harry Potter","J.K.Rolin")
    book2=Book("The Three Body","Liu Cixin")

    magazine1=Magazine("Nature","aa",2)
    magazine2=Magazine("Scientice","bb",3)

    lib=Library()
    lib.add_item(book1)
    lib.add_item(book2)
    lib.add_item(magazine1)
    lib.add_item(magazine2)

    lib.display_items()
    lib.remove_item("Harry Potter")
    lib.display_items()

