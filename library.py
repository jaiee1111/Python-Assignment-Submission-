class library:
    def __init__(self, book_name, auther,availability_status=True):
        self.book_name = book_name
        self.auther = auther  
        self.availability_status = availability_status #True if available, false if checked out 

    def check_out(self):
        if self.availability_status:
            self.availability = False
            print("book'{self.book_name}'by{self.auther}has been checked out.")
        else:
            print("sorry,'{self.book_name}' is currently not avalible.")

    def return_book(self):
        if not self.availability_status:
            self.availability_status = True
            print("book'{self.book_name}'has been returned and is now available.") 
        else:
            print("book'{self.book_name}'was not checked out.")

    def display_book_info(self):
        status="available"if self.availability_status else"checked out"
        print("book:{self.book_name},auther:{self.auther},status:{status}")

#example usages 
book1 = library("the great gatsby","f.scott fitzgerald")
book2 = library("to kill a mockingbird","harper lee")
book3 = library("1986","george orwell",False) 

# display book information 
book1.display_book_info
book2.display_book_info
book3.display_book_info

print("checking out books")
book1.check_out()
book2.check_out()

print("Returning book ")
book1.return_book()
book2.return_book()

print("final book statuses:")
book1.display_book_info()
book2.display_book_info()
book3.display_book_info()
