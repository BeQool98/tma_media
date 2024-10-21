from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.register(Headerinfo)
admin.site.register(AboutUs)
admin.site.register(WhyChooseUs)
admin.site.register(OurClients)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Brands)
admin.site.register(Messages)
admin.site.register(CallBack)
admin.site.register(MissionAndVision)
admin.site.register(ContactUsPage)
admin.site.register(Brochure)
admin.site.register(CoreValues)
admin.site.register(Subscribers)



class ServicesAdmin(SummernoteModelAdmin):
    summernote_fields=('long_description')
    
admin.site.register(Services, ServicesAdmin)

