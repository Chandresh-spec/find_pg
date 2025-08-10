from django.contrib import admin
from .models import PG,PG_Owner,AboutPg,PG_Image,DeatilPage,PGRules
# Register your models here.

class PGAdmin(admin.ModelAdmin):
    class Meta:
        model=PG_Owner
        fields=('owner_name','contact_number','email')





class PG_OwnerAdmin(admin.ModelAdmin):
    class Meta:
        model=PG
        fields=('pg_name','address')
    



class AboutpgAdmin(admin.ModelAdmin):
    class Meta:
        model=AboutPg
        fields=('occupancy','gender','price','facilities')

class PGImageAdmin(admin.ModelAdmin):
    class Meta:
        model=PG_Image
        fields=('imgs')


class PGImageAdmin(admin.ModelAdmin):
    class Meta:
        model=PG_Image
        fields=('imgs')



class DetailPageAdmin(admin.ModelAdmin):
    class Meta:
        model= DeatilPage
        fields=('deposit_amount','notice_period','parking','operating_since')


class PGRulesAdmin(admin.ModelAdmin):
    class meta:
        model=PGRules
        fileds=('gate_closing','visitor_entry','smoking','drinking','party')


admin.site.register(PG_Owner,PG_OwnerAdmin)
admin.site.register(AboutPg,AboutpgAdmin)
admin.site.register(PG,PGAdmin)
admin.site.register(PG_Image,PGImageAdmin)
admin.site.register(DeatilPage,DetailPageAdmin)
admin.site.register(PGRules,PGRulesAdmin)




