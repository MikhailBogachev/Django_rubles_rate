from typing import Any
from datetime import date
import datetime
import requests

from django.core.management.base import BaseCommand, CommandParser

from core.models import RublesRate


class Command(BaseCommand):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    hhtp_status_code_ok = 200

    @staticmethod
    def _get_date(delta):
        return date.today() + datetime.timedelta(days=int(delta))

    @staticmethod
    def _get_url_for_prev_date(_date):
        year = _date.year
        month = f'0{_date.month}' if _date.month < 10 else _date.month
        day = f'0{_date.day}' if _date.day < 10 else _date.day
        return f'https://www.cbr-xml-daily.ru/archive/{year}/{month}/{day}/daily_json.js'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('delta', type=int, nargs='?', help='date for which data should be downloaded')

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        _date = date.today()
        if kwargs['delta']:
            _date = self._get_date(kwargs['delta'])
            self.url = self._get_url_for_prev_date(_date)

        response = requests.get(url=self.url)
        if response.status_code == self.hhtp_status_code_ok:
            list_objs = []
            for valute, data in response.json()['Valute'].items():
                list_objs.append(RublesRate(charcode=valute, date=_date, rate=data['Value']))
            RublesRate.objects.bulk_create(list_objs)
            self.stdout.write(f'Loading of {len(list_objs)} objects for {_date} succesfully completed')
        else:
            self.stdout.write('Unsuccesfully')
