from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.url = self.name.lower()
        self.url = self.url.replace(" ", "_")
        self.url = self.url.replace(".", "_")
        self.url = self.url.replace(",", "_")
        self.url = self.url.replace("?", "")
        self.url = self.url.replace("!", "")
        self.url = self.url.replace("+", "plus")
        self.url = self.url.replace("-", "minus")
        self.url = self.url.replace("(", "lparen")
        self.url = self.url.replace(")", "rparen")
        self.url = self.url.replace("#", "hashtag")
        return super().save(*args, **kwargs)
