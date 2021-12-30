from django.conf.urls.static import static

from todoprojects import settings
from . import views
from django.urls import path

app_name = 'todoapps'
urlpatterns = [
    path('cbvhome/', views.TaskListview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdelete'),

    path('', views.todo, name='todo'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

    # path('details', views.details, name='details'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
