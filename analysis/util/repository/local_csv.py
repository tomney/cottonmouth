from util.repository.base_class import Repository
from typing import List
import csv


class LocalCsv(Repository):
    @staticmethod
    def write(input: List[dict]):
        with open('local.csv', "w") as local_file:
            writer = csv.writer(local_file, delimiter=",")
            writer.writerow(input[0].keys())
            for datum in input:
                writer.writerow(datum.values())
