from pymongo import MongoClient
import csv

client = MongoClient('localhost', 27017)
db = client.parsing
collection = db.atera_posts
with open('export.csv', mode='w') as csv_file:
    fieldnames = ['Post Title', 'Datetime', 'Post Description', 'User Name', 'no. of Upvotes', 'Post Status',
                  'URL \\ Permalink']
    writer = csv.DictWriter(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
    writer.writeheader()

    for doc in collection.find():
        if 'post_status' in doc:
            status = doc['post_status']
        else:
            status = ''
        writer.writerow({'Post Title': doc['post_title'], 'Datetime': doc['post_datetime'],
                         'Post Description': doc['post_text'], 'User Name': doc['post_author'],
                         'no. of Upvotes': doc['post_votes'], 'Post Status': status,
                         'URL \\ Permalink': doc['post_url']})
