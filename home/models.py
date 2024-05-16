from django.db import models,transaction
import random
import string

class candidate(models.Model):
    CATEGORY_CHOICES = [
        (1, 'General'),
        (2, 'OBC'),
        (3, 'SC'),
        (4, 'ST'),
        (5, 'PwD'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)  # Adjust max_length based on typical phone number lengths
    aadhar = models.CharField(max_length=12, default=None)
    address = models.CharField(max_length=255)
    parentname1 = models.CharField(max_length=100, null=True, blank=True, default=None)
    category = models.IntegerField(choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.id}-{self.email}-{self.phone}-{self.aadhar}-{self.address}-{self.parentname1}-{self.category}"

class rank(models.Model):
    name = models.CharField(max_length=100,default=None)
    dob = models.DateField()
    total_12th = models.IntegerField()
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField(null=True, blank=True, default=None)
    cutoff = models.FloatField()
    Rank = models.IntegerField(null=True, blank=True)
    random_no = models.CharField(max_length= 5, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Assign a unique rank based on the cutoff
            self.assign_initial_rank()
        
        if not self.random_no:
            self.random_no = self.generate_unique_random_no()

        with transaction.atomic():
            super().save(*args, **kwargs)
            self.reassign_all_ranks()

    def assign_initial_rank(self):
        # Count ranks with higher or equal cutoffs
        higher_ranks = rank.objects.filter(cutoff__gte=self.cutoff).count()
        self.Rank = higher_ranks + 1

    def generate_unique_random_no(self):
        while True:
            random_no = ''.join(random.choices(string.digits, k=5))
            if not rank.objects.filter(random_no=random_no).exists():
                return random_no

    def reassign_all_ranks(self):
        # Reassign ranks to maintain order and uniqueness
        ranks = rank.objects.all().order_by('-cutoff', '-maths', '-physics', '-chemistry', '-total_12th', 'dob', '-random_no')
        Rank = 1
        for rank_obj in ranks:
            if rank_obj.Rank != Rank:
                rank_obj.Rank = Rank
                rank_obj.save(update_fields=['Rank'])
            Rank += 1

    def __str__(self):
        return f"Candidate: {self.name}\tRandom Number: {self.random_no},M:{self.maths},P:{self.physics},C:{self.chemistry},Total:{self.total_12th},DOB:{self.dob}, Rank: {self.Rank}\tCutoff: {self.cutoff}"