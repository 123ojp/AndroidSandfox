from django.db import models

# Create your models here.

class WorkerJobStatus:
    NOJOB  = 0
    NEWJOB = 1
    ALLOCATE_JOB = 2
    NO_PERMISSION = 3