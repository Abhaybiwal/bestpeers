from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, TemplateView, DetailView, FormView, View
from django.views.decorators.http import require_POST
from django.http import HttpResponse,JsonResponse
from .models import *
from .forms import ContactForm
from math import ceil
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm,CustomPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, CustomTokenObtainPairSerializer,SignupSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication




CustomUser = get_user_model()


class IndexView(APIView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'allProds'
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticated]

    # permission_classes=[IsAuthenticated]
      
    def get(self, request, *args, **kwargs):
        
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return redirect(reverse('shop:login'))

        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])
        context['allProds'] = allProds
        return context

class AboutView(TemplateView):
    template_name = 'shop/about.html'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'shop/password_reset_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('shop:password_reset_done')


class CustomPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'shop/password_change_form.html'
    success_url = reverse_lazy('shop:password_change_done')


# class CustomPasswordResetView(auth_views.PasswordResetView):
#     template_name = 'shop/password_reset_form.html'
#     email_template_name = 'registration/password_reset_email.html'
#     success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'shop/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'shop/password_reset_confirm.html'
    success_url = reverse_lazy('shop:password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'shop/password_reset_complete.html'


class ContactView(FormView):
    template_name = 'shop/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('thanks') 

    def form_valid(self, form):
        # Save the data to the Contact model
        contact = Contact(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            desc=form.cleaned_data['message']
        )
        contact.save()
        return redirect('thanks/')


class TrackerView(TemplateView):
    template_name = 'shop/tracker.html'


class SearchView(View):
    def get(self, request):
        return HttpResponse("we are at search")


class ProductView(DetailView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'product'

    def get_object(self):
        myid = self.kwargs.get("myid")
        return get_object_or_404(Product, id=myid)
    
    def post(self, request, *args, **kwargs):

        product = self.get_object()
        return redirect('add_to_cart', myid=product.id)

class CheckoutView(TemplateView):
    template_name = 'shop/checkout.html'
    
    
@csrf_protect
@login_required
def submit_data(request):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        myid=int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=myid)
        user = request.user
        cart_item ,created= Cart.objects.get_or_create(user=user, product=product)
        cart_item.quantity = quantity
        cart_item.save()
        return JsonResponse({'message': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@login_required
@require_POST
def update_cart(request):
    try:
        action = request.POST.get('action')
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'success': False, 'message': 'Product ID not provided.'})

        cart_item = get_object_or_404(Cart, product__id=product_id, user=request.user)

        if action == 'delete':
            cart_item.delete()
            return JsonResponse({'success': True, 'message': 'Item deleted successfully.'})

        elif action == 'update':
            quantity = request.POST.get('quantity')
            if not quantity or int(quantity) < 1:
                return JsonResponse({'success': False, 'message': 'Invalid quantity.'})
            cart_item.quantity = int(quantity)
            cart_item.save()
            return JsonResponse({'success': True, 'message': 'Quantity updated successfully.'})

        return JsonResponse({'success': False, 'message': 'Invalid action.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})



class ThanksView(TemplateView):
    template_name = 'shop/thanks.html'
    

class CartItems(View):
    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        return render(request, "shop/cartitems.html", {'cart_items': cart_items})


# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/shop')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'shop/signup.html', {'form': form})

class LoginView(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        return render(request, 'shop/login.html')

    def post(self, request):
        try:
            data = request.POST
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.validated_data.get('username')
                password = serializer.validated_data['password']

                # Authentication
                user = authenticate(username=username, password=password)

                if user is None:
                    return render(request, 'shop/login.html', {'error': 'Invalid credentials.'})
                
                login(request, user)
                
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                # Pass tokens to the template
                context = {
                    'access_token': str(access_token),
                    'refresh_token': str(refresh),
                }

                return render(request,'shop/login.html',context)
            return render(request, 'shop/login.html', {'errors': serializer.errors})
        
        except Exception as e:
            return render(request, 'shop/login.html', {'error': str(e), 'details': str(e)})



class SignupView(APIView):
    def get(self, request):
        return render(request, 'shop/signup.html')

    def post(self, request):
        try:
            data = request.POST
            serializer = SignupSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()

                # Generate tokens
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                # Save tokens in session or cookies
                request.session['access_token'] = str(access_token)
                request.session['refresh_token'] = str(refresh)

                return redirect(reverse('shop:index'))

            return render(request, 'shop/signup.html', {'errors': serializer.errors})
        
        except Exception as e:
            return render(request, 'shop/signup.html', {'error': 'Something went wrong.', 'details': str(e)})
        


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# class LogoutView(generics.GenericAPIView):
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        

class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()

            # Clear session tokens if stored
            if 'access_token' in request.session:
                del request.session['access_token']
            if 'refresh_token' in request.session:
                del request.session['refresh_token']

            # Redirect to login page
            return redirect('login')
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": str(e)})


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'This is a protected view'}
        return Response(content)
    
class ShowApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message': 'Hello, world!'})