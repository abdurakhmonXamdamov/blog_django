from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True)
  avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')

  def __str__(self):
    return f"{self.user.username}'s Profile"

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    Img = Image.open(self.avatar.path)
    if Img.height > 300 or Img.width > 300:
      output_size = (300, 300)
      Img.thumbnail(output_size)
      Img.save(self.avatar.path)

