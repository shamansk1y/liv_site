# from account.models import Favorite
# from cart.cart import Cart
from .forms import SubscriptionForm, ContactUsForm
from .models import Slider, Contacts, About


def get_common_context():
    return {
        'slider': Slider.objects.filter(is_visible=True),
        'contacts': Contacts.objects.get(id=1),
        'subscription': SubscriptionForm(),
        'contact_us': ContactUsForm(),
        'about': About.objects.get(id=1),
        # 'last_products': Product.objects.order_by('-created')[:8],
        # 'products': Product.objects.filter(available=True),
        # 'recommended_products': RecommendedProduct.objects.all()[:8],
        # 'category': Category.objects.filter(parent=None),
        # 'manufacturer': Manufacturer.objects.all(),
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