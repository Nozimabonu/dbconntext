import psycopg2
from colorama import Fore

conn = psycopg2.connect(dbname='n42 5-oy@localhost',
                        user='postgres',
                        password='0509',
                        host='localhost',
                        port='5432'
                        )
cur = conn.cursor()

create_table_query = '''
create table if not exists Persons (
id serial primary key,
full_name varchar(255) not null,
age int,
email varchar(255) not null
);

'''

cur.execute(create_table_query)
cur.commit()


def print_response(message: str):
    print(Fore.YELLOW + message + Fore.RESET)


def insert_person():
    name = str(input('Enter person name: '))
    age = int(input('Enter person age: '))
    email = str(input('Enter person email: '))
    insert_into_query = 'insert into Persons(full_name, age, email) values (%s, %s, %s);'
    insert_into_params = (name, age, email)
    cur.execute(insert_into_query, insert_into_params)
    conn.commit()
    print_response('INSERT 0 1')


def select_all_person():
    select_query = 'select * from Persons;'
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print_response(str(row))


def select_one_person():
    _id = int(input('Enter person id: '))
    select_query = 'select * from Persons where id = %s;'
    cur.execute(select_query, (_id,))
    person = cur.fetchone()
    if person:
        print_response(str(person))
    else:
        print_response('No such person')


def update_person():
    select_all_person()
    _id = int(input('Enter person id: '))
    name = str(input('Enter person name: '))
    age = int(input('Enter person age: '))
    email = str(input('Enter person email: '))
    update_query = 'update Persons set full_name = %s, age = %s, email = %s where id = %s;'
    update_query_params = (name, age, email, _id)
    cur.execute(update_query, update_query_params)
    conn.commit()
    print_response('Successfully updated person')


def delete_person():
    select_all_person()
    _id = int(input('Enter person id: '))

    delete_query = 'delete from Persons where id = %s;'
    cur.execute(delete_query, (_id,))
    conn.commit()
    print_response('Successfully deleted person')


def save():
    name = str(input('Enter person name: '))
    age = int(input('Enter person age: '))
    email = str(input('Enter person email: '))
    update_query = 'update Persons set full_name = %s, age = %s where id = %s;'
    update_query_params = (name, age, email)
    cur.execute(update_query, update_query_params)


def get_person():
    select_all_person()
    _id = int(input('Enter person id: '))
    select_query = 'select * from Persons where id = %s;'
    cur.execute(select_query, (_id,))
    person = cur.fetchone()
    if person:
        print_response(str(person))
        return person


def menu():
    try:
        print('Insert Person      => 1')
        print('Select all Persons => 2')
        print('Delete book        => 3')
        print('Select one Person  => 4')
        print('Update Person      => 5')
        print('Save Person        => 6')
        print('get Person         => 7')
        choice = int(input('Enter your choice: '))

    except ValueError as v:

        choice = -1

        return choice


def run():
    while True:
        choice = menu()
        match choice:
            case 1:
                insert_person()
            case 2:
                select_all_person()
            case 3:
                delete_person()
            case 4:
                select_one_person()
            case 5:
                update_person()
            case 6:
                save()
            case 7:
                get_person()
            case _:
                break


if __name__ == '__main__':
    run()

# cur.execute('select * from Person')
