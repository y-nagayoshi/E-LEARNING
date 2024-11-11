from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'mine/',
        views.ManageCourseListView.as_view(),
        name='manage_course_list'
    ),
    path(
        'create/',
        views.CourseCreateView.as_view(),
        name='course_create'
    ),
    path(
        '<pk>/edit/',
        views.CourseUpdateView.as_view(),
        name='course_edit'
    ),
    path(
        '<pk>/delete/',
        views.CourseDeleteView.as_view(),
        name='course_delete'
    ),
    path(
      'module/<int:module_id>/content/<module_name>/create/',
      views.ContentCreateUpdateView.as_view(),
      name='module_content_create'  
    ),
    path(
        'module/<int:module_id>/content/<module_name>/<id>',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_update'
    ),
    path(
        'content/<int:id>/delete/',
        views.ContentDeleteView.as_view(),
        name='module_content_delete'
    ),
    path(
        'module/<int:module_id>',
        views.ModuleContentListView.as_view(),
        name='module_content_list'
    )
]