from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from ..models import User


class SeeAdminsView(PermissionRequiredMixin, ListView):
    permission_required = 'tinyapp.view_user'
    template_name = 'admin.html'
    model = User
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')

        return context

    def get_queryset(self):
        current_user_id = self.request.user.id

        if (current_user_id is None or not self.request.user.has_perm('tinyapp.view_user')
        ):
            return None

        return User.objects.all()
