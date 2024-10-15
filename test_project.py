
from project import Table1,Table2,Table3,Table4,Table5,Booking, Change_the_book, Cancel_the_book,check_cancel_Name

def test_booking():
    assert Booking(1,"MMM",4) == "================\nSuccessful book\n================"
    assert Booking(5,"Mr john",6) == "================\nSuccessful book\n================"


def test_change_the_book_unSuccesslly():
    assert Change_the_book("Man") == "\nname: Man Not Found"
    assert Change_the_book("John") == "\nname: John Not Found"

def test_check_cancel_Name():
    check_cancel_Name("MMM") == "MMM","Table1"
    check_cancel_Name("Mr john") == "Mr john", "Table5"

def test_cancel_the_book_Successlly():
    assert Cancel_the_book("Y",Table1) == "===================\nCanceled Successfully\n==================="
    assert Cancel_the_book("Y",Table5) == "===================\nCanceled Successfully\n==================="
