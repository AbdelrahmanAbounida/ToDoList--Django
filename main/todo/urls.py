from django.urls import path

from .views import TaskDetail, ToDoList, CreateTask,UpdateTask,DeleteTask,MyLogin,MainApp,MyLogout,about,donate,contact,MyRegister



urlpatterns = [
	path('',ToDoList.as_view(),name='home'),
	path('app/',MainApp.as_view(),name="app"),
	path('detail/<int:pk>',TaskDetail.as_view(),name='detail'),
	path('create/',CreateTask.as_view(),name='create'),
	path('update/<int:pk>',UpdateTask.as_view(),name='update'),
	path('delete/<int:pk>',DeleteTask.as_view(),name='delete'),
	path('login/',MyLogin.as_view(),name='login'),
	path('logout/', MyLogout.as_view(),name='logout'),
	path('About.html/', about,name='about'),
	path('Donate.html/', donate,name='donate'),
	path('Contact.html/', contact,name='contact'),
	path('regiter/', MyRegister.as_view(),name='register'),
	
]
