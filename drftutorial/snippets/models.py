from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save,pre_delete,post_delete,m2m_changed



LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    birthdate = models.DateField()


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name

class Track(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

@receiver(pre_save, sender=Book)
def pre_save_book_handler(sender, instance,*args, **kwargs):
    print(f"About to save book: {instance.title}")
    print(args, kwargs)


@receiver(post_save, sender=Book)
def post_save_book_handler(sender, instance, created,*args, **kwargs):
    print(args,kwargs)
    if created:
        print(f"New book created: {instance.title}")
    else:
        print(f"Book updated: {instance.title}")


# note we cant save the instance again we can assign it to some value like 
# instanse.fild_name = instanse.another_created or upadated field in pre_save 
# because if we try to do so we will stuck in the infinte loop 

@receiver(pre_delete, sender=Book)
def pre_delete_handler(sender, instance, **kwargs):
    # Perform actions before the model is deleted
    print(f"About to delete: {instance}")

@receiver(post_delete, sender=Book)
def post_delete_handler(sender, instance, **kwargs):
    # Perform actions after the model is deleted
    print(f"Deleted: {instance}")


@receiver(m2m_changed,sender=Book.authors.through)
def m2m_changed_handler(sender, instance, action,*args,**kwargs):
    # print(args,kwargs)
    if action == 'pre_add':
        print("was added")
        qs=kwargs.get("model").objects.filter(pk__in=kwargs.get("pk_set"))
        print(qs.count())