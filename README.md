# dom-scrapy

* added scrapper and importer to csv for dashboard service zendesk.com

## commands for export:
* mongoexport --db parsing --collection ateraj_comments --type csv --fields id,body,author_id,vote_sum,vote_count,official,html_url,created_at,updated_at,url,post_id --out comments.csv
* mongoexport --db parsing --collection ateraj_posts --type csv --fields id,title,details,author_id,vote_sum,vote_count,comment_count,follower_count,topic_id,html_url,created_at,updated_at,url,featured,pinned,closed,status --out posts.csv

* mongoexport --db parsing --collection ateraj_comments --out comments.json