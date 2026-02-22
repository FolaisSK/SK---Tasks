from diaryApp.entry import Entry


class Diary:
    def __init__(self, username, password):
        self.__validate_password_length(password)
        self.__username = username
        self.__password = password
        self.__is_locked = True
        self.__entries = []
        self.__entry_id = 0

    def is_locked(self):
        return self.__is_locked

    def unlock_diary(self,password):
        self.__check_is_unlocked()
        self.__validate_password(password)
        self.__is_locked = False

    def lock_diary(self):
        self.__check_status()
        self.__is_locked = True

    def create_entry(self, title, body):
        self.__check_status()
        self.__entry_id += 1
        entry =  Entry(self.__entry_id, title, body)
        self.__entries.append(entry)

    def find_entry_by_id(self, entry_id):
        self.__check_status()
        self.__validate_entry_id(entry_id)
        for entry in self.__entries:
            if entry.get_id() == entry_id:
                return entry
        raise Exception("Entry not found")

    def delete_entry(self, entry_id):
        self.__check_status()
        self.__validate_entry_id(entry_id)
        self.__entries.remove(self.find_entry_by_id(entry_id))

    def update_entry(self, entry_id, new_title, new_body):
        self.__check_status()
        self.__validate_entry_id(entry_id)
        entry = self.find_entry_by_id(entry_id)
        entry.set_title(new_title)
        entry.set_body(new_body)

    def get_username(self):
        return self.__username

    def peep_password(self,password):
        if self.__password == password:
            return True
        return False

    def __validate_password(self, password):
        if  not self.peep_password(password):
            raise Exception("Incorrect Password")

    def __validate_password_length(self, password):
        if password == "":
            raise Exception("Password cannot be empty")
        if len(password) < 4:
            raise Exception("Password must be at least 4 characters")

    def __validate_entry_id(self, entry_id):
        if entry_id < 1:
            raise Exception("Entry id cannot be less than 1")

    def __check_status(self):
        if self.__is_locked:
            raise Exception("Diary is locked!!")

    def __check_is_unlocked(self):
        if not self.__is_locked:
            raise Exception("Diary is unlocked!!")