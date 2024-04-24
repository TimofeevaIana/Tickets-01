from datetime import datetime, timedelta


class Film:
    def __init__(self, title, start_date, end_date):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.show_dates = []
        self.show_times = []
        self.available_seats = self.initialize_seats()

    def initialize_seats(self):
        seats = {}
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for row in rows:
            for col in range(1, 11):
                seats[f"{row}{col}"] = "Available"
        return seats

    def add_show_dates(self, start_date, end_date):
        current_date = start_date
        while current_date <= end_date:
            self.show_dates.append(current_date)
            current_date += timedelta(days=1)

    def add_show_times(self, times):
        self.show_times.extend(times)

    def display_available_dates(self):
        for idx, date in enumerate(self.show_dates, 1):
            print(f"{idx}. {date.strftime('%Y-%m-%d')}")
        return self.show_dates

    def display_available_times(self):
        return self.show_times

    def display_available_seats(self):
        return ' '.join([seat for seat, status in self.available_seats.items() if status == "Available"])


# Определение главной функции
def main():
    films = []

    while True:
        print("Добро пожаловать в информационно-справочную систему для продажи билетов в кинотеатре!")
        print("Добавить новый фильм - нажмите 1")
        print("Выбрать фильм для продажи билета - нажмите 2")

        choice = input()

        if choice == '1':
            title = input("Введите название фильма: ")
            start_date = datetime.strptime(input("Введите дату начала показа фильма (гггг-мм-дд): "), "%Y-%m-%d")
            end_date = datetime.strptime(input("Введите дату окончания показа фильма (гггг-мм-дд): "), "%Y-%m-%d")
            film = Film(title, start_date, end_date)

            times = input("Введите доступные времена показа через запятую (например, 10:00,14:30): ")
            film.add_show_times(times.split(','))

            film.add_show_dates(start_date, end_date)
            films.append(film)

