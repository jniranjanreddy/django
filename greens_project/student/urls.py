from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index), 
    path('laptops/',views.laptops),
    path('mobiles/',views.mobiles),
    path('check_db_connection/',views.check_db_connection),

]