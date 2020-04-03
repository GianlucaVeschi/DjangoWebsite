from django.contrib import admin
from personal.models import Question

# Register your models here.

#Tell Django a new table named "Question" has been created and it should be visible in the Admin panel.
admin.site.register(Question) 