import model
import view
import config


def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.write_db_file()
        case 4:
            view.change_contact(model.db_list)
            model.write_db_file()
        case 3:
            model.db_list.append(view.create_contact())
        case 5:
            view.delete_contact(model.db_list)
        case 6:
            view.find_contact(model.db_list)
        case 7:
            view.exit_program()


def start():
    model.read_db(config.db_name)
    view.db_success(model.db_list)
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
