from django.conf.urls import url
from album import views

urlpatterns =[
url(r'^$',views.first_view, name='first_view'),
	url(r'^category/$', views.category, name='category-list'),
	url(r'^category/(?P<category_id>[0-9]+)/detail/$', views.category_detail, name='category-detail'), 

	url(r'^photo/$', views.PhotoListView.as_view(), name='photo-list'),
	url(r'^photo/(?P<pk>[0-9]+)/detail/$', views.PhotoDetailView.as_view(), name='photo-detail'),

	
	url(r'^photo/(?P<pk>[0-9]+)/update/$', views.PhotoUpdate.as_view(), name='photo-update'),

	url(r'^photo/(?P<pk>[0-9]+)/delete/$', views.PhotoDelete.as_view(), name='photo-delete'),

#para crear
	url(r'^photo/create/$', views.PhotoCreate.as_view(), name='photo-create'),
	

#category
	url(r'^category/(?P<pk>[0-9]+)/update/$', views.CategoryUpdate.as_view(), name='category-update'),

	url(r'^category/(?P<pk>[0-9]+)/delete/$', views.CategoryDelete.as_view(), name='category-delete'),
	
	url(r'^category/create/$', views.CategoryCreate.as_view(), name='category-create'),
	]