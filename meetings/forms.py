from django import forms
from .models import Meeting , Room

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
        'date': forms.DateInput(attrs={"type": "date"}),
        'start': forms.TimeInput(attrs={"type": "time"}),
        'duration': forms.TextInput(attrs={"type": "number","min":"1", "max":"4"})
        }
        def clean_date(self):
            d = self.cleaned_data.get("date")
            if d < forms.date.today():
             raise forms.ValidationError("Meetings cannot be in the past")
            return d
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
        'name': forms.TextInput(attrs={"type": "text"}),
        'floor': forms.NumberInput(attrs={"type": "numbre"}),
        'room_number': forms.NumberInput(attrs={"type": "number","min":"1", "max":"100"})
        }
        