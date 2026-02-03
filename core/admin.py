from django.contrib import admin
from .models import Profile, Skill, Experience, Education, Certificate


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email', 'phone')
    fieldsets = (
        (None, {
            'fields': ('full_name', 'title', 'photo', 'about', 'location')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone')
        }),
        ('Social Media', {
            'fields': ('linkedin', 'github', 'twitter')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')
    search_fields = ('job_title', 'company', 'description')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'issue_date')