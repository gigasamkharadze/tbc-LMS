from django.db import models
from django.utils.translation import gettext as _

# import choices
from academic_portal.choices import YEAR_OF_STUDY_CHOICES


# Create your models here.
class Lecturer(models.Model):
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, verbose_name=_('User'))
    courses = models.ManyToManyField('Course', verbose_name=_('Courses'), related_name='lecturers')
    email = models.EmailField(primary_key=True, verbose_name=_('Email'))
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_('Last Name'))
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Lecturer')
        verbose_name_plural = _('Lecturers')
        ordering = ['last_name', 'first_name', 'date_of_birth', 'email']
        indexes = [
            models.Index(fields=['first_name'], name='lecturer_first_name_idx'),
            models.Index(fields=['last_name'], name='lecturer_last_name_idx'),
        ]


class Student(models.Model):
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, verbose_name=_('User'), related_name='student')
    courses = models.ManyToManyField('Course', verbose_name=_('Courses'), related_name='students')
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name=_('Faculty'), related_name='students')
    email = models.EmailField(primary_key=True, verbose_name=_('Email'))
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_('Last Name'))
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'))
    year_of_study = models.PositiveSmallIntegerField(choices=YEAR_OF_STUDY_CHOICES, verbose_name=_('Year of Study'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ['last_name', 'first_name', 'date_of_birth', 'email', 'year_of_study', 'faculty']
        indexes = [
            models.Index(fields=['last_name'], name='student_last_name_idx'),
        ]


class Course(models.Model):
    code = models.CharField(max_length=10, primary_key=True, verbose_name=_('Code'))
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    syllabus = models.FileField(upload_to='syllabus/', verbose_name=_('Syllabus'))

    def __str__(self):
        return f'{self.code}'

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['code', 'title']
        indexes = [
            models.Index(fields=['title'], name='course_title_idx'),
        ]


class Faculty(models.Model):
    courses = models.ManyToManyField('Course', verbose_name=_('Courses'), related_name='faculties')
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_('Name'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')


class Assignment(models.Model):
    course = models.OneToOneField('Course', on_delete=models.CASCADE, verbose_name=_('Course'), related_name='assignments')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    due_date = models.DateTimeField(verbose_name=_('Due Date'))
    file = models.FileField(upload_to='assignments/', verbose_name=_('File'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Assignment')
        verbose_name_plural = _('Assignments')
        ordering = ['title', 'due_date']
        indexes = [
            models.Index(fields=['title'], name='assignment_title_idx'),
        ]