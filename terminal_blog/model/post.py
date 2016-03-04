import uuid

from EightApps.terminal_blog.database import Database
import datetime


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        #uuid4 create random uuid
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date = date

        # post = Post(blog_id="123", title="a title", content="some content", author="Jose")

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'id' : self.id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title' : self.title,
            'created_date' : self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        # Post.from_mango('123')
        post_data =  Database.find_one(collection='posts', query={'id' : id})
        return cls(
            blog_id=post_data['blog_id'],
            title=post_data['title'],
            content=post_data['content'],
            author=post_data['author'],
            date=post_data['created_date'],
            id=post_data['id']
        )

    @staticmethod
    def from_blog(id):
        # Post.from_blog('123')
        return [post for post in Database.find(collection='posts', query={'blog_id' : id})]
