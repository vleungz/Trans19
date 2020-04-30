from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Patient, Location
from .forms import LocationForm, PatientForm, PatientFormSet


def index(request):
    context = {"index": "active"}
    return render(request, 'trans19/index.html', context)


def locations(request):
    latest_location_list = Location.objects.order_by('location_name')[:20]
    context = {'latest_location_list': latest_location_list, "location": "active"}
    return render(request, 'trans19/locations.html', context)


def patients(request):
    latest_patient_list = Patient.objects.order_by('case_number')[:20]
    context = {'latest_patient_list': latest_patient_list, "patient": "active"}
    return render(request, 'trans19/patients.html', context)


def detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'trans19/detail.html', {'patient': patient})


def location_new(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            return redirect('trans19:locations')
    else:
        form = LocationForm()
    return render(request, 'trans19/addLocation.html', {'form': form})


def location_edit(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            return redirect('trans19:locations')
    else:
        form = LocationForm(instance=location)
    return render(request, 'trans19/addLocation.html', {'form': form})


class LocationDelete(DeleteView):
    model = Location
    template_name = 'trans19/deleteLocation.html'
    success_url = reverse_lazy('trans19:locations')


class PatientCreate(CreateView):
    model = Patient
    template_name = 'trans19/addPatient.html'
    form_class = PatientForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(PatientCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['visits'] = PatientFormSet(self.request.POST)
        else:
            data['visits'] = PatientFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        visits = context['visits']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if visits.is_valid():
                visits.instance = self.object
                visits.save()
        return super(PatientCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('trans19:patients')


class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'trans19/addPatient.html'
    form_class = PatientForm

    def get_context_data(self, **kwargs):
        data = super(PatientUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['visits'] = PatientFormSet(self.request.POST, instance=self.object)
        else:
            data['visits'] = PatientFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        visits = context['visits']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if visits.is_valid():
                visits.instance = self.object
                visits.save()
        return super(PatientUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('trans19:patients')


class PatientDelete(DeleteView):
    model = Patient
    template_name = 'trans19/deletePatient.html'
    success_url = reverse_lazy('trans19:patients')