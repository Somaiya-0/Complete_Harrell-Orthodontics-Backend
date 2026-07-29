from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPracticeStaff(BasePermission):
    """Grants access to the hospital-staff dashboard APIs. Superusers
    (developer/super-admin) always pass; regular staff must have
    role='staff' on their account. Referring providers never pass."""

    def has_permission(self, request, view):
        user = request.user
        if not (user and user.is_authenticated):
            return False
        return user.is_superuser or user.role == user.Role.STAFF


class IsPracticeStaffOrReadOnly(BasePermission):
    """Public can read (GET/HEAD/OPTIONS); only practice staff can write.
    Used on content endpoints so the public site keeps working with no
    auth while the staff dashboard manages the same data."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if not (user and user.is_authenticated):
            return False
        return user.is_superuser or user.role == user.Role.STAFF
