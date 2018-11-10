from django.contrib import admin
from .models import Restaurant, Review, Dish, RestaurantReview, DishReview
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(RestaurantReview)
admin.site.register(DishReview)
