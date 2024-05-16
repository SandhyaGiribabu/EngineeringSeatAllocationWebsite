from django.shortcuts import redirect, render, HttpResponse
from .models import candidate,rank
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    return render(request, 'contact.html')

def registration(request):
    return render(request, 'registration.html')

def choice(request):
    return render(request, 'choice.html')

def seat(request):
    return render(request, 'seat.html')

def apply(request):
     
    return render(request, 'apply.html')

def apply2(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        aadhar = request.POST.get('aadhar')
        address = request.POST.get('address')
        parentname1 = request.POST.get('parentname1')
        category = request.POST.get('category')

        # Create a new candidate object
        new_candidate = candidate(
            name=name,
            email=email,
            phone=phone,
            aadhar=aadhar,
            address=address,
            parentname1=parentname1,
            category=category
        )

        # Save the candidate object to the database
        new_candidate.save()

        # Redirect to a success page or any other page
        return render(request, 'apply2.html')
    return render(request, 'apply2.html')

def success(request):
    if request.method == 'POST':
        # Extract data from the POST request
        data = {
            'dob': request.POST.get('dob'),
            'total_12th': request.POST.get('total_12th'),
            'maths': request.POST.get('maths'),
            'physics': request.POST.get('physics'),
            'chemistry': request.POST.get('chemistry'),
            'cutoff': request.POST.get('cutoff'),
            'name': request.POST.get('name')
        }

        # Check if all required fields are present
        if all(data.values()):
            # Create a new rank object associated with the candidate
            new_rank = rank(**data)
            new_rank.save()
            return render(request, 'success.html', {
                'random_no': new_rank.random_no,
                'candidate_rank': new_rank.Rank
            })
        else:
            # If any required field is missing, re-render the success page with an error message
            return render(request, 'apply2.html', {'error': 'All fields are required.'})

    else:
        # Fetch the rank object associated with the candidate
        name = request.GET.get('name')
        if name:
            try:
                rank_obj = rank.objects.get(name=name)
                return render(request, 'success.html', {
                    'random_no': rank_obj.random_no,
                    'candidate_rank': rank_obj.Rank
                })
            except rank.DoesNotExist:
                return render(request, 'success.html', {'error': 'Rank not found.'})
        else:
            return render(request, 'success.html')
        """return render(request, 'success.html')"""
"""
if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        aadhar = request.POST.get('aadhar')
        address = request.POST.get('address')
        parentname1 = request.POST.get('parentname1')
        category = request.POST.get('category')

        # Create a new candidate object
        new_candidate = candidate(
            name=name,
            email=email,
            phone=phone,
            aadhar=aadhar,
            address=address,
            parentname1=parentname1,
            category=category
        )

        # Save the candidate object to the database
        new_candidate.save()

        # Redirect to a success page or any other page
        return render(request, 'apply2.html')"""