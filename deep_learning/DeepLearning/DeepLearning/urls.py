from django.urls import path
from MyModel.views import ImageProcessingView, StatisticsView

urlpatterns = [
    path('', ImageProcessingView.as_view(), name='image_upload'),
    path('istatistikler/', StatisticsView.as_view(), name='statistics'),
]
