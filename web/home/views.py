from django.shortcuts import render , redirect
from pathlib import Path
from django.conf import settings

def index(request):
    if request.method =='POST':
        action = request.POST.get('redirect')

        if action == "controls" : return redirect('controls')
        if action == "photos": return redirect('photos')
        if action == "test": return redirect('test')
    content= {}
    return render(request, "home/index.html", content)

def photos(request):
    base = Path("/srv/media")
    albums = [x.name for x in base.iterdir()]
    content = {"albums": albums}
    return render(request, "home/photos.html", content)

def into_album(request, album_name):
    album_path = Path(settings.MEDIA_ROOT)/ album_name
    Images = [f"/media/{album_name}/{img.name}" for img in album_path.iterdir()]

    content = {
        "album_name" : album_name,
        "images" : Images,
    }
    return render(request, "home/into_album.html", content)

def controls(request):
    return render(request, "home/controls.html")

def test(request):
    return render(request, "home/test.html")