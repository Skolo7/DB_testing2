import sqlite3 # import biblioteki sqlite3


class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

    # utworzenie metody tworzącej tabelę
    def create_table(self):
        # utworzenie kwerendy Customers zawierającej pola takie jak: id, imie, nazwisko i datę dołączenia
        query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, surname TEXT NOT NULL, date_joined DATE NOT NULL);"
        self.con.execute(query)  # wykonanie tworzenia kwerendy
        # con.commit()  # zaimportowanie/zatwierdzenie kwerendy do bazy

    # utworzenie funkcji dodającej dane do tabeli: add_to_customers()
    def add_to_customers(self, name, surname, date_joined):
        query = "INSERT INTO Customers(name, surname, date_joined) VALUES(?,?,?)"
        self.con.execute(query, (name, surname, date_joined))


    # utworzenie funkcji ukazującej tabelę
    def preview_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        results = self.con.execute(query).fetchall()  # metoda fetchall() zwraca wszystkie wybrane przez SELECTa rekordy w postaci listy
        print(results)

    # utworzenie funkcji kasującej wiersze w bazie danych
    def delete_row(self, id):
        query = f"DELETE FROM Customers WHERE id = {id}"
        self.con.execute(query)


    def update_information(self, id, name, surname, date_joined):
        query = f"UPDATE Customers SET name = {name}, surname = {surname}, date_joined = {date_joined} WHERE id = {id}"
        self.con.execute(query)



    # enter jest wywolywane zawsze po napotkaniu sktruktury "with"
    # enter jest wywolywane jesli chcemy "otwierać połączenie z bazą reprezentowaną przez klasę", zwraca obiekt klasy
    def __enter__(self):
        return self

    # exit jest wywolywane zawsze po napotkaniu struktury with .. as ..
    # zatwierdza wywołane polecenia i zamyka polecenia z bazą
    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()
        self.con.close()

# with open(nazwa_pliku, tryb_pracy) as file
with Database('example2-data') as db:
    # db.create_table()
    # db.add_to_customers('John', 'Wick', '2000-09-02')
    # db.add_to_customers('James', 'Bond', '2002-05-16')
    # db.preview_table('Customers')
    # db.delete_row(2)
    db.preview_table('Customers')
    db.update_information('1', 'James', 'Bond', '2002-05-16')
    db.preview_table('Customers')


# def connect_to_db(path): # utworzenie funkcji nawiązującej połączenie z danym plikiem
#     con = sqlite3.connect(path) # zapamietanie tego pliku pod zmienną con (connection)
#     return con # zwrócenie handlera umożliwiającego zarzadzanie zasobem bazy

# metoda sqlite działa w sposób:
# 1. Wyszukanie pliku bazy danych pod podaną przez użytkownika scieżką
# 2. Jeśli plik został znaleziony, to jest z nim nawiązywane połączenie
# 3. W przeciwnym razie plik jest tworzony i dopiero wtedy jest nawiązywane połączenie


# # wykonanie funkcji
# con = connect_to_db("example-database.sqlite3")
# # create_table(con)
