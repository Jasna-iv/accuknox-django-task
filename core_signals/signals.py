from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SampleRecord
 
import threading
import time
 
 
@receiver(post_save, sender=SampleRecord)
def verify_signal_behavior(sender, instance, created, **kwargs):
 
    print("\nSignal Execution Started")
 
    # Question 1
    print("Checking synchronous behavior...")
 
    time.sleep(5)
 
    # Question 2
    print("Current Signal Thread:", threading.get_ident())
 
    print("Signal Execution Completed\n")