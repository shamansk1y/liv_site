# from account.models import Favorite
from cart.cart import Cart
from shop.models import Category, Product
from .forms import SubscriptionForm, ContactUsForm
from .models import Slider, Contacts, About, Baner
from shop.models import RecommendedProduct

def get_common_context():
    return {
        'slider': Slider.objects.filter(is_visible=True),
        'contacts': Contacts.objects.get(id=1),
        'subscription': SubscriptionForm(),
        'contact_us': ContactUsForm(),
        'about': About.objects.get(id=1),
        'last_products': Product.objects.order_by('-created')[:4],
        'recommended_products': RecommendedProduct.objects.all()[:4],
        'categories': Category.objects.filter(is_visible=True),
        'category_main_page': Category.objects.filter(category_main_page=True)[:4],
        'baner': Baner.objects.get(id=1),
    }


def get_page_context(request):
    # favorites_count = 0
    # if request.user.is_authenticated:
    #     favorites_count = Favorite.objects.filter(user=request.user).aggregate(count=Count('id'))['count']


    data = {
        'user_manager': request.user.groups.filter(name='manager').exists(),
        'user_auth': request.user.is_authenticated,
        # 'favorites_count': favorites_count,
    }
    context = get_common_context()
    data.update(context)
    return data