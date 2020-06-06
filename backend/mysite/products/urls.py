from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('loadProducts', views.loadProducts.as_view()),
    path('productDetail/<int:pk>', views.DetailProduct.as_view()),
    path('createTester/<int:productId>', views.createTester.as_view()),
    path('deleteTester/<int:productId>', views.deleteTester.as_view()),
    path('loadTester/<int:productId>', views.loadTester.as_view()),
    path('createComment/<int:productId>', views.createComment.as_view()),
    path('deleteComment/<int:productId>', views.deleteComment.as_view()),
    path('loadComment/<int:productId>', views.loadComment.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
