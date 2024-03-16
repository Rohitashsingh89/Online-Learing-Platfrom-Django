from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Announcement, Assignment, Contact, Department, Material


class AnnouncementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True
        self.fields['description'].label = ''

    class Meta:
        model = Announcement
        fields = ['description']
        widgets = {
            'description': FroalaEditor(),
        }


class AssignmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.label = ''
        self.fields['file'].required = False

    class Meta:
        model = Assignment
        fields = ('title', 'description', 'deadline', 'marks', 'file')
        widgets = {
            'description': FroalaEditor(),
            'title': forms.TextInput(attrs={'class': 'form-control mt-1', 'id': 'title', 'name': 'title', 'placeholder': 'Title'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control mt-1', 'id': 'deadline', 'name': 'deadline', 'type': 'datetime-local'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control mt-1', 'id': 'marks', 'name': 'marks', 'placeholder': 'Marks'}),
            'file': forms.FileInput(attrs={'class': 'form-control mt-1', 'id': 'file', 'name': 'file', 'aria-describedby': 'file', 'aria-label': 'Upload'}),
        }


class MaterialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.label = ""
        self.fields['file'].required = False

    class Meta:
        model = Material
        fields = ('description', 'file')
        widgets = {
            'description': FroalaEditor(),
            'file': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'name': 'file', 'aria-describedby': 'file', 'aria-label': 'Upload'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

from .models import Course

class CourseForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), 
                                       empty_label='Select Department',
                                       widget=forms.Select(attrs={'class': 'form-select mt-1', 'placeholder': 'Department'}))
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.label = ''
        self.fields['code'].label = 'Course Code'
        self.fields['name'].label = 'Course Name'
        self.fields['price'].label = 'Course Price'
        self.fields['studentKey'].label = 'Student Key'
        self.fields['facultyKey'].label = 'Faculty Key'
        self.fields['image'].required = False
        self.fields['description'].required = False

    class Meta:
        model = Course
        fields = ['code', 'name', 'price', 'image', 'department', 'studentKey', 'facultyKey', 'description']
        widgets = {
            'code': forms.NumberInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Course Code'}),
            'name': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Course Name'}),
            'price': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Course Price'}),
            'studentKey': forms.NumberInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Student Key'}),
            'facultyKey': forms.NumberInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Faculty Key'}),
            'description': FroalaEditor(),
            'image': forms.FileInput(attrs={'class': 'form-control mt-1', 'aria-describedby': 'file', 'aria-label': 'Upload'}),
        }
        

# faculty = request.user