from django.urls import path, include

urlpatterns = [
    path('/todos', include('apps.todos.urls')),
    path('/users', include('apps.users.urls')),
    path('/performers', include('apps.performers.urls')),
    path('/auth', include('apps.auth_.urls'))
]
