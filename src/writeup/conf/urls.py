from django.conf import settings
import oauth2_provider.views as oauth2_views
from django.urls import include, path

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    # path('authorize', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path("token", oauth2_views.TokenView.as_view(), name="token"),
    path("revoke_token", oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

urlpatterns = [
    path("o/", include(oauth2_endpoint_views)),
]

if settings.DEBUG:
    from django.contrib import admin

    urlpatterns += [
        path("admin/", admin.site.urls),
        path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    ]
