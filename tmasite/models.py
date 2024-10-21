from django.db import models

# Create your models here.

class Headerinfo(models.Model):
    top_small=models.CharField(max_length=100, null=True, blank=True)
    bold_description=models.CharField(max_length=50, null=True, blank=True)
    down_description=models.CharField(max_length=200, null=True, blank=True)
    try:
        def __str__(self):
            return self.top_small    
    except:
        pass
    
    
class AboutUs(models.Model):
    top_header=models.CharField(max_length=100, null=True, blank=True)
    bold_description=models.CharField(max_length=200, null=True, blank=True)
    down_description=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='media', null=True, blank=True, default='media/author_img_default.png')
    ceo_name=models.CharField(max_length=20, null=True, blank=True)
    ceo_position=models.CharField(max_length=20, null=True, blank=True)
    
    try:
        def __str__(self):
            return self.top_header    
    except:
        pass
    

class Services(models.Model):
    icon=models.CharField(max_length=100, null=True, blank=True)
    short_title=models.CharField(max_length=50, null=True, blank=True)
    long_title=models.CharField(max_length=150, null=True, blank=True)
    short_desc=models.CharField(max_length=400, null=True, blank=True)
    long_description=models.TextField()
    image=models.ImageField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    try:
        def __str__(self):
            return self.short_title    
    except:
        pass
    
    
class WhyChooseUs(models.Model):
    tab_name=models.CharField(max_length=100, null=True, blank=True)
    title=models.CharField(max_length=100, null=True, blank=True)
    down_description=models.TextField(null=True, blank=True)
    image=image=models.ImageField(null=True, blank=True)
    
    try:
        def __str__(self):
            return self.title    
    except:
        pass
    
class OurClients(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    try:
        def __str__(self):
            return self.name    
    except:
        pass
    
    
    
class Team(models.Model):
    image=models.ImageField(null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    position=models.CharField(max_length=50, null=True, blank=True)
    
    try:
        def __str__(self):
            return self.name    
    except:
        pass
    

class Testimonial(models.Model):
    image=models.ImageField(default='testi_avatar02._default.png', null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    position=models.CharField(max_length=50, null=True, blank=True)
    comment=models.TextField(null=True, blank=True)
    
    try:
        def __str__(self):
            return self.name    
    except:
        pass
    
class Brands(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    
    try:
        def __str__(self):
            return self.name    
    except:
        pass

#This is the contact us form    

class Messages(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)
    phone=models.CharField(max_length=50, null=True, blank=True)
    comment=models.TextField(null=True, blank=True)

    try:
        def __str__(self):
            return self.name    
    except:
        pass

class CallBack(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)
    phone=models.CharField(max_length=50, null=True, blank=True)

    try:
        def __str__(self):
            return self.name    
    except:
        pass

class MissionAndVision(models.Model):
    mission_title=models.CharField(max_length=100, null=True, blank=True)
    mission_body=models.TextField(null=True, blank=True)
    vision_title=models.CharField(max_length=100, null=True, blank=True)
    vision_body=models.TextField(null=True, blank=True)
    try:
        def __str__(self):
            return self.mission_title    
    except:
        pass

class CoreValues(models.Model):
    value_name=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    
    try:
        def __str__(self):
            return self.value_name    
    except:
        pass

class ContactUsPage(models.Model):
    big_header=models.CharField(max_length=100, null=True, blank=True)
    text=models.TextField(null=True, blank=True)
    address=models.CharField(max_length=100, null=True, blank=True)
    phone=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    
    try:
        def __str__(self):
            return self.big_header    
    except:
        pass


class Subscribers(models.Model):
    email=models.CharField(max_length=200, null=True, blank=True)
    
    


class Brochure(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    book = models.FileField(upload_to='media',null=True,blank=True, help_text='Upload your brochure Here')
    
    
    if name is not None:
        def __str__(self):
            return self.name
    
    
    

