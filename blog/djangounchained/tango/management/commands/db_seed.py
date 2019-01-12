import os
import ast
import importlib.machinery
from django.core.management import BaseCommand
import sys


class Command(BaseCommand):
    help = 'Seed the database with records'

    def handle(self, *args, **options):
        self.run_seeds()

    @staticmethod
    def run_seeds():
        app_name = os.getenv('APP_NAME') + '.database_seeder'
        module = importlib.import_module(app_name)
        database_seeder_class = getattr(module, 'DatabaseSeeder')

        for seed in database_seeder_class.seeds:
            seed.run()
