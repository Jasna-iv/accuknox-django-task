from django.http import HttpResponse
from django.db import transaction
from .models import SampleRecord
 
import threading
 
 
def signal_demo(request):
 
    print("Main Thread:", threading.get_ident())
 
    try:
 
        with transaction.atomic():
 
            print("Saving object...")
 
            SampleRecord.objects.create(
                title="Signal Demo Entry"
            )
 
            print("Object saved successfully")
 
            # Question 3
            raise Exception("Rollback validation")
 
    except Exception:
 
        print("Database transaction rolled back")
 
    return HttpResponse("Check terminal output")