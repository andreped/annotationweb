from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from . import views

app_name = 'annotationweb'
urlpatterns = [
    path('', views.index, name='index'),
    path('datasets/', views.datasets, name='datasets'),
    path('add-image-sequence/<int:subject_id>/', views.add_image_sequence, name='add_image_sequence'),
    path('add-key-frames/<int:image_sequence_id>/', views.add_key_frames, name='add_key_frames'),
    path('show_frame/<int:image_sequence_id>/<int:frame_nr>/', views.show_frame, name='show_frame'),
    path('new-dataset/', views.new_dataset, name='new_dataset'),
    path('delete-dataset/<int:dataset_id>/', views.delete_dataset, name='delete_dataset'),
    path('dataset-details/<int:dataset_id>/', views.dataset_details, name='dataset_details'),
    path('new-subject/<int:dataset_id>/', views.new_subject, name='new_subject'),
    path('delete-subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('show-image/<int:image_id>/', views.show_image, name='show_image'),
    path('new-task/', views.new_task, name='new_task'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('reset-filters/<int:task_id>/', views.reset_filters, name='reset_filters'),
    path('new-label/', views.new_label, name='new_label'),
    path('task-description/<int:task_id>/', views.task_description, name='task_description'),
    path('export/<int:task_id>/', views.export, name='export'),
    path('export-options/<int:task_id>/<int:exporter_index>/', views.export_options, name='export_options'),
    path('import/<int:dataset_id>/', views.import_data, name='import'),
    path('import-options/<int:dataset_id>/<int:importer_index>/', views.import_options, name='import_options'),
    path('annotate/<int:task_id>/', views.annotate_next_image, name='annotate'),
    path('annotate/<int:task_id>/image/<int:image_id>/', views.annotate_image, name='annotate'),

    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('classification/', include('classification.urls')),
    path('segmentation/', include('segmentation.urls')),
    path('boundingbox/', include('boundingbox.urls')),
    path('landmark/', include('landmark.urls')),
    path('cardiac/', include('cardiac.urls')),
    path('cardiac_landmark/', include('cardiac_landmark.urls')),
    path('spline-segmentation/', include('spline_segmentation.urls'))
]

# This is for making statics in a development environment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
