import uuid

import datetime

from EightApps.web_blog.src.common.database import Database


class Post(object):

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        #uuid4 create random uuid
        self._id = uuid.uuid4().hex if _id is None else _id
        self.created_date = created_date

        # post = Post(blog_id="123", title="a title", content="some content", author="Jose")

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title' : self.title,
            'created_date' : self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        # Post.from_mango('123')
        post_data =  Database.find_one(collection='posts', query={'_id' : id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        # Post.from_blog('123')
        return [post for post in Database.find(collection='posts', query={'blog_id' : id})]
