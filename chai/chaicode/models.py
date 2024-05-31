from django.db import models
from django.contrib.auth import User
# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')

  def __str__(self):
    return self.name


#one to many 
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')# cascade then when a post is deleted, all its associated comments will also be deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
