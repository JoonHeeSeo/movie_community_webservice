from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import requests


# get_movies_API view를 실행
def execute_view():
    response = requests.get('http://localhost:8000/movies/get/movies/')
    print(response.text)

class Command(BaseCommand):
    help = 'Starts the Django development server and executes a view'

    def handle(self, *args, **options):
        # Create a scheduler instance
        scheduler = BackgroundScheduler()

        # Add a job to execute the view at an interval
        trigger = IntervalTrigger(minutes=60)
        scheduler.add_job(execute_view, trigger)

        # Start the scheduler
        scheduler.start()

        try:
            # Start the Django development server
            from django.core.management import execute_from_command_line
            execute_from_command_line(['manage.py', 'runserver', '--noreload'])
        except KeyboardInterrupt:
            # Stop the scheduler when the server is interrupted
            scheduler.shutdown()