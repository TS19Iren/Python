import config
db_list = []


def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding=config.encoding) as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(config.separator)
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)

def write_db_file():
    global db_list
    with open(config.db_name, 'w', encoding=config.encoding) as data:
        for i in db_list:
            contact = str(i['lastname']+config.separator+i['firstname']+config.separator+i['phone']+config.separator+i['comment']+'\n')
            data.write(contact)

