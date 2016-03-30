# Create your views here.
from django.shortcuts import render
from django.conf import settings

import requests
import json
import urllib.request

from .forms import SubmitEmbed
from .serializer import EmbedSerializer
from django.http import HttpResponse


def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
            #r = request.get('http://api.locu.com/v1_0/venue/search/?api_key=6d45e2e191a4509d222a619f5823f7bc909b76b8')
            json = r.json()
            serializer = EmbedSerializer(data=json)
            if serializer.is_valid():
                embed = serializer.save()
                return render(request, 'embeds.html', {'embed': embed})
    else:
        form = SubmitEmbed()

    return render(request, 'index.html', {'form': form})


def fun(request):
      

    urlData = "https://api.locu.com/v1_0/venue/search/?api_key=6d45e2e191a4509d222a619f5823f7bc909b76b8"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    json.loads(data.decode(encoding))
    


    #return render(request)
    return HttpResponse(json.dumps(data.decode(encoding)))
    #return(json.data.decode(encoding))