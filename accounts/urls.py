from django.urls import reverse_lazy
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.password_validation import password_validators_help_text_html as pass_help
from . import views, forms

app_name = 'accounts'
urlpatterns = [
    url(r'^register/$',
        views.register,
        name='register'),

    url(r'^register-done/$',
        views.register_done,
        name='register_done'),

    url(r'^login/$',
        auth_views.LoginView.as_view(
            template_name='accounts/login.html',
            extra_context={'title': "Login", 'submit': "Login"},
            redirect_authenticated_user=True),
        name='login'),

    # 'title' is automatically included in the context by Django here
    url(r'^logout/$',
        auth_views.LogoutView.as_view(
            template_name='accounts/success_page_login.html',
            extra_context={'message': "You have successfully logged out"}),
        name='logout'),

    url(r'^profile/$',
        views.profile,
        name='profile'),

    url(r'^change-password/$',
        views.change_password,
        name='change_password'),

    url(r'^password-reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='main/generic_form.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt',
            success_url=reverse_lazy('accounts:password_reset_done'),
            extra_context={'title': "Password Reset", 'submit': "Send Email"},),
        name='password_reset'),

    url(r'^password-reset-done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/success_page.html',
            extra_context={'title': "Password Reset Email Sent",
                           'message': "Reset password email sent successfully. "
                                      "Please check your email."}),
        name='password_reset_done'),

    url(r'^edit/$',
        views.edit,
        name='edit'),

    url(r'^activate/(?P<key>[a-f|\d]+)/$',
        views.activation,
        name='activation'),

    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='main/generic_form.html',
            form_class=forms.PasswordSet,
            success_url=reverse_lazy('accounts:password_reset_complete'),
            extra_context={'title': "Create a New Password",
                           'submit': "Reset Password",
                           'password_help_text': pass_help()},
        ),
        name='password_reset_confirm'),

    url(r'^password-reset-complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/success_page_login.html',
            extra_context={'title': "Password Reset Complete",
                           'message': "Password reset successfully. Please login."},
        ),
        name='password_reset_complete'),
]
