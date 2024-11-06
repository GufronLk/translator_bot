import sqlite3


def connect(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor


# tuple(conn, cursor)

# users
# user_id
# chat_id

# translations
# translations_id
# original
# translated
# code_from
# code_to
# user_id

def create_users_table():
    conn, cursor = connect('../translator.db')
    sql = '''
        create table if not exists users (
           user_id integer primary key autoincrement,
           chat_id bigint not null
        );
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('users created')


# create_users_table()

def create_translations_table():
    conn, cursor = connect('../translator.db')
    sql = '''
        create table if not exists translations(
            translation_id integer primary key autoincrement,
            original text,
            translated text,
            code_from text,
            code_to text,
            is_fav boolean default false,
            user_id integer references users(user_id)
        );
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('translations created')


# create_translations_table()

def get_user_id(chat_id):
    conn, cursor = connect('translator.db')
    sql = 'select user_id from users where chat_id=?'
    user = cursor.execute(sql, (chat_id,)).fetchone()
    if user is None:
        return 0, False
    return user[0], True


def add_user(chat_id):
    user_id, exists = get_user_id(chat_id)
    sql = 'insert into users(chat_id) values (?)'
    conn, cursor = connect('translator.db')
    if not exists:
        cursor.execute(sql, (chat_id,))
        conn.commit()
        print('user added')
    conn.close()


def add_translation(
        original,
        translated,
        code_from,
        code_to,
        chat_id
):
    conn, cursor = connect('translator.db')
    user_id, _ = get_user_id(chat_id)
    sql = '''
    insert into translations(original, translated, code_from, code_to, user_id)
    values (?,?,?,?,?) returning translation_id;
    '''
    _id = cursor.execute(sql, (original, translated, code_from, code_to, user_id)).fetchone()
    conn.commit()
    conn.close()
    print('translation added')
    return _id[0]


def make_fav(translation_id):
    conn, cursor = connect('translator.db')
    sql = 'update translations set is_fav=1 where translation_id=?'
    cursor.execute(sql, (translation_id,))
    conn.commit()
    conn.close()