from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.http  import HttpResponse
from .forms import *
# Create your views here.
from .views import *

def index(request):
    context = {
        'categories': Category.objects.all()[:6],
        'latest_products': Product.objects.all()[:6]
    }
    return render(request, "shop.html", context)

def about_us(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "ecom/contact_us.html")
def team(request):
    return render(request, "ecom/team.html")


def cart(request):
    return(request, "cart.html")

def admin(request):
    return render(request, "admin/index.html")


class ProductUploadView(CreateView):
    form_class = ProductUploadForm
    template_name = "product/create.html"

    @method_decorator(login_required(login_url=reverse_lazy('marketplace:home')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductUploadView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super(ProductUploadView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=200)

    def form_valid(self, form):
        product = TinyTag.get(self.request.FILES['product'].file.name)
        # form.instance.audio_id = generate_key(15, 15)
        form.instance.user = self.request.user
        # form.instance.playtime = song.duration
        # form.instance.size = song.filesize
        category = []
        for a in self.request.POST.getlist('category[]'):
            try:
                category.append(int(a))
            except:
                category = category.objects.create(name=a)
                category.append(category)
        form.save()
        form.instance.artists.set(album)
        form.save()
        data = {
            'status': True,
            'message': "Successfully submitted form data.",
            'redirect': reverse_lazy('core:upload-details', kwargs={'audio_id': form.instance.audio_id})
        }
        return JsonResponse(data)


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'products/strain-detail.html'
    context_object_name = 'product'
    slug_field = 'product_id'
    slug_url_kwarg = 'product_id'



# def affirmations(request, song_id):
#     aff = Song.objects.get(audio_id=song_id).affirmations
#     return HttpResponse(aff)



class CategoryListView(ListView):
    model = Category
    template_name = 'category/index.html'
    context_object_name = 'category'

# class AffirmationsListView(ListView):
#     model = Song
#     template_name = 'genres/index.html'
#     context_object_name = 'genres'


class ProductsByCategoryListAPIView(DetailView):
    model = Category
    template_name = 'products/product-by-category.html'
    context_object_name = ''

    def get_context_data(self, **kwargs):
        context = super(ProductsByCategoryListAPIView, self).get_context_data(**kwargs)
        context['products'] = self.get_object().product_set.all
        return context


class OrderListView(ListView):
     model = Order
     template_name = 'order/index.html'
     context_object_name = 'order'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'Order/show.html'
    context_object_name = 'Order'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['order'] = self.get_object().products.all()
        return context

class TestimonialsDetailView(DetailView):
    model = Testimonials
    template_name = 'testimonials/show.html'
    context_object_name = 'testimonials'

    def get_context_data(self, **kwargs):
        context = super(TestimonialsDetailView, self).get_context_data(**kwargs)
        context['testimonials'] = self.get_object().testimonials.all()
        return context


class CartCreateView(CreateView):
    form_class = CartForm
    http_method_names = ['post']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CartCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            data = {
                'status': True,
                'message': "Please login first",
                'redirect': None
            }
            return JsonResponse(data=data)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def favoriteunfavorite(request):
    if request.method == "POST":
        if request.POST.get('decision') == 'make':
            song = Products.objects.get(id=request.POST.get('product_id'))
            if not Cart.objects.filter(user=request.user, product=product).exists():
                Cart.objects.create(user=request.user, product=product)
                data = {
                    'status': True,
                    'message': "Song marked in Favourite",
                    'redirect': None
                }
                return JsonResponse(data)
            else:
                data = {
                    'status': True,
                    'message': "Already favorite",
                    'redirect': None
                }

                return JsonResponse(data)
        else:
            product = Product.objects.get(id=request.POST.get('product_id'))
            Cart.objects.filter(user=request.user, product=product).delete()
            data = {
                'status': True,
                'message': "Product unfavorited",
                'redirect': None
            }
            return JsonResponse(data)
    else:
        data = {
            'status': False,
            'message': "Method not allowed",
            'redirect': None
        }

        return JsonResponse(data)


class UnFavoriteView(DeleteView):
    model = Cart;

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        data = {
            'status': True,
            'message': "Product unfavorited.",
            'redirect': None
        }

        return JsonResponse(data)
