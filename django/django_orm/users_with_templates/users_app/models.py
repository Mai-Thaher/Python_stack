from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email_address=models.CharField(max_length=255)
    age=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def new_user():
    user=User.objects.create(first_name='Dina',last_name='Rahhal', email_address='Dina_rahhal@gmail.com',age=28)

def edit_user():
    user=User.objects.get(id=3)
    user.last_name="Asaad"
    user.save()

def new_user_from_form(request):
    user=User.objects.create(first_name=request.POST['f_name'],last_name=request.POST['l_name'], email_address=request.POST['email'],age=request.POST['age'])