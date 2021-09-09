from votapp.forms import PersonalinfoForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')    
def personal_info(request):
    if request.method == 'POST':
        profile_form = PersonalinfoForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('index')
    else:
        profile_form = PersonalinfoForm(instance=request.user)
    return render(request, 'personal_info.html',{ "profile_form": profile_form})

@login_required(login_url='/accounts/login/')
def class_list(request):
    all_classes = classes.objects.all()
    search_term = ''
    if 'name' in request.GET:
        all_classes = all_classes.order_by('description')

    if 'date' in request.GET:
        all_classes = all_classes.order_by('pub_date')


    if 'search' in request.GET:
        search_term = request.GET['search']
        all_classes = all_classes.filter(text__icontains=search_term)

    paginator = Paginator(all_polls, 6)
    page = request.GET.get('page')
    polls = paginator.get_page(page)
    get_dict_copy = request.GET.copy()
    context = {
        'polls': polls,
        'search_term': search_term,
    }
    return render(request, 'poll_list.html', context)