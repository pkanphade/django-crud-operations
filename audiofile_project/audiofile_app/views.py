from django.shortcuts import render, redirect
from django.shortcuts import Http404
from .forms import AudioBookForm
from .models import AudioBook

# Create your views here.


def audio_book_list(request):
    context = {'audio_book_list': AudioBook.objects.all()}
    return render(request, 'audiofile_app/audio_book_list.html', context)


def audio_book_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AudioBookForm()
        else:
            audio_book = AudioBook.objects.get(pk=id)
            form = AudioBookForm(instance=audio_book)
        return render(request, 'audiofile_app/audio_book_form.html', {'form': form})
    else:
        if id == 0:
            form = AudioBookForm(request.POST)
        else:
            audio_book = AudioBook.objects.get(pk=id)
            form = AudioBookForm(request.POST, instance=audio_book)

        if form.is_valid():
            form.save()
        return redirect('/audioBook/list')


def audio_book_detail(request, audio_book_id):
    try:
        audio_book = AudioBook.objects.get(pk=audio_book_id)
    except AudioBook.DoesNotExist:
        raise Http404("Audio Book does not exist")
    return render(request, 'audiofile_app/audio_book_detail.html', {'audio_book': audio_book})


def audio_book_delete(request, audio_book_id):
    audio_book = AudioBook.objects.get(pk=audio_book_id)
    audio_book.delete()
    return redirect('/audiofile_app/list')
