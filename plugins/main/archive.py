"""Add 'archive_year' and 'archive_month' variables to the global context.

Each one is a list containing (date, [Article, ]), sorted by date-decending
"""
from   collections import defaultdict
from   datetime import date

from   pelican import signals

def create_archive(generator):
    archive_year = []
    current_year = None
    current_year_list = []

    archive_month = []
    current_month = None
    current_month_list = []

    for article in generator.context['articles']:
        article_date = article.date
        if current_year is None or current_year != article_date.year:
            current_year = article_date.year
            current_year_list = []
            archive_year.append((date(current_year,1,1), current_year_list))
        current_year_list.append(article)

        if current_month is None or current_month != article_date.month:
            current_month = article_date.month
            current_month_list = []
            archive_month.append((date(current_year, current_month,1), current_month_list))
        current_month_list.append(article)

    generator.context['archive_year'] = archive_year
    generator.context['archive_month'] = archive_month


def register():
    signals.article_generator_finalized.connect(create_archive)
    signals.page_generator_finalized.connect(create_archive)
