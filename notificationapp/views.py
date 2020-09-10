from django.shortcuts import render
from notificationapp.models import Notification

def notification_view(request):
    notifications = Notification.objects.filter(receiver=request.user)
    noti_count = 0
    new_notifications = []
    for notify in notifications:
        if notify.notification_flag == False:
            noti_count += 1
            new_notifications.append(notify.msg_content.tweet)
            notify.notification_flag = True
            notify.save()
    return render(request, 'notification.html', {"new_notifications": new_notifications, "notification_count": noti_count})

def count_notification_view(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(reciever=request.user)
        noti_count = 0
        for notification in notifications:
            if notification.notification_flag == False:
                noti_count += 1

    else:
                noti_count = 0

    return noti_count