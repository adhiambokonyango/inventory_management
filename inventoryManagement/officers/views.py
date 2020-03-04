import csv, io
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created. Log in as {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'officers/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'officers/profile.html')


"""
@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    # template = "contact_upload.html"
    prompt = {
        'order': 'Order of the CSV should be username, email, password1, password2'
    }
    if request.method == "GET":
        return render(request, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Contact.objects.update_or_create(
            username=column[0],
            email=column[1],
            password1=column[2],
            password2=column[3],
        )
    context = {}
    return render(request, 'officers/contact_upload.html', context)
"""
