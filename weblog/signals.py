from django.db.models.signals import post_save
from django.core.mail import send_mail

from .models import Blog , Notification


def notification(sender , **kwargs):
    if kwargs['created']:
        emails = Notification.objects.values_list('email',flat=True)
        msg = " Hi buddy! \n A new post has been uploaded to the blog \n https://amirgh.pythonanywhere.com/"
        for email in emails:
            send_mail('New Blog',msg ,'alighalenoei8383@gmail.com' , [email] , fail_silently=False)
            print('Send Notification successfuly')

post_save.connect(receiver=notification , sender=Blog)

