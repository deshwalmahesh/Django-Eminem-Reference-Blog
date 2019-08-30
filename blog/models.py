from django.urls import reverse
from django.utils import timezone
from django.db import models

class Post(models.Model):
    author= models.ForeignKey('auth.User',max_length=25, on_delete=models.CASCADE)
    create_date=models.DateField(default=timezone.now)
    title=models.CharField(max_length=50)
    text=models.TextField()
    published_date=models.DateField(blank=True,null=True) #IT can be published later but the comments_approved is not included

    def publish(self): #to publish at a later time
        self.published_date=timezone.now()
        self.is_published=True
        self.save() #WE will try to add self.published_date.save() see if it works

    def approve_comments(self):
        return self.comments.filter(approved_comment=True) #See last line of Comment Class. Same thing

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk}) #go to a url named 'post detail' after posting the post with id given
                                                            #'post_detail' will be created later (I am making models.py first)
                                                            # See urls.py. I have created urls.py too

    def __str__(self):
        return  self.title

class Comment(models.Model):
    post=models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE) #each post connected to a Post class
    author=models.CharField(max_length=1024) #person who is commenting
    text=models.CharField(max_length=1024)
    edited_text=models.CharField(max_length=1024,blank=True,null=True)
    created_date=models.DateField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)
    edit=models.BooleanField(default=False)
    edited_on=models.DateTimeField(blank=True,null=True)

    def approve(self):
        self.approved_comment=True
        self.is_approved=True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list') #return to page which directs to url-'post_list' after commenting

    def __str__(self):
        return self.text

    def update_comment(self):
        self.edit=True
        self.edited_on=timezone.now()
        self.save()

    def approve_edit(self):
        if self.edit:
            self.text=self.edited_text
            self.save()
