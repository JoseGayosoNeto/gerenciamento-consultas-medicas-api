from django.urls import path

from .views import health_db_connection_check

urlpatterns = [
    path('health/', health_db_connection_check, name='health_db_conn_check'),
]
