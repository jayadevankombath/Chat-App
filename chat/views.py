from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from chat.models import Thread
User = get_user_model()

@login_required
def message_page(request):
    threads = Thread.objects.by_user(user = request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    users = User.objects.all()
    context = {
        'Threads':threads,
        'users':users
    }
    return render(request, 'messages.html', context)

# Add User to Chat List
def addUserToChat(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        second_person = User.objects.get(id = userid)
        if Thread.objects.filter(first_person = request.user, second_person = second_person ).exists() or Thread.objects.filter(first_person = second_person, second_person =request.user).exists():
            return redirect("/chat")
        else:
            Thread.objects.create(first_person = request.user, second_person = second_person)
    return redirect("/chat")
