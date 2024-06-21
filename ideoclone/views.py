from django.shortcuts import render
from openai import OpenAI
from.models import Ideogram

# Create your views here.
def home(request):
    api_key= ''
    client= OpenAI(api_key= api_key)

    
    api_key = "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"
    image_url=''
    if request.method=="POST":  
        prompt=request.POST.get('prompt')
        client = OpenAI(api_key=api_key)
        response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )

        image_url = response.data[0].url
    return render(request, 'home.html',{'image':image_url})