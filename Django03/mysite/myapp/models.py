from django.db import models


class Author(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first} {self.last}"


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    posted_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    comment = models.TextField(null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.author}'s comment"


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)