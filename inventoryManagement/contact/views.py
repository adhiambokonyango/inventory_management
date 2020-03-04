from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
import csv, io
# Create your views here.
from .models import Contact
from .forms import ContactForm


def contact(request):
    template = "contact.html"
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template = "contact_upload.html"
    prompt = {
        'order': 'order of csv is firstName, secondName, PFnumber, Ministry, Department, email'
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Contact.objects.update_or_create(
            firstName=column[0],
            secondName=column[1],
            PFnumber=column[2],
            Ministry=column[3],
            Department=column[4],
            email=column[5]
        )
    context = {}
    return render(request, template, context)
