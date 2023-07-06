from pathlib import Path


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

ALLOWED_DOMAIN = 'peps.python.org'

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
STATISCTIC_FILENAME = 'status_summary_{}.csv'

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
