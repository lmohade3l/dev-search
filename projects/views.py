from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    page = 'projects'
    return render(request , 'projects/projects.html' , {'page':page , 'projects':projectsList} )


def project(request, pk):
    project_obj = None
    for p in projectsList:
        if p['id']==pk :
            project_obj = p

    return render(request , 'projects/single-project.html', {'project' : project_obj} )
