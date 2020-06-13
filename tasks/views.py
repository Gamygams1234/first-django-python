from django.shortcuts import render
from django import forms

# Create your views here.
tasks = ['foo', 'bar', 'baz']


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # adding some functionality with a serverside and client side check
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=15)


def index(request):

    return render(request, "tasks/index.html", {
        'tasks': tasks
    })


def add(request):
    # if the form is valid, this is how we get data form the form
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:  # we send back the existing data if it does not work
            return render(request, "tasks/add.html", {
                'form': form
            })

    return render(request, "tasks/add.html", {
        'form': NewTaskForm()
    })
