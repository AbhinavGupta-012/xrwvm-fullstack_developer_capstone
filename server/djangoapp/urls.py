# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # path for registration
    path('registration', views.registration, name='registration'),

    # path for login/logout
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),

    # path to get cars
    path('get_cars', views.get_cars, name='getcars'),

    # paths to get dealers and dealer details
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),

    # path to get specific dealer details and reviews
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),

    # path to add a review
    path('add_review', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
