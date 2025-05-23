from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import HomeView, BookTableView, MenuView, AboutView, FeedbackView, Login, Signup_View
# from Base_App.views import * 

# urlpatterns = [
#     path('', HomeView, name='home'),
#     path('book_table/', BookTableView, name='book_table'),
#     path('menu/', MenuView, name='menu'),
#     path('about/', AboutView, name='about'),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='home'),
    path('book_table/', BookTableView, name='book_table'),
    path('menu/', MenuView, name='menu'),
    path('about/', AboutView, name='about'),
    path('feedback/', FeedbackView, name='feedback'),
    path('login/',Login,name="login"),
    path('signup/', Signup_View, name='signup'),
    path('accounts/',include("allauth.urls"))

]


if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
