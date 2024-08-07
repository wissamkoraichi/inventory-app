from rest_framework.permissions import BasePermission

class IsCompanyEmail(BasePermission):
    def has_permission(self, request, view):
        return request.user.email.endswith('@afamconcept.com')
