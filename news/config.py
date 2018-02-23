category_url_for_request = "https://hacker-news.firebaseio.com/v0/%s.json?print=pretty"
item_url_for_request = "https://hacker-news.firebaseio.com/v0/item/%i.json?print=pretty"

#insert_story_query = "INSERT INTO news_story (author, descendants, story_id, kids, score, text, time, title, type, category_name, url, category_id_id) " \
                        #"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"



insert_story_query = "INSERT INTO news_story (author, descendants, story_id, score, text, time, title, type, category_name, url, category_id_id)  " \
                     "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"