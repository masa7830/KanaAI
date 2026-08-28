import tkinter as tk
from tkinter import simpledialog, messagebox
import calendar
from datetime import date, timedelta
from pathlib import Path

SCHEDULE_FILE = Path("schedule.txt")


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana Calendar")
        self.root.geometry("650x500")

        today = date.today()

        self.year = today.year
        self.month = today.month
        self.selected_date = None

        # 上部
        top_frame = tk.Frame(root)
        top_frame.pack(pady=10)

        previous_button = tk.Button(
            top_frame,
            text="←",
            command=self.previous_month
        )
        previous_button.pack(side="left")

        self.month_label = tk.Label(
            top_frame,
            text="",
            font=("Arial", 16)
        )
        self.month_label.pack(
            side="left",
            padx=20
        )

        next_button = tk.Button(
            top_frame,
            text="→",
            command=self.next_month
        )
        next_button.pack(side="left")

        # カレンダー部分
        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.pack(pady=10)

        # 予定表示
        self.schedule_label = tk.Label(
            root,
            text="Kana:日付を選んでね！",
            justify="left"
        )
        self.schedule_label.pack(pady=10)

        # 予定追加
        add_button = tk.Button(
            root,
            text="この日に予定を追加",
            command=self.add_schedule
        )
        add_button.pack(pady=10)

        self.show_calendar()


    def show_calendar(self):
        # 前のカレンダー表示を消す
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        self.month_label.config(
            text=f"{self.year}年{self.month}月"
        )

        week_names = [
            "月", "火", "水",
            "木", "金", "土", "日"
        ]

        for column, name in enumerate(week_names):
            label = tk.Label(
                self.calendar_frame,
                text=name,
                width=6
            )

            label.grid(
                row=0,
                column=column
            )

        # 月のカレンダー情報を取得
        month_calendar = calendar.monthcalendar(
            self.year,
            self.month
        )

        for row_index, week in enumerate(
            month_calendar,
            start=1
        ):
            for column_index, day in enumerate(week):

                if day == 0:
                    label = tk.Label(
                        self.calendar_frame,
                        text="",
                        width=6
                    )

                    label.grid(
                        row=row_index,
                        column=column_index
                    )

                else:
                    button = tk.Button(
                        self.calendar_frame,
                        text=str(day),
                        width=5,
                        command=lambda d=day:
                            self.select_date(d)
                    )

                    button.grid(
                        row=row_index,
                        column=column_index,
                        padx=2,
                        pady=2
                    )


    def select_date(self, day):
        self.selected_date = date(
            self.year,
            self.month,
            day
        )

        schedules = self.get_schedule(
            self.selected_date
        )

        if schedules:
            text = "\n".join(
                f"・{schedule}"
                for schedule in schedules
            )
        else:
            text = "予定はないよ！"

        self.schedule_label.config(
            text=
            f"Kana:{self.month}月{day}日の予定だよ！\n"
            f"{text}"
        )


    def add_schedule(self):
        if self.selected_date is None:
            messagebox.showinfo(
                "Kana",
                "先に日付を選んでね！"
            )
            return

        schedule = simpledialog.askstring(
            "Kana",
            f"{self.selected_date}の予定を入力してね"
        )

        if not schedule:
            return

        repeat = messagebox.askyesno(
            "繰り返し設定",
            "毎週繰り返しますか？"
        )

        if repeat:
            count = simpledialog.askinteger(
                "Kana",
                "何回登録しますか？",
                minvalue=1
            )

            if count is None:
                return

        else:
            count = 1

        current_date = self.selected_date

        with SCHEDULE_FILE.open(
            "a",
            encoding="utf-8"
        ) as file:

            for _ in range(count):
                file.write(
                    f"{current_date},{schedule}\n"
                )

                current_date += timedelta(
                    weeks=1
                )

        self.select_date(
            self.selected_date.day
        )


    def get_schedule(self, selected_date):
        schedules = []

        if not SCHEDULE_FILE.exists():
            return schedules

        with SCHEDULE_FILE.open(
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:
                line = line.strip()

                if not line:
                    continue

                schedule_date, schedule = \
                    line.split(",", 1)

                if schedule_date == \
                        selected_date.isoformat():

                    schedules.append(schedule)

        return schedules


    def next_month(self):
        self.month += 1

        if self.month > 12:
            self.month = 1
            self.year += 1

        self.selected_date = None
        self.schedule_label.config(
            text="Kana:日付を選んでね！"
        )

        self.show_calendar()


    def previous_month(self):
        self.month -= 1

        if self.month < 1:
            self.month = 12
            self.year -= 1

        self.selected_date = None
        self.schedule_label.config(
            text="Kana:日付を選んでね！"
        )

        self.show_calendar()


def open_calendar():
    window = tk.Toplevel()
    CalendarApp(window)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    open_calendar()

    root.mainloop()