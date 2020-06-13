from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        'tasks': request.session["tasks"]
    })


def add(request):
    # if the form is valid, this is how we get data form the form
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect('/tasks')
        else:  # we send back the existing data if it does not work
            return render(request, "tasks/add.html", {
                'form': form
            })

    return render(request, "tasks/add.html", {
        'form': NewTaskForm()
    })
