from django.contrib import admin

# Register your models here.
from main.models import Project, ProjectImage, Skill, SkillImage, WorkExperience, WorkPic, Education

admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Skill)
admin.site.register(SkillImage)
admin.site.register(WorkExperience)
admin.site.register(WorkPic)
admin.site.register(Education)
