from django.db import models

class Task(models.Model):
    # many to one
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        default=1
    )
    # many to many
    assigned_to = models.ManyToManyField(
        'Employee',
        related_name='tasks'
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# one to one
class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )
    # one to one
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name='details'
    )
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
    
# many to one
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    
# many to many
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)