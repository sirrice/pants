from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader

from pants.home.models import *

def index(request):
    return render_to_response('index.html',
                              {'dudes' : Dude.objects.all().order_by('-pk')},
                              context_instance=RequestContext(request))

def adddude(request):
    if request.method != "POST":
        return render_to_response('adddude.html',
                                  {},
                                  context_instance=RequestContext(request))
    
    name = request.POST['name']
    passwd = request.POST['password']
    if passwd == 'blarg' and \
       len(Dude.objects.filter(name=name)) == 0:
        d = Dude(name=name)
        d.save()
    return render_to_response('adddude.html',
                              {},
                              context_instance=RequestContext(request))
    

def lookup_vote(dudeid, ip):
    dude = Dude.objects.get(pk=dudeid)
    if not dude:
        return None
    votes = Vote.objects.filter(dude=dude, ip=ip).order_by("-id")
    if len(votes) > 0: 
        return votes[0]
    return None
    

def getvote(request, dudeid):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    elif 'REMOTE_ADDR' in request.META:
        ip = request.META['REMOTE_ADDR']
    else:
        ip = "unknown"
    voteobj = lookup_vote(dudeid, ip)
    vote = (voteobj and voteobj.pants) or 0
    return render_to_response('getvote.json',
                              {'vote' : vote},
                              context_instance=RequestContext(request))    

def addvote(request):
#     if request.method != "POST":
#         return render_to_response('addvote.json',
#                                   {'status' : "err"},
#                                   context_instance=RequestContext(request))
    dudeid = request.REQUEST['dudeid']
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    elif 'REMOTE_ADDR' in request.META:
        ip = request.META['REMOTE_ADDR']
    else:
        ip = "unknown"
    votestr = request.REQUEST['vote']
    voteobj = lookup_vote(dudeid, ip)
    voteval = ((votestr == 'true') and 1 or (votestr == 'false') and -1 or 0)
    skip = False
    try:
	dudeobj = Dude.objects.get(pk=dudeid)
    except:
	skip = True

    status = "err"
    if voteobj:
        if voteobj.pants == voteval: 
            voteobj = Vote(dude=dudeobj, ip=ip, pants=0)
            voteobj.save()
            status = "clear"
        else:
            voteobj.pants = voteval
            voteobj.save()
            status = "ok"
    elif not skip:
        try:
            dudeobj = Dude.objects.get(pk=dudeid)
            voteobj = Vote(dude=dudeobj, ip=ip,
                           pants=voteval)
            voteobj.save()
            status = "ok"
        except Exception as e:
            print "fuck ", e
            pass
    return render_to_response('addvote.json',
                              {'status' : status},
                              context_instance=RequestContext(request))
    
        
    
    



def addcomment(request):
    if request.method != "POST":
        return HttpResponseRedirect('/')
    
    namestr = request.REQUEST['name']
    commentstr = request.REQUEST['comment']
    cobj = Comment(name=namestr, comment=commentstr)
    cobj.save()

    return render_to_response('addcomment.json',
                              {'status' : "ok"},
                              context_instance=RequestContext(request))


def comments(request):
    comments = Comment.objects.all().order_by("-pk")
    return render_to_response("comments.html",
                              {"comments":comments},
                              context_instance=RequestContext(request))
