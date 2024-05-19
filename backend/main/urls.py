from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("speed/", views.speed, name="speed"),
	path("order/", views.order, name="order"),
	path("location/", views.location, name="location"),
	path("storage/", views.storage, name="storage"),
	path("manuals/<slug:manual_slug>/", views.manuals, name="manuals"),

	path("post/<int:post_id>/", views.show_post, name='post'),
]
