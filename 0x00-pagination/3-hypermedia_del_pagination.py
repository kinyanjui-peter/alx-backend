#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset
    
    def mark_row_deleted(self, index: int):
        """Mark a row as deleted."""
        self.deleted_rows.append(index)

    def deleted_rows(self) -> List[int]:
        """Returns a list of indices of deleted rows."""
        return self.deleted_rows

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient hypermedia pagination: a fuction that ensure
        consistency even if a data, or page is deleted
        """

        data = []

        start_index = index * page_size
        next_index = start_index + page_size
        dataset_length = len(self.dataset())
        # dataset = self.dataset()
        # check validity of start index
        assert start_index < dataset_length

        # replace deleted dataset with follwing dataset
        deleted_rows = self.deleted_rows()
        for row_index in deleted_rows:
            if row_index < next_index:
                start_index += 1
                
        for i in range(start_index, min(next_index, dataset_length)):
            data.append(self.dataset()[i])

        return {
            'index': start_index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
