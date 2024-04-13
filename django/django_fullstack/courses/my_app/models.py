from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self,postdata):
        errors={}
        if len(postdata['name'])<=5:
            errors['name']="Course name should be more than 5 characters"
        if len(postdata['desc'])<=15:
            errors['desc']="Course description should be more than 15 characters"
        return errors

class Description(models.Model):
    def __str__(self):
        return self.desc_content
    desc_content=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=CourseManager()

class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=CourseManager()

def course_info():
    return Course.objects.all()

def add_course_from_form(request):
    desc=Description.objects.create(desc_content=request.POST['desc'])
    return Course.objects.create(name=request.POST['name'], description=desc)

def specific_course_info(id):
    return Course.objects.get(id=id)

def delete_selected_course(id):
    course=Course.objects.get(id=id)
    course.delete()
    

