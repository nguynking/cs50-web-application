import secrets
import markdown2

from django.shortcuts import render
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from django import forms    
from django.urls import reverse

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Entry title", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    content = forms.CharField(label="Entry content", widget=forms.Textarea(attrs={'class': 'form-control col-md-8 col-lg-8', 'rows': 10}))
    edit = forms.BooleanField(initial="False", widget=forms.HiddenInput(), required=False)

def index(request):
    if request.method == "GET":
        return search(request)
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def title(request):
    return render(request, "encyclopedia/")

def entry(request, entry):
    markdowner = Markdown()
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, "encyclopedia/nonExistingPage.html", {
            "entryTitle": entry
        })
    return render(request, "encyclopedia/entry.html", {
        "entry": markdowner.convert(entryPage),
        "entryTitle": entry
    })

def newPage(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is None or form.cleaned_data["edit"] is True:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('entry', kwargs={'entry': title}))
            else:
                return render(request, "encyclopedia/newPage.html", {
                    "form": form,
                    "existing": True,
                    "entry": title
                })
        else:
            return render(request, "encyclopedia/newPage.html", {
                "form": form,
                "existing": False
            })
    else:
        return render(request, "encyclopedia/newPage.html", {
            "form": NewEntryForm(),
            "existing": False
        })

def search(request):
    value = request.GET.get('q', '')
    if util.get_entry(value) is not None:
        return HttpResponseRedirect(reverse('entry', kwargs={'entry': value}))
    else:
        subStringEntries = []
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                subStringEntries.append(entry)

        return render(request, "encyclopedia/index.html", {
            'entries': subStringEntries,
            'search': True,
            'value': value
        })

def edit(request, entry):
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, "encyclopedia/nonExistingPage.html", {
            "entryTitle": entry
        })
    else:
        form = NewEntryForm()
        form.fields["title"].initial = entry
        form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = entryPage
        form.fields["edit"].initial = True
        return render(request, "encyclopedia/newPage.html", {
            "form": form,
            "content": entryPage,
            "entryTitle": entry 
        })


def random(request):
    return HttpResponseRedirect(reverse('entry', kwargs={'entry': secrets.choice(util.list_entries())}))
