from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path, include


# from shop.views import landing

from shop.views import home
from .views import *

#
urlpatterns = [
    path('', home, name='home'),
    path('', landing, name='landing'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('catalog/', catalog, name='catalog'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('statii/', stati, name='statii'),
    path('post/', show_post, name='post'),
    path('zamer/', ZamerView.as_view(), name='zamer'),
    path('onas/', nas, name='onas')
    # path('contact/success/', SuccessView.as_view(), name='success'),






]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

