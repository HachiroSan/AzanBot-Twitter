import datetime
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
import pytz
from func import (
    post_tweet,
    get_Azan_Schedule_from_API,
    get_locale_from_Timezone,
    get_next_azan_time,
)
import time
from rich.status import Status
from tweety import Tweety
from rich.console import Console, group
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.style import Style
from log import LogContainer

# Set timezone to Malaysia
timezone = pytz.timezone("Asia/Kuala_Lumpur")


class AzanBot:
    def __init__(self, location):
        self.location = location
        self.tweety = Tweety()
        self.scheduler = BackgroundScheduler()
        self.console = Console()
        self.logscontainer = LogContainer(max_size=20)

        # Flag to check if the run() method has been run
        self.has_been_run = False

        # Schedule task to run at 12:01 AM every day
        self.scheduler.add_job(
            self.update_schedule, "cron", hour="00", minute="01", second="0"
        )

    def get_data(self):
        self.prayer_schedule = get_Azan_Schedule_from_API(self.location)

    def create_cron(self):
        self.logscontainer.add_log(
            f'Adding new azan schedule {datetime.datetime.now(timezone).strftime("%d/%m/%Y")}'
        )
        for azan_type, time in self.prayer_schedule.items():
            time = datetime.datetime.strptime(time, "%H:%M")
            # Schedule tasks to run at specific times, using 'date' trigger
            run_date = datetime.datetime.now(timezone).replace(
                hour=time.hour, minute=time.minute
            )
            self.scheduler.add_job(
                post_tweet,
                "date",
                run_date=run_date,
                args=[self.tweety, azan_type, time, self.location, self.logscontainer],
            )
            self.logscontainer.add_log(
                "Added job schedule: "
                + azan_type.capitalize()
                + " at "
                + time.strftime("%H:%M")
            )

    def Info_Panel(self):
        screen_name = self.tweety.get_username()
        user_id = self.tweety.get_id()
        location = self.tweety.get_location()
        followers_count = self.tweety.get_followers_count()
        bio = self.tweety.get_bio()
        favourites_count = self.tweety.get_favourites_count()
        total_statuses = self.tweety.get_status_count()
        table = Table(show_header=False, show_lines=False)
        table.add_column("Key", justify="right", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")
        table.add_row("Twitter", "@" + screen_name)
        table.add_row("Twitter Id", user_id)
        table.add_row("Followers", followers_count)
        table.add_row("location", location)
        table.add_row("Total Likes", favourites_count)
        table.add_row("Total Status", total_statuses)
        test = table.add_row("Bio", bio)
        return table

    @group()
    def Data_Panel(self):
        highlight = Style(color="red", bold=True, bgcolor="green", blink=True)
        current_date = datetime.datetime.now(timezone).strftime("%d/%m/%Y")
        table = Table()
        table.add_column("Prayer", justify="right", style="cyan", no_wrap=True)
        table.add_column("Time", style="magenta")
        next_azan = get_next_azan_time(self.prayer_schedule)
        for azan_type, time in self.prayer_schedule.items():
            time = datetime.datetime.strptime(time, "%H:%M")
            if azan_type == next_azan:
                table.add_row(
                    azan_type.capitalize(), time.strftime("%H:%M"), style=highlight
                )
                continue
            # Schedule tasks to run at specific times
            table.add_row(azan_type.capitalize(), time.strftime("%H:%M"))
        up_next = Text("Up Next: " + next_azan.capitalize(), style="bold red")
        time_left = Text(
            "Time Left: ",
            style="bold red",
        )
        time_left.append(time.strftime("%H:%M:%S"), style="bold yellow")
        yield Align(table, align="center")
        yield Align(up_next, align="center")

    def Header_Left(self):
        zone, locale = get_locale_from_Timezone(self.location)
        timezone_text = Text(justify="center")
        timezone_text.append("  Timezone: ", style="bold red")
        timezone_text.append("[" + zone + "]", style="bold yellow")

        # locale_text = Text(no_wrap=True)
        # locale_text.append("  Locale: ", style="bold red")
        # locale_text.append(locale, style="bold yellow")

        return timezone_text

    def Header_Center(self):

        title = Text("AzanBot", style="bold green")

        return title

    def Header_Right(self):
        date_txt = Text(justify="center")
        date_txt.append("Date: ", style="bold red")
        date_txt.append(
            datetime.datetime.now(timezone).strftime("%d/%m/%Y"), style="bold yellow"
        )
        date_txt.append("  Time: ", style="bold red")
        date_txt.append(
            datetime.datetime.now(timezone).strftime("%H:%M:%S"), style="bold yellow"
        )

        return date_txt

    def Log_Panel(self):
        logscontainer = self.logscontainer
        table = Table(show_header=False, show_edge=False, show_lines=False)

        table.add_column("Date", justify="right", style="cyan", no_wrap=True)
        table.add_column("String", style="magenta")

        logs = logscontainer.get_logs()
        for log in logs:
            table.add_row(log[0], log[1])

        return table

    def Footer_Panel(self):
        text = Text(
            "Github @Muhd_Farhad | version 1.0",
            style="bold white",
        )
        return text

    def generate_dashboard(self):
        layout = Layout()
        # Divide the "screen" in to three parts
        layout.split_column(
            Layout(name="header", size=3),
            Layout(ratio=1, name="main"),
            Layout(size=3, name="footer"),
        )

        # Divide the "main" layout in to "side" and "body"
        layout["main"].split_row(Layout(name="side"), Layout(name="body", ratio=2))
        # Divide the "side" layout in to two
        layout["side"].split_column(Layout(name="side_top"), Layout(name="side_bottom"))

        layout["header"].split_row(
            Layout(name="header_left"),
            Layout(name="header_center"),
            Layout(name="header_right"),
        )

        layout["header_left"].update(
            Panel(Align(self.Header_Left(), "center", vertical="middle"))
        )
        layout["header_center"].update(
            Panel(Align(self.Header_Center(), "center", vertical="middle"))
        )
        layout["header_right"].update(
            Panel(Align(self.Header_Right(), "center", vertical="middle"))
        )
        layout["body"].update(
            Panel(
                Align(self.Log_Panel(), "center", vertical="middle"),
                title="[yellow]Logs",
                border_style="cyan",
            )
        )

        layout["side_top"].update(
            Panel(
                Align(self.Info_Panel(), "center", vertical="middle"),
                title="[yellow]Twitter Profile",
                border_style="red",
            )
        )

        layout["side_bottom"].update(self.Data_Panel())

        layout["footer"].update(Align(self.Footer_Panel(), "center", vertical="middle"))
        return layout

    def update_schedule(self):
        self.get_data()
        self.create_cron()
        self.logscontainer.add_log("Updated new schedule")

    def run_job(self, job):
        if job == 0:
            self.get_data()
        elif job == 1:
            self.create_cron()
        elif job == 2:
            # Start scheduler
            self.scheduler.start()

    def run(self):
        self.logscontainer.add_log("Starting Azan Bot for the first time")
        self.has_been_run = True

        jobs = [
            "Fetching data from API",
            "Creating jobs schedule",
            "Starting scheduler",
        ]

        # For loop
        with Status("Preparing the recipe") as status:
            for i, job in enumerate(jobs):
                self.run_job(i)
                status.update(job)
                time.sleep(1)

        with Live(
            self.generate_dashboard(), refresh_per_second=30
        ) as live:  # update 4 times a second to feel the fluid
            while True:
                live.update(self.generate_dashboard())
