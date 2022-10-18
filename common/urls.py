from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "common"

urlpatterns = [
    path('', home, name='home'),
    # path('about_us', instructions, name="instructions"),
    # path('contact', contact, name="contact"),
    # path('listeningtips',listeningtips, name="listeningtips"),
    # path('album', AlbumListView.as_view(), name='albums'),
    # path('album/<slug:slug>', AlbumDetailView.as_view(), name='album'),
    # path('genres', GenreListView.as_view(), name='genres'),
    # path('affirmations/<song_id>', affirmations, name='affirmations'),
    # path('genres/<int:pk>', SongsByGenreListView.as_view(), name='songs-by-genre'),
    # path('songs/', include([
    #     path('make-favorite', favoriteunfavorite, name='song-favorite'),
    #     path('upload', SongUploadView.as_view(), name='upload'),
    #     path('<slug:audio_id>', SongDetailsView.as_view(), name='upload-details'),

    ])),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
