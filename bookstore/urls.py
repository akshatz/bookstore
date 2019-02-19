from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url (r'^store/', include('store.urls'), name='store'),
    url (r'accounts/', include('registration.backends.simple.urls')),
    url (r'^admin/', include(admin.site.urls)),
]
