from django.conf.urls.defaults import *
from openPLM.plmapp.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^home/', display_home_page),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/$', display_object),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/attributes/$', display_object),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/lifecycle/$', display_object_lifecycle),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/revisions/$', display_object_revisions),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/history/$', display_object_history),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/BOM-child/$', display_object_child),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/BOM-child/edit/$', edit_children),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/parents/$', display_object_parents),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/doc-cad/$', display_object_doc_cad),
    (r'^object/([^/]+)/([^/]+)/([^/]+)/modify/$', modify_object),
    (r'^object/create/$', create_object),

	# In order to take into account the css file
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : 'media/'})
)
