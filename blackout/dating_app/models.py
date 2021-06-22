from django.db import models
from login_app.models import User
from datetime import datetime

# Create your models here.
class ProfileManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if post_data['gender'] == "Select your Gender":
            errors['gender'] = 'Please select: Prefer not to say, if you do not wish to disclose.'
        if post_data['birthday'] == "":
            errors['birthday'] = "Birthday must be populated"
        elif post_data['birthday'] > datetime.now().strftime("%Y-%m-%d"):
            errors['birthday'] = "Invalid Birthday, Must be in the past"
        if post_data['color'] == "Select your favorite color":
            errors['color'] = 'Please select a color.'
        if len(post_data['sport']) < 3:
            errors['sport'] = 'Sport should be more than 2 characters.'
        if len(post_data['movie']) < 3:
            errors['movie'] = 'Movie Title should be more than 2 characters.'
        if len(post_data['music']) < 3:
            errors['music'] = 'Music Genre should be more than 2 characters.'
        return errors
    
    def updater(self, post_data):
        errors = {}
        if post_data['color'] == "Select your favorite color":
            errors['color'] = 'Please select a color.'
        if len(post_data['sport']) < 3:
            errors['sport'] = 'Sport should be more than 2 characters.'
        if len(post_data['movie']) < 3:
            errors['movie'] = 'Movie Title should be more than 2 characters.'
        if len(post_data['music']) < 3:
            errors['music'] = 'Music Genre should be more than 2 characters.'
        return errors

class Profile(models.Model):
    gender = models.CharField(max_length = 255)
    birthday = models.DateField()
    color = models.CharField(max_length = 255)
    sport = models.CharField(max_length = 255)
    movie = models.CharField(max_length = 255)
    music = models.CharField(max_length = 255)
    creator = models.ForeignKey(User, related_name='user_profile', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_likes = models.ManyToManyField(User, related_name='user_matches')
    image = models.ImageField(upload_to='images', default="default.jpg")
    objects = ProfileManager()