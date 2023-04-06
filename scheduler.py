from apscheduler.schedulers.background import BackgroundScheduler


class Scheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def add_schedule(self, func, type, run_date, args=None, kwargs=None, timezone=None):
        self.scheduler.add_job(
            func, type, run_date=run_date, args=args, kwargs=kwargs, timezone=timezone
        )

    def clear_schedule(self):
        self.scheduler.remove_all_jobs()  # remove all jobs

    def print_jobs(self):
        # Print all jobs
        for job in self.scheduler.get_jobs():
            print(job)
