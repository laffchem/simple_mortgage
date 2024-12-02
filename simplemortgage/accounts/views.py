from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserForm, RegistrationForm, FileUploadForm
from .models import CustomUser, UserFile
from django.http import FileResponse
from urllib.parse import quote
from mortgages.models import Mortgage  # Import the Mortgage model


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("home")


@login_required
def view_account(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user_files = UserFile.objects.filter(user=user)
    return render(
        request, "accounts/profile.html", {"user": user, "user_files": user_files}
    )


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Create 3 mortgage offers for the new user
            Mortgage.objects.bulk_create(
                [
                    Mortgage(
                        user=user,
                        lender_name="Lender 1",
                        interest_rate=3.5,
                        max_amount=500000,
                        loan_type="Fixed",
                        min_down_payment=20,
                        loan_term=30,
                    ),
                    Mortgage(
                        user=user,
                        lender_name="Lender 2",
                        interest_rate=3.75,
                        max_amount=400000,
                        loan_type="Adjustable",
                        min_down_payment=15,
                        loan_term=15,
                    ),
                    Mortgage(
                        user=user,
                        lender_name="Lender 3",
                        interest_rate=4.0,
                        max_amount=300000,
                        loan_type="Fixed",
                        min_down_payment=10,
                        loan_term=20,
                    ),
                ]
            )
            return redirect("profile", user_id=request.user.id)
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile", user_id=request.user.id)
    else:
        form = CustomUserForm(instance=user)
    return render(request, "accounts/edit_user.html", {"form": form})


@login_required
def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.user = request.user
            user_file.save()
            return redirect("profile", user_id=request.user.id)
    else:
        form = FileUploadForm()
    return render(request, "accounts/upload.html", {"form": form})


@login_required
def view_pdf(request, file_id):
    user_file = get_object_or_404(UserFile, id=file_id, user=request.user)
    response = FileResponse(user_file.file.open(), content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="{quote(user_file.label)}"'
    return response
