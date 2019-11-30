from django.urls import path
from . import views

urlpatterns = [
    path('s_list/', views.SolutionList.as_view(), name="s_list"),
    path('s_create/', views.SolutionCreate.as_view(), name="s_create"),
    path('s_detail/<int:pk>', views.SolutionDetail.as_view(), name='s_detail'),
    path('s_update/<int:pk>', views.SolutionUpdate.as_view(), name='s_update'),
    path('s_delete/<int:pk>', views.SolutionDelete.as_view(), name='s_delete'),
]