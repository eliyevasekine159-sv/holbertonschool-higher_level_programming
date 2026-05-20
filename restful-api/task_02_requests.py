#!/usr/bin/python3
"""
Module to fetch posts from an API and print them or save them to a CSV file
"""
import csv
import requests


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder and saves them to a CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()

        # CSV üçün lazım olan sütun adlarını təyin edirik
        fieldnames = ['id', 'title', 'body']

        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for post in posts:
                # Yalnız id, title və body məlumatlarını süzüb fayla yazırıq
                writer.writerow({
                    'id': post.get('id'),
                    'title': post.get('title'),
                    'body': post.get('body')
                })
