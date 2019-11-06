from django.shortcuts import render,reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView
from django.contrib.auth import get_user_model
from .forms import UserProfileForm
from .models import Link,Vote,UserProfile

class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "links/user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    template_name = "links/edit_profile.html"
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]
    def get_success_url(self):
        return reverse("profile", kwargs={'slug':self.request.user})