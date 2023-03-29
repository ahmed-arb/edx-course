"""
edx_course Django application initialization.
"""

from django.apps import AppConfig
# from edx_django_utils.plugins.constants import (
#     ProjectType, PluginURLs
# )

class EdxCourseConfig(AppConfig):
    """
    Configuration for the edx_course Django application.
    """

    name = 'edx_course'

    # plugin_app = {

    #     # Configuration setting for Plugin URLs for this app.
    #     PluginURLs.CONFIG: {

    #         # Configure the Plugin URLs for each project type, as needed.
    #         ProjectType.LMS: {

    #             # The namespace to provide to django's urls.include.
    #             PluginURLs.NAMESPACE: 'edx_course',

    #             # The application namespace to provide to django's urls.include.
    #             # Optional; Defaults to None.
    #             PluginURLs.APP_NAME: 'edx_course',

    #             # The regex to provide to django's urls.url.
    #             # Optional; Defaults to r''.
    #             PluginURLs.REGEX: r'^api/edx_course/',

    #             PluginURLs.RELATIVE_PATH: 'urls',
    #         }
    #     },    
    # }
