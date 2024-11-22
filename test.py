from blog.models import Post, Category, Comment  # Замените myapp на имя вашего приложения
from django.contrib.auth.models import User
from django.utils import timezone

# Создаем тестового пользователя
user = User.objects.create(username="test_user")

# Создаем категорию
category = Category.objects.create(name="Tutorial")

# Создаем пост и добавляем к нему категорию
post = Post.objects.create(title="My First Post", content="This is a test post.", author=user, published_date=timezone.now())
post.categories.add(category)  # Добавляем категорию к посту

# Создаем комментарий к посту
comment = Comment.objects.create(post=post, author=user, content="Great post!", published_date=timezone.now())

# Проверяем, что объекты созданы и работают
print(post)           # Должен вывести объект Post с названием "My First Post"
print(post.categories.all())  # Должен вывести QuerySet с категорией "Tutorial"
print(post.comments.all())    # Должен вывести QuerySet с комментарием "Great post!"
