from phonebook import PhoneBook

def test_lookup_by_name():
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        assert number == "12345"