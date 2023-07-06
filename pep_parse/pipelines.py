from collections import defaultdict
from datetime import datetime
from pathlib import Path

from pep_parse.settings import (
    BASE_DIR, RESULTS_DIR, STATISCTIC_FILENAME
)


class PepParsePipeline:
    def open_spider(self, spider):
        self.statistic = defaultdict(int)

    def process_item(self, item, spider):
        self.statistic[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = Path.joinpath(
            BASE_DIR, RESULTS_DIR,
            STATISCTIC_FILENAME.format(
                datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            )
        )
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write('Status,Amount\n')
            for status, num in sorted(
                self.statistic.items(),
                key=lambda item: item[1],
                reverse=True
            ):
                file.write(f'{status},{num}\n')
            file.write(f'Total,{sum(self.statistic.values())}\n')
