from django.shortcuts import render, HttpResponse
from .models import contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from blog.models import post


# HTML PAGES
def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'post':
       name = request.post['name']
       email = request.post['email']
       phone = request.post['phone']
       content = request.post['content']
       if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
           messages.error(request, "Please fill the form correctly")
       else:
           contact=contact(name=name, email=email, phone=phone, content=content)
           contact.save()
           messages.success(request, "Your message has been successfully sent")
    return render(request, 'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=post.objects.none()
    else:
        allPostsTitle= post.objects.filter(title__icontains=query)
        allPostsAuthor= post.objects.filter(author__icontains=query)
        allPostsContent =post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

# Authentication APIs
def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) < 10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method == "POST":
                # Get the post parameters
          loginusername = request.POST['loginusername']
          loginpassword = request.POST['loginpassword']

          user = authenticate(username=loginusername, password=loginpassword)
          if user is not None:
             login(request, user)
             messages.success(request, "Successfully Logged In")
             return redirect("home")
          else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")




def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def about(request):
    return render(request, "home/about.html")

