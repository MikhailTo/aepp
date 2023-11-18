from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    aggregate = models.CharField(max_length=100)
    cabinet = models.CharField(max_length=100)
    location = models.ForeignKey('Location', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name + ' -> ' + self.type + ' -> ' + self.aggregate


class Location(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=False)
    division = models.ForeignKey('Division', on_delete=models.PROTECT, null=False)
    color = models.CharField(max_length=255, default='grey')
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=128)

    def __str__(self):
        return self.company_name


class Division(models.Model):
    division_name = models.CharField(max_length=128)

    def __str__(self):
        return self.division_name


class Group(models.Model):
    group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name


class Order(models.Model):
    order_number = models.IntegerField(default="")
    company = models.ForeignKey('Company', on_delete=models.PROTECT, null=False, default=0) # "ПАО Северсталь"
    division = models.ForeignKey('Division', on_delete=models.PROTECT, null=False, default=0) #"ППП ЛПЦ-1"
    issuer = models.ForeignKey('Issuer', on_delete=models.PROTECT, null=False)
    accountable_name = models.CharField(max_length=128, default="Не назначается")
    allower_name = models.CharField(max_length=128, default="оперативному персоналу")
    producer = models.ForeignKey('Member', on_delete=models.PROTECT, null=False)
    watching = models.ForeignKey('Watching', on_delete=models.PROTECT, null=False, default=0) # ""
    brigade = models.ForeignKey('Brigade', on_delete=models.PROTECT, null=False)
    errand = models.CharField(max_length=512)
    add_instrs = models.CharField(max_length=512)
    extrad_time = models.TimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    interventions = models.ForeignKey('Equipment', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.errand


class Interventions(models.Model):
    installation_name = models.CharField(max_length=255)
    disconnections = models.CharField(max_length=255)
    protections = models.CharField(max_length=255, default="Не требуется")

    def __str__(self):
        return self.installation_name + ': ' + self.disconnections


class Watching(models.Model):
    full_name = models.CharField(max_length=128)
    access_group = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name + ' ' + self.access_group + 'гр.'


class Issuer(models.Model):
    full_name = models.CharField(max_length=128)
    access_group = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name + ' ' + self.access_group + 'гр.'


class Member(models.Model):
    full_name = models.CharField(max_length=128)
    access_group = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name + ' ' + self.access_group + 'гр.'


class Brigade(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Member, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE)