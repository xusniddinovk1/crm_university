from rest_framework.permissions import BasePermission


class IsAdminOrStaff(BasePermission):  # [Only Staff user and Admin]
    def has_permission(self, request, view):
        # [User is authenticated and admin or staff user]
        return request.user and request.user.is_authenticated and (request.user.is_admin or request.user.is_staff)


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_teacher


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_student


class IsTeacherOfGroup(BasePermission):
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated and request.user.is_teacher):
            return False

        group_id = request.data.get('group') or request.query_params.get('group')
        if group_id:
            return request.user.teacher_profile.get_teacher.filter(id=group_id).exists()
        return True


class IsAdminOrStaffOrStudentOrTeacher(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
                user and user.is_authenticated and (
                user.is_staff or
                getattr(user, 'is_student', False) or
                getattr(user, 'is_teacher', False)
        )
        )


class IsTeacherOrStudent(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
                user and user.is_authenticated and (
                getattr(user, 'is_teacher', False) or
                getattr(user, 'is_student', False)
        )
        )
