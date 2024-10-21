from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import MessageForm
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def home(request):
    services=Services.objects.all()[:4] 
    header=Headerinfo.objects.get()
    about=AboutUs.objects.get()
    whychooseus=WhyChooseUs.objects.all()
    teams=Team.objects.all()
    testimonials=Testimonial.objects.all()
    brands=Brands.objects.all()
    clients=OurClients.objects.all()
    
       
    context={'services': services, 'header':header, 
             'about':about, 'whychooseus':whychooseus,
             'teams':teams, 'testimonials':testimonials, 'brands':brands, 
             'clients':clients}
    return render(request, 'index.html', context )




def about(request):
    missionandvision=MissionAndVision.objects.get()
    brands=Brands.objects.all()
    about=AboutUs.objects.get()
    corevalues=CoreValues.objects.all()
    if corevalues.count()%2==0:#checks if the values are even
        ind=int(corevalues.count()/2)
        first_div=corevalues[:ind] #assigns first halve value to new list
        
        second_div=corevalues[ind:] #assigns second halve value to new list
       
    else:
        ind=int((corevalues.count()/2) + 1)
        first_div=corevalues[:ind]
        
        second_div=corevalues[ind:]
      
                
        

        
        
        
   
    
    
    context={'about':about, 'missionandvision':missionandvision, 
             'brands':brands, 'first_div':first_div, 'second_div':second_div}
    
    return render(request, 'about.html', context)


def service(request):
    services=Services.objects.all()
    context={'services':services}
    return render(request, 'services.html', context)

def service_detail(request, pk):
    service=Services.objects.get(id=pk)
    services=Services.objects.all()
    context={"service":service, "services":services}
    return render(request, 'service_details.html', context)

def contact(request):
 
    
    contact_us=ContactUsPage.objects.last()
    context={"contact_us":contact_us}
    return render(request, 'contact.html',context)

def messages(request):
    if request.method=="POST":
        try: 
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')
            print(name, email, phone, message)
        
            message=Messages(name=name, email=email, phone=phone, comment=message)
            message.save();
            messages.success(request, "Message Submitted")
            return HttpResponseRedirect(reverse("contact"))
        except:
            # messages.error(request, "Failed to send message")
            return HttpResponseRedirect(reverse("contact"))
        
    return redirect('contact')
        




def download(request):
        document = get_object_or_404(MyCV)
        try:
            response = HttpResponse(document.book, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{document.book.name}"'
            return response 
        except ValueError:
            messages.info(request, 'Document not found')
            return HttpResponseRedirect(reverse("home"))
        

