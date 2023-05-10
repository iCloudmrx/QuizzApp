from django.urls import path
from .views import home, signup, ready_to_test, test, check_test, new_question, new_test


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('<int:test_id>/ready-to-test/', ready_to_test, name='ready_to_test'),
    path('<int:test_id>/test/', test, name='test'),
    path('<int:check_test_id>/check-test/', check_test, name='check_test'),
    path('new-test/', new_test, name='new_test'),
    path('<int:test_id>/new-question/', new_question, name='new_question'),
]
