from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
MATH_CHOICES = (('arithmetic'),
    ('algebra'),
    ('analysis'),
    ('calculus'),
    ('combinatorics'),
    ('geometry'),
    ('probability'),
    ('topology')
)

SOLUTION_STATUS = (('unsolved'),
    ('solved')
)

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    content = models.CharField(max_length=200, unique=True)
    area = models.CharField(max_length=15, choices=MATH_CHOICES, default='arithmetic')
    outcome = models.CharField(max_length=10, choices=SOLUTION_STATUS, default='unsolved')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
