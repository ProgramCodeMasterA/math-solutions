from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
MATH_CHOICES = (('arithmetic','Arithmetic'),
    ('algebra','Algebra'),
    ('analysis','Analysis'),
    ('calculus','Calculus'),
    ('combinatorics','Combinatorics'),
    ('geometry','Geomoetry'),
    ('probability','Probability'),
    ('topology','Topology')
)


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    content = models.CharField(max_length=200, unique=True) # Type in the content of your math problem
    area = models.CharField(max_length=15, choices=MATH_CHOICES, default='arithmetic')  # Choose which category of Maths the problem is
    problem = models.BooleanField(default=False)    # True/False if math problem is solved
    created_on = models.DateTimeField(auto_now_add=True)    # Add DateTine field
    status = models.IntegerField(choices=STATUS, default=0) # Define if object is a draft or is published post
