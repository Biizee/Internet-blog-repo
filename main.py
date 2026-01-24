import django_setup

from blog.models import Post, Comments
from django.core.exceptions import ObjectDoesNotExist

def create_post():
    name = input("Enter post title: ")
    text = input("Enter post text: ")
    post = Post.objects.create(
        name = name, text = text
    )
    print(f"\nYour post created!")

def list_all_posts():
    posts = Post.objects.all()
    if posts:
        for post in posts:
            i = 1
            print(f"\nPost id - {post.id}. \nPost name - {post.name}. \nPost text - {post.text}. \nPost date - {post.date_with_time}.")
            comments = Comments.objects.filter(to_post = post)
            if comments:
                for comm in comments:
                    print(f"(Id - {comm.id}) Nr {i} - {comm.text}")
                    i += 1

def create_comm():
    text = input("\nEnter comment text: ")
    author = input("\nEnter your nicname: ")
    try:
        to_post = int(input("\nEnter post id: "))
        to_post = Post.objects.get(id = to_post)
        comment = Comments.objects.create(
            text = text,
            autor = author,
            to_post = to_post

        )
        print(f"\nComment was succesfully created!")
    except ObjectDoesNotExist:
        print(f"\nPost doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def edit_post():
    try:
        post = int(input("Enter post id: "))
        post = Post.objects.get(id = post)
        new_name = input("\nEnter new name for post (leave blank to keep current): ")
        if new_name:
            post.name = new_name
            new_text = input("Enter new text for post (leave blank to keep current): ")
            if new_text:
                post.text = new_text
        post.save()
        print("\nPost edited succesfully!")
    except ObjectDoesNotExist:
        print(f"\nPost doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_post():
    try:
        post = int(input("Enter post id: "))
        post = Post.objects.get(id = post)
        post.delete()
        print("\nPost deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nPost doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def edit_comment():
    try:
        comm = int(input("Enter comment id: "))
        comm = Comments.objects.get(id = comm)
        new_text = input("Enter new text for comment (leave blank to keep current): ")
        if new_text:
            comm.text = new_text
        comm.save()
        print("\nComment edited succesfully!")
    except ObjectDoesNotExist:
        print(f"\nComment doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_comm():
    try:
        comm = int(input("Enter comment id: "))
        comm = Comments.objects.get(id = comm)
        comm.delete()
        print("\nComment deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nComment doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

while True:
    print("""
Options:
1. Create post
2. List all posts and comments
3. Create comment to post
4. Edit post
5. Delete post
6. Edit comment
7. Delete comment
8. Exit""")
    
    try:
        choice = int(input("\nEnter your choice: "))
    except Exception as e:
        print(f"Error: {e}")
    
    if choice == 8:
        break

    elif choice == 1:
        create_post()
    
    elif choice == 2:
        list_all_posts()

    elif choice == 3:
        create_comm()
    
    elif choice == 4:
        edit_post()
    
    elif choice == 5:
        delete_post()
    
    elif choice == 6:
        edit_comment()
    
    elif choice == 7:
        delete_comm()

    else:
        print("Invalid choice, try again!")
