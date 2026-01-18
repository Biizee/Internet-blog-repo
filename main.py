import django_setup

from blog.models import Post, Comments


#!--Creating post and some comments related to this post
#first_post = Post.objects.create(
#    name = "Як встановити пайтон?",
#    text = "Я хочу навчитися програмувати на пайтоні, як його правильно встановити, щоб потім не вертатися до цього.",
#
#)
#
#first_comment = Comments.objects.create(
#    text = "Глянь відео на ютубі, я хз",
#    autor = "Сергій2010",
#    #related_to_post = first_post,
#
#)
#
#second_comment = Comments.objects.create(
#    text = "Руками",
#    autor = "Степан[Prime]",
#    #related_to_post = first_post,
#    
#)

#!--Finding post and comments by their id
first_post = Post.objects.get(id = 1)
first_comment = Comments.objects.get(id = 1)
second_comment = Comments.objects.get(id = 2)

#!--Relating comments to post
#first_comment.many_to_many.add(first_post)
#second_comment.many_to_many.add(first_post)

#!--Changing text of first post
first_post.text = "Я хочу навчитися програмувати на пайтоні, як його правильно встановити, щоб потім не вертатися до цього. Тільки будь ласка без глупих відповідей."
first_post.save()


#!--Creating and delete second post for testing
#second_post = Post.objects.create(
#    name = "Gugugaga",
#    text = "Gugugugagagugugau",
#
#)

second_post = Post.objects.get(id = 4)
second_post.delete()
