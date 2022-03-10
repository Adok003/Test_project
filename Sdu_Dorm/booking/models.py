from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=25, help_text="Enter your name...")
    last_name = models.CharField(max_length=25, help_text="Enter your surname...")
    mail_address = models.EmailField(max_length=30, help_text="Enter your email...")
    phone_number = models.IntegerField(help_text="Enter your phone number...")
    password = models.CharField(max_length=25)


class Block(models.Model):
    block_name = models.CharField(max_length=1)
    block_type = models.CharField(max_length=10)


class Floor(models.Model):
    floor_number = models.IntegerField()


class Room(models.Model):
    room_number = models.IntegerField()
