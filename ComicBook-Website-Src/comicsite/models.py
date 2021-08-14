# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.utils import timezone


class Comic(models.Model):
    comicid = models.AutoField(db_column='comicID', primary_key=True)  # Field name made lowercase.
    comictitle = models.CharField(db_column='comicTitle', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    comicplot = models.TextField(db_column='comicPlot', blank=True, null=True)  # Field name made lowercase.
    comicpublisher = models.CharField(db_column='comicPublisher', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    comicseries = models.CharField(db_column='comicSeries', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    comicvolume = models.IntegerField(db_column='comicVolume', blank=True, null=True)  # Field name made lowercase.
    comicissue = models.IntegerField(db_column='comicIssue', blank=True, null=True)  # Field name made lowercase.
    comicgenre = models.CharField(db_column='comicGenre', max_length=45, blank=True,
                                  null=True)  # Field name made lowercase.
    comicauthor = models.CharField(db_column='comicAuthor', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    comicsynopsis = models.TextField(db_column='comicSynopsis', blank=True, null=True)  # Field name made lowercase.
    comicrating = models.IntegerField(db_column='comicRating', blank=True, null=True)  # Field name made lowercase.
    comiccover = models.CharField(db_column='comicCover', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'comic'


class Comment(models.Model):
    # a integer field which uniquely identifies the comment
    commentid = models.AutoField(primary_key=True)
    # the id of the user who made this comment
    userid = models.IntegerField(null=False)
    # specifies whether this comment is for a comic or a post
    type = models.CharField(max_length=32)
    # the id of the comic or post on which this comment was made
    pageid = models.IntegerField(null=False)
    # the actual comment itself
    text = models.TextField(blank=False)
    # the date of the comment
    date = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        managed = True
        db_table = 'comments'


class Rating(models.Model):
    # a integer field which uniquely identifies the rating
    ratingid = models.AutoField(primary_key=True)

    # the id of the user who made this rating
    userid = models.IntegerField(null=False)

    # the id of the comic being rated
    comicid = models.IntegerField(null=False)

    # the actual rating, from 1 to 5
    rating = models.IntegerField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'ratings'

'''
class PostRating(models.Model):
    # the post id
    postid = models.AutoField(primary_key=True)
    # user id 
    userid = models.IntergerField(null=False)
    # rating of the post in boolean value
    post_rating = models.BooleanField(null=True)

    class Meta:
        managed = True
        db_table = 'post_rating'
'''


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    # additional attributes
    userid = models.AutoField(primary_key=True)
    usercity = models.TextField(blank=True, null=True, default= "N/A" )
    profpic = models.ImageField(upload_to='profile_images', blank=True)

    class Meta:
        managed = True
        db_table = 'user_profile'


class Post(models.Model):
    # id of the post
    postid = models.AutoField(primary_key=True)
    # title of each post
    title = models.TextField(blank=True)
    # text body of the post
    text = models.TextField(blank=True)
    # image a user can upload with the post
    image = models.ImageField(upload_to='post_images', blank=True)
    # the user posting the post
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING) //BACKUP
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date of the post
    date = models.DateTimeField(default=timezone.now())

    class Meta:
        managed = True
        db_table = 'post'


class FavoriteComics(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    comicid = models.IntegerField(null=True)

    class Meta:
        managed = True
        db_table = 'fav_comic'


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'following'
