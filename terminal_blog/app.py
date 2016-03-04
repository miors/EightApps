import pymongo

from EightApps.terminal_blog.database import Database
from EightApps.terminal_blog.menu import Menu
from EightApps.terminal_blog.model.blog import Blog
#from EightApps.terminal_blog.model.post import Post

Database.initialize()

# post = Post(blog_id="123",
#             title="Another great post",
#             content="This is some sample content",
#             author="Jose")
#
# post.save_to_mongo()

### post = Post.from_mongo('ae1f998026d64d298f8d4e28bb48fd6e')
### print(post)
###
### posts = Post.from_blog('123')
### for post in posts:
###     print(post)

#-- blog = Blog(author="Jose",
#--            title="Sample title",
#--             description="Sample description")
#--
#-- blog.new_post()
#--
#-- blog.save_to_mongo()
#--
#-- from_database = Blog.from_mongo(blog.id)
#--
#-- print(blog.get_posts()) # Post.from_blog(id)

menu = Menu()
menu.run_menu()

# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']

# find data in collection
#students = collection.find({})
#for student in students:
#    print(student)

# students = [student for student in collection.find({})]
# print(students)
#
# students_mark = [student['mark'] for student in collection.find({}) if student['mark'] == 100.0 ]
# print(students_mark)
#
# post = Post("Post1 title", "Post1 content", "Post1 author")
# post2 = Post("Post2 title", "Post2 content", "Post2 author")
# post2.content = "Some different content"
#
# print(post.content)
# print(post2.content)


