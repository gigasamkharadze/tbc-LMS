from django.contrib import admin
from academic_portal.models import Lecturer, Student, Course, Faculty, Assignment, Attendance
# Register your models here.


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth', 'courses_display')
    search_fields = ('first_name', 'last_name', 'email')

    @staticmethod
    def courses_display(obj):
        return ', '.join([course.title for course in obj.courses.all()])
    courses_display.short_description = 'Courses'


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth', 'faculty', 'year_of_study', 'courses_display')
    search_fields = ('first_name', 'last_name', 'email')

    @staticmethod
    def courses_display(obj):
        return ', '.join([course.title for course in obj.courses.all()])
    courses_display.short_description = 'Courses'


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'description', 'syllabus')
    search_fields = ('code', 'title')


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'courses_display')
    search_fields = ('name',)

    @staticmethod
    def courses_display(obj):
        return ', '.join([course.title for course in obj.courses.all()])
    courses_display.short_description = 'Courses'


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'course')
    search_fields = ('title', 'description')


admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Attendance)