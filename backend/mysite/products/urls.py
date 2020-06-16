from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('loadAllProducts', views.loadAllProducts.as_view()),
    path('loadPublishedProducts', views.loadPublishedProducts.as_view()),
    path('loadNotPublishedProducts', views.loadNotPublishedProducts.as_view()),
    path('loadEndProducts', views.loadEndProducts.as_view()),
    path('loadAllTesters', views.loadAllTesters.as_view()),
    path('loadProduct/<int:productId>', views.loadProduct.as_view()),
    path('deleteProduct/<int:productId>', views.deleteProduct.as_view()),
    path('editProduct/<int:productId>', views.editProduct.as_view()),
    path('createTester/<int:productId>', views.createTester.as_view()),
    path('deleteTester/<int:productId>', views.deleteTesters.as_view()),
    path('loadTesters/<int:productId>', views.loadTesters.as_view()),
    path('createComment/<int:productId>', views.createComment.as_view()),
    path('deleteComment/<int:commentId>', views.deleteComment.as_view()),
    path('updateComment/<int:commentId>', views.updateComment.as_view()),
    path('loadComments/<int:productId>', views.loadComments.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)