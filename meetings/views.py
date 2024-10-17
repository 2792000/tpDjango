from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import *
from .forms import MeetingForm,RoomForm
# Create your views here.
def meetings_list_view(request):

    meetings = Meeting.objects.all()  # Get all meetings
    return render(request, 'meetings.html', {'meetings': meetings, })
def room_list_view(request):

    rooms = Room.objects.all()  # Get all rooms
    return render(request, 'rooms.html', {'rooms': rooms, })

# Get meeting by id
def meeting_detail_view(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)  # Get the meeting by id or return 404
    return render(request, 'meeting_detail_view.html', {'meeting': meeting})

# Get room by id
def room_detail_view(request, room_id):
    room = get_object_or_404(Room, id=room_id)  # Get the room by id or return 404
    return render(request, 'room_detail_view.html', {'room': room})

def meeting_create_view(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new meeting
            return redirect('all')  # Redirect to the meetings list
    else:
        form = MeetingForm()
    return render(request, 'new.html', {'form': form})

def room_create_view(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new meeting
            return redirect('allrooms')  # Redirect to the meetings list
    else:
        form = RoomForm()
    return render(request, 'newroom.html', {'form': form})


def delete_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id) # Get the meeting b ID
    if request.method == "POST":
        meeting.delete() # Delete the meeting
        return redirect('/meetings/all') # Redirect to themeetings list view after deletion
    return render(request, 'confirm_delete.html', {'meeting': meeting})
    # Render confirmation page