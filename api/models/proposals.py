from django.db import models 


class Proposal(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=50)
    proposal_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "proposal"
        verbose_name_plural ="proposals"

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("Proposal_detail", kwargs={"pk": self.pk})

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.ForeignKey(Proposal,on_delete=models.CASCADE)
    github_link = models.URLField(max_length=2000)
    notes = models.TextField()
    date_started = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ="project"
        verbose_name_plural ="projects"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Project_detail", kwargs={"pk": self.pk})

