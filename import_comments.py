from pymongo import MongoClient
import csv

client = MongoClient('localhost', 27017)
db = client.parsing
collection = db.atera_comments
with open('export.csv', mode='w') as csv_file:
    fieldnames = ['Datetime', 'Comment Description', 'User Name', 'no. of Upvotes', 'Related Post Name',
                  'Official Comment?', 'URL \\ Permalink']
    writer = csv.DictWriter(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
    writer.writeheader()

    for doc in collection.find():
        if 'comment_votes' in doc:
            votes = doc['comment_votes']
        else:
            votes = ''
        if 'comment_official' in doc:
            official = doc['comment_official']
        else:
            official = ''
        writer.writerow({'Datetime': doc['comment_datetime'], 'Comment Description': doc['comment_text'],
                         'User Name': doc['comment_author'], 'no. of Upvotes': votes,
                         'Related Post Name': doc['related_post'], 'Official Comment?': official,
                         'URL \\ Permalink': doc['comment_url']})
