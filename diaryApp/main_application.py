from diaries import Diaries


diaries = Diaries()


def main():
    display_main_menu()


def display_main_menu():
    menu ="""
WELCOME TO SK DIARY APP
1 -> Create Diary
2 -> Find Diary
3 -> Delete Diary
4 -> Exit
"""
    print(menu)
    response = input("Select option: ")
    match response:
        case "1":
            create_diary()
        case "2":
            find_diary()
        case "3":
            delete_diary()
        case "4":
            exit_app()
        case _:
            default_main_menu_response()

def create_diary():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        diaries.add(username, password)
        print("Diary Created Successfully!!!")
    except Exception as ex:
        print(ex)
    finally:
        display_main_menu()

def find_diary():
    username = input("Enter your username: ")
    try:
        diary = diaries.find_by_username(username)
        display_diary_menu(diary)
    except Exception as ex:
        print(ex)
    finally:
        display_main_menu()

def display_diary_menu(diary):
    menu ="""
WELCOME TO SK DIARY MENU
1 -> Unlock Diary
2 -> Lock Diary
3 -> Create Entry
4 -> Update Entry
5 -> Delete Entry
6 -> Return To Main Menu
"""
    print(menu)
    response = input("Select option: ")
    match response:
        case "1":
            unlock_diary(diary)
        case "2":
            lock_diary(diary)
        case "3":
            create_entry(diary)
        case "4":
            update_entry(diary)
        case "5":
            delete_entry(diary)
        case "6":
            display_main_menu()
        case _:
            default_diary_menu_response(diary)

def unlock_diary(diary):
    password = input("Enter Diary Password: ")
    try:
        diary.unlock_diary(password)
        print("Diary Unlocked!!")
    except Exception as ex:
        print(ex)
    finally:
        display_diary_menu(diary)

def lock_diary(diary):
    try:
        diary.lock_diary()
        print("Diary Locked!!")
    except Exception as ex:
        print(ex)
    finally:
        display_diary_menu(diary)

def create_entry(diary):
    title = input("Enter Title of Entry: ")
    body = input("Enter Body of Entry: ")

    try:
        diary.create_entry(title, body)
        print("Entry Recorded Successfully!!!")
    except Exception as ex:
        print(ex)
    finally:
        display_diary_menu(diary)

def update_entry(diary):
    try:
        entry_id = int(input("Enter Entry ID: "))
        new_title = input("Enter New Title: ")
        new_body = input("Enter New Body: ")

        diary.update_entry(entry_id, new_title, new_body)
        entry = diary.find_entry_by_id(entry_id)

        print("Date Created:", entry.get_date_created())
        print("Entry Updated Successfully!!!")
    except Exception as ex:
        print(ex)
    finally:
        display_diary_menu(diary)

def delete_entry(diary):
    try:
        entry_id = int(input("Enter Entry ID: "))
        entry = diary.find_entry_by_id(entry_id)

        print("Date Created:", entry.get_date_created())
        diary.delete_entry(entry_id)

        print("Entry Deleted Successfully!!!")
    except Exception as ex:
        print(ex)
    finally:
        display_diary_menu(diary)

def delete_diary():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        diaries.delete(username, password)
        print("Diary Deleted!!!")
    except Exception as ex:
        print(ex)
    finally:
        display_main_menu()

def exit_app():
    exit()

def default_main_menu_response():
    display_main_menu()

def default_diary_menu_response(diary):
    print("Invalid Option")
    display_diary_menu(diary)


if __name__ == "__main__":
    main()