from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

#Profile
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(("Email"), max_length=254)
    mobile = PhoneNumberField(("Mobile"))
    bio = models.TextField(("Bio"))
    linkedIn = models.URLField(("LinkedIn"), max_length=200)
    github = models.URLField(("Github"), max_length=200)

    def __str__(self):
        return self.name
    

#Education
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    institution = models.CharField(("Institution"), max_length=50)
    course = models.CharField(("Course Title"), max_length=50)
    start_date = models.DateField(("Start Date"), auto_now=False)
    end_date = models.DateField(("End date"), auto_now=False)
    remarks = models.TextField(("Remarks"))

    def __str__(self):
        return self.institution
    

#Work Experience
class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    institution = models.CharField(("Company"), max_length=50)
    title = models.CharField(("Title"), max_length=50)
    start_date = models.DateField(("Start Date"), auto_now=False)
    end_date = models.DateField(("End Date"), auto_now=False)
    remarks = models.TextField(("Remarks"))

    def __str__(self):
        return self.institution
    

#Interests
class Interests(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(("Name"), max_length=50)
    tags = models.CharField(("Tags"), max_length=50)

    def __str__(self):
        return self.name
    

#Skills
class Skills(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skills = models.CharField(("Skills"), max_length=50)
    proficiency = models.CharField(("Proficiency"), max_length=50)
    tags = models.CharField(("Tags"), max_length=50)

    def __str__(self):
        return self.skills
    

#Projects
class Projects(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    typeof = models.CharField(("Type"), max_length=50)
    title = models.CharField(("Title"), max_length=50)
    details = models.TextField(("Details"))

    def __str__(self):
        return self.typeof
    