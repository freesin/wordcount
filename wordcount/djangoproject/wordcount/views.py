from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') #3개 인자까지 받을 수 있음, 템플릿 언어,사전형 객체(dictionary형)

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            # add to dictionary
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()} )
