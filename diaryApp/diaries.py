from diaryApp.diary import Diary


class Diaries:
    def __init__(self):
        self.__diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.__diaries.append(diary)

    def find_by_username(self, username):
        for diary in self.__diaries:
            if diary.get_username() == username:
                return diary
        raise Exception("Diary does not exist!!")

    def delete(self, username, password):
        diary = self.find_by_username(username)
        diary.unlock_diary(password)
        self.__diaries.remove(diary)