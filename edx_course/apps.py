"""
edx_course Django application initialization.
"""

from django.apps import AppConfig

from edx_django_utils.plugins.constants import PluginURLs

from openedx.core.djangoapps.plugins.constants import ProjectType

class EdxCourseConfig(AppConfig):
    """
    Configuration for the edx_course Django application.
    """

    name = 'edx_course'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'edx_course',
                PluginURLs.APP_NAME: 'edx_course',
                PluginURLs.REGEX: r'^api/edx_course/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },    
    }
