import requests
from news.config import *
import sqlite3


class Stories(object):
    conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
    cursor = conn.cursor()  # Open a cursor to perform database operations

    @staticmethod
    def get_story_ids(category):                                    # get stories ids in selected category
        category_url = (category_url_for_request % category)
        response = requests.get(category_url, timeout=5)            # send request to api. get all categories IDs
        data = response.json()
        return data

    @staticmethod
    def get_story_details(i):                                       # get all fields from particular story
        url_for_items = (item_url_for_request % i)
        current_item = requests.get(url_for_items, timeout=5)
        current_story = current_item.json()
        return current_story

    @staticmethod
    def write_to_var_from_response(story_id):                       # write data from json into variables
        item_variables = {
            'author': story_id.get('by'),
            'descendants': story_id.get('descendants'),
            'story_id': story_id.get('id'),
            'score': story_id.get('score'),
            'text': story_id.get('text'),
            'time': story_id.get('time'),
            'title': story_id.get('title'),
            'type': story_id.get('type'),
            'url': story_id.get('url')
        }

        return item_variables

    def get_stories(self, story_title, insert_query, category_id):
        id_list = Stories.get_story_ids(story_title)

        for i in id_list[:1]:
            current_story = Stories.get_story_details(i)

            var_db = Stories.write_to_var_from_response(current_story)
            print(var_db)
            Stories.cursor.execute(insert_query,
                                   (var_db['author'], var_db['descendants'], var_db['story_id'], var_db['score'],
                                    var_db['text'], var_db['time'], var_db['title'], var_db['type'], story_title,
                                    var_db['url'], category_id))

            Stories.conn.commit()


def execute():
    instance = Stories()
    instance.get_stories('askstories', insert_story_query, 1)
    instance.get_stories('newstories', insert_story_query, 2)
    instance.get_stories('jobstories', insert_story_query, 3)
    instance.get_stories('showstories', insert_story_query, 4)