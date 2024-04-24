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
