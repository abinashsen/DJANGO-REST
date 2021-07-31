from django.db import models


class StudentsModel(models.Model):
    roll_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    date_of_birth = models.DateField()
    flo_marks = models.IntegerField()
    sle_marks = models.IntegerField()
    tls_marks = models.IntegerField()
    mth_marks = models.IntegerField()
    gsc_marks = models.IntegerField()
    ssc_marks = models.IntegerField()
    total_marks = models.IntegerField()

    class Meta:
        db_table = 'students'
