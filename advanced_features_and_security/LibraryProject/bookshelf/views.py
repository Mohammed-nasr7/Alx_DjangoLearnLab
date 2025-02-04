from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Book, CustomUser
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'Error creating account. Please check the details and try again.')
    else:
        form = UserCreationForm()  # Create an empty form for GET request

    # Ensure the 'register.html' template is rendered and the form is passed
    return render(request, 'bookshelf/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'bookshelf/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'bookshelf/logout.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

def list_books(request):
    #Modify views to avoid SQL injection and ensure safe handling of user input
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle form data here (e.g., save to database)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            message = form.cleaned_data['message']
            # Optionally, redirect to a success page or another action
            return render(request, 'example_success.html', {'name': name})
    else:
        form = ExampleForm()

    return render(request, 'example_form.html', {'form': form})



