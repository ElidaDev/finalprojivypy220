from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
import calendar

# Create your views here.
def firstView(request):
    return HttpResponse("Something I want to be printed other than Django installed successfully")

def showEmployees(request):
    employees = Employee.objects.all
    
    return render(request, "index.html",{"employees": employees})
def showSchedules(request):
    schedules = Shift.objects.all
    return render(request, "schedules.html",{"shifts":schedules})
def AddShift(request):
    form = ShiftForm()
    if request.method == "POST":
        form = ShiftForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("schedule")
    return render(request, "addShift.html",{"form":form})
    
def AddShiftEvent(request):
    shiftId = request.GET.get("shift")
    form=ShiftEventForm()
    if request.method == "POST":
        form = ShiftEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("schedule")
    else:
        form = ShiftEventForm()
        if shiftId:
            form.fields["shift"].initial = shiftId
    return render(request, "addShiftEvent.html", {"form": form})
    
def EditShift(request, id):
    shift = get_object_or_404(Shift,id = id)
    form = ShiftForm(instance=shift)
    if request.method == "POST":
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect("schedule")
    return render(request, "editShift.html",{"form":form})
    
    
def EditShiftEvent(request, id):
    shift = get_object_or_404(Event,id = id)
    form = ShiftEventForm(instance=shift)
    if request.method == "POST":
        form = ShiftEventForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect("schedule")
    return render(request, "editShiftEvent.html",{"form":form})
    
def calendarView(request):
    today = timezone.localdate()

    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))

    selectedEmployee = request.GET.get("employee")

    if month < 1:
        month = 12
        year -= 1

    if month > 12:
        month = 1
        year += 1

    employees = Employee.objects.all()
    shifts = Shift.objects.filter(
        startDateTime__year=year,
        startDateTime__month=month
    ).order_by("employee", "startDateTime")

    firstShifts = []
    alreadyAdded = set()

    for shift in shifts:
        key = (shift.employee_id, shift.startDateTime.date())

        if key not in alreadyAdded:
            firstShifts.append(shift)
            alreadyAdded.add(key)

    firstShifts.sort(key=lambda shift: shift.startDateTime)

    shifts = firstShifts
    events = Event.objects.filter(
        startDateTime__year=year,
        startDateTime__month=month
    )

    if selectedEmployee:
        shifts = shifts.filter(employee_id=selectedEmployee).order_by("employee", "startDateTime")
        events = events.filter(shift__employee_id=selectedEmployee)

    calendarObject = calendar.Calendar(firstweekday=6)
    weeks = calendarObject.monthdayscalendar(year, month)

    if month == 1:
        previousMonth = 12
        previousYear = year - 1
    else:
        previousMonth = month - 1
        previousYear = year

    if month == 12:
        nextMonth = 1
        nextYear = year + 1
    else:
        nextMonth = month + 1
        nextYear = year

    return render(
        request,
        "calendar.html",
        {
            "weeks": weeks,
            "year": year,
            "month": month,
            "monthName": calendar.month_name[month],

            "previousMonth": previousMonth,
            "previousYear": previousYear,

            "nextMonth": nextMonth,
            "nextYear": nextYear,

            "employees": employees,
            "selectedEmployee": selectedEmployee,
            "shifts": shifts,
            "events": events
        }
    )
    
def deleteShiftEvent(request, id):
    shiftEvent = get_object_or_404(Event, id=id)

    if request.method == "POST":
        shiftEvent.delete()
        return redirect("schedule")

    return render(request, "deleteEvent.html", {"event": shiftEvent})

def deleteShift(request, id):
    shift = get_object_or_404(Shift, id=id)

    if request.method == "POST":
        shift.delete()
        return redirect("schedule")

    return render(request, "deleteShift.html", {"shift": shift})

def dayView(request, shiftId):

    shift = Shift.objects.get(id=shiftId)

    employee = shift.employee
    date = shift.startDateTime.date()

    shifts = Shift.objects.filter(
        employee=employee,
        startDateTime__date=date
    ).order_by('startDateTime')

    events = Event.objects.filter(
        shift=shift
    ).order_by('startDateTime')

    return render(request, 'dayView.html', {
        'employee': employee,
        'date': date,
        'shifts': shifts,
        'events': events
    })