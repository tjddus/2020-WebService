from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('loadProducts', views.loadProducts.as_view()),
    path('loadProduct/<int:productId>', views.loadProduct.as_view()),
#     path('deleteProduct/<int:productId>', views.DetailProduct.as_view()),
    path('createTester/<int:productId>', views.createTester),
    path('deleteTester/<int:productId>', views.deleteTester),
    path('loadTesters/<int:productId>', views.loadTesters),
    path('createComment/<int:productId>', views.createComment.as_view()),
    path('deleteComment/<int:productId>', views.deleteComment),
    path('loadComments/<int:productId>', views.loadComments.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
