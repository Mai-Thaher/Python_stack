from django.db import models
import datetime

class ShowManager(models.Manager):
    def show_validator(self, postdata):
        print(postdata)
        errors={}
        if len( postdata["title"] ) < 2:
            errors["title"]="TV_show title should be at least 2 characters"
        if len( postdata['network'] ) < 3:
            errors['network']="The network should be at least 3 characters"
        if len( postdata['desc'] ) < 10:
            errors['desc']="The description should be at least 10 characters"
        today = datetime.datetime.timestamp(datetime.datetime.now()) #change date to integer
        release_date = datetime.datetime.strptime(postdata['date'], '%Y-%m-%d') # shange the date from string to date
        if datetime.datetime.timestamp(release_date) >= today:
            errors['date']="The date should be in the past"
        return errors


class TV_show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=ShowManager()
    
def create_show():
    d1 = datetime.date(2013, 9, 17)
    # d=d1.strftime("%B %d %y")
    TV_show.objects.create(title = "Brooklyn Nine-Nine", network = "NBC", release_date = d1)

# def update():
#     c=TV_show.objects.get(id=1)
#     c.title="Stranger Things"
#     c.save()

def display_shows():
    return TV_show.objects.all()

def delete(id):
    show=TV_show.objects.get(id=id)
    show.delete()

def show_info(id):
    return TV_show.objects.get(id=id)
    
def new_show(request):
    show=TV_show()
    show.title=request.POST['title']
    show.network=request.POST['network']
    show.release_date=request.POST['date']
    show.description=request.POST['desc']
    show.save()
    return show
    # return TV_show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'],description=request.POST['desc'])
    
def update(request,id):
    show=TV_show.objects.get(id=id)
    show.title=request.POST['title']
    show.network=request.POST['network']
    show.release_date=request.POST['date']
    show.description=request.POST['desc']
    show.save()

