# paper_service/models.py

from django.db import models


class Paper(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('reviewing', 'Reviewing'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='papers/')
    conference_id = models.IntegerField()  # 只存储会议的ID
    author_ids = models.JSONField()  # 存储一个包含作者用户ID的列表
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='submitted')


class Review(models.Model):
    paper_id = models.IntegerField()  # 只存储论文的ID
    reviewer_id = models.IntegerField()  # 只存储审稿人的用户ID
    score = models.IntegerField()
    comment = models.TextField()
    decision = models.CharField(max_length=50)  # 如 'accept', 'reject'
