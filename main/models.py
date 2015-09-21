from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.


class Project(models.Model):
    date = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class ProjectImage(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey('main.Project')
    image = models.ImageField(upload_to='project')
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class SkillImage(models.Model):
    name = models.CharField(max_length=255)
    skill = models.ForeignKey('main.Skill')
    image = ImageField(upload_to='skill')

    def __unicode__(self):
        return self.name


class WorkExperience(models.Model):
    name = models.CharField(max_length=255)
    dates = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class WorkPic(models.Model):
    name = models.CharField(max_length=255)
    job = models.ForeignKey('main.WorkExperience')
    image = models.ImageField(upload_to='workexperience')

    def __unicode__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=255)
    dates = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name