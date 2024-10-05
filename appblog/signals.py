from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Person
from django.core.mail import send_mail
from django.conf import settings
   
   
   
@receiver(post_save, sender=User)    
def create_person(sender, instance, created, **kwargs):
    user = instance
    if created:
        person =Person.objects.create(
            user = user,
        )
        print('person created')
        subject = 'welcome to emmanuel\'s website'
        message = 'we are glad you could make it'
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
            
        )
        
        
# @receiver(post_save, sender=User)            
# def update_person(sender, instance, created, **kwargs):
#     if created == False:
#         instance.person.save()
#         print('person updated')

@receiver(post_delete, sender=Person)    
def delete_person(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('user associated with person has been deleted')