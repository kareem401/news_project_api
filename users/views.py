from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy("login")
	template_name = "signup.html"

	def form_valid(self, form):

		form.save()

		username = self.request.POST["username"]
		password = self.request.POST["password"]

		user = authenticate(
				username = form.cleaned_data["username"],
				password = form.cleaned_data["password"],

		)
		login(self.request, user)
		return HttpresponseRedirect(reverse("article_list"))