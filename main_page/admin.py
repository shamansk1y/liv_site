from django.contrib import admin
from main_page.models import Slider, ContactUs, Contacts, Subscription, About, Baner


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_editable = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'tab', 'tab_url']
    list_display = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'tab', 'tab_url']
    list_display_links = None


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    model = Contacts
    list_editable = ['address', 'phone', 'email','fb_url', 'youtube_url', 'in_url']
    list_display = ['address', 'phone','email', 'fb_url', 'youtube_url', 'in_url']
    list_display_links = None


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_editable = ['email', 'is_processed']
    list_display = ['email', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_editable = ['name', 'email', 'subject', 'message', 'is_processed']
    list_display = ['name', 'email', 'subject', 'message', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_editable = ['title', 'desc', 'image', 'is_visible', 'tab_name', 'cat_url']
    list_display = ['title', 'desc', 'image', 'is_visible', 'tab_name', 'cat_url']
    list_display_links = None



@admin.register(Baner)
class BanerAdmin(admin.ModelAdmin):
    model = Baner
    list_editable = ['title', 'position', 'image_3', 'h_3', 'desc_3', 'tab_3', 'tab_url_3', 'image_4', 'h_4',
                     'desc_4', 'tab_4', 'tab_url_4']
    list_display = ['title', 'position', 'image_3', 'h_3', 'desc_3', 'tab_3', 'tab_url_3', 'image_4', 'h_4',
                    'desc_4', 'tab_4', 'tab_url_4']
    list_display_links = None