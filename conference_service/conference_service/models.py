# conference_service/models.py

from django.db import models


class Conference(models.Model):
    acronym = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    submission_deadline = models.DateTimeField()
    review_deadline = models.DateTimeField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50)  # 如 'preparing', 'submitting', 'reviewing', 'finalizing', 'finished'
    chair_id = models.IntegerField()  # 只存储chair的用户ID


class PCMemberInvitation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    conference_id = models.IntegerField()  # 只存储会议的ID
    pc_member_id = models.IntegerField()  # 只存储被邀请的PC member的用户ID
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')  # 如 'pending', 'accepted', 'rejected'
