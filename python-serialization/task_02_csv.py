#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            # DictReader sütun adlarını açar (key) kimi istifadə edir
            csv_reader = csv.DictReader(csv_f)
            for row in csv_reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data, json_f)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
