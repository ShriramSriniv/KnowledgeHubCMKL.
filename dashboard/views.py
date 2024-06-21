from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tools, Training_video

# Base view for the dashboard
def base(request):
    return render(request, 'dashboard/base.html')

# Home Page View Configuration
@login_required(login_url='login')
def home(request):
    return render(request, 'dashboard/home.html')

# Knowledge Page View Configuration
@login_required(login_url='login')
def knowledge(request):
    return render(request, 'dashboard/knowledge/knowledge.html')

# Courses Page Views Configurations
@login_required(login_url='login')
def courses(request):
    return render(request, 'dashboard/courses/courses.html')

@login_required(login_url='login')
def unreal(request):
    training_videos = Training_video.objects.all()
    context = {
        'training_videos': training_videos,
    }
    return render(request, 'dashboard/courses/unreal.html', context)

@login_required(login_url='login')
def photoshop(request):
    training_videos = Training_video.objects.all()
    context = {
        'training_videos': training_videos,
    }
    return render(request, 'dashboard/courses/photoshop.html', context)

# Tools Page Views Configurations
@login_required(login_url='login')
def tools(request):
    return render(request, 'dashboard/tools/tools.html')

@login_required(login_url='login')
def content1(request):
    return render(request, 'dashboard/tools/content1.html')

@login_required(login_url='login')
def AI_tools(request):
    return render(request, 'dashboard/tools/AI_digital_tools.html')

# View for item1
def item1(request):
    tools = Tools.objects.all()
    context = {
        'tools': tools,
    }
    return render(request, 'dashboard/tools/item1.html', context)



# views.py in your main app
## this views are for the notifications when the user uploads new items in the database

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification


from .models import Notification
@login_required
@login_required
def notifications_view(request):
    notifications = request.user.notifications.all().order_by('-created_at')
    return render(request, 'dashboard/notifications.html', {'notifications': notifications})

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications')
