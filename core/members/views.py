from django.shortcuts import render, get_object_or_404
from django.utils.encoding import uri_to_iri 
from .models import Member



def members_list(request):
    members = Member.objects.filter(is_active=True)
    template = 'members/member_list.html'
    context = {
        'title': 'Members List',
        'members': members
    } 
    return render(request, template, context)

def member_detail(request, member_id):
    member = get_object_or_404(Member, member_id=uri_to_iri(member_id))
    template = 'members/member_detail.html'
    context = {
        'title': 'Member Detail',
        'member': member
    }  
    return render(request, template, context)
