"""GiftLand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Product import views as Product_views
from Admin import views as Admin_views
from user import views as user_views
from ProductInfo import views as Product_view
from UserManagement import views as userman_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', Product_views.Show_Product),
    path('addproduct/', Product_views.ProductAdd),
    path('addcategory/', Product_views.CategoryAdd),
    path('addreview/', Product_views.ReviewAdd),
    path('addcart/', Product_views.CartAdd),
    path('manage/', Admin_views.Show_Admin),
    path('adda/', Admin_views.AdminAdd),
    path('user', user_views.customer),
    path('adduser/', user_views.useradd),
    path('addorder/', user_views.orderadd),
    path('addpayment/', user_views.paymentadd),
    path('adddelivery/', user_views.addDelivery),
    path('signup/', userman_views.Registerpage),
    path('profile/', userman_views.CreateProfile),
    path('profileview/', userman_views.ViewProfile),
    path('', Product_view.ShowProducts,name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('<int:product_id>',Product_view.ProductDetails),
    path('cart/',Product_view.ViewCart, name='cart'),
    path('updatecart/<int:product_id>', Product_view.AddtoCart, name='update-cart'),
    path('deletefromcart/<int:product_id>', Product_view.RemovefromCart, name='delete-from-cart'),
    path('orderproduct/<int:product_id>', Product_view.CreateOrder, name='order-product'),
    path('orders/', Product_view.UserOrder),
    path('payment/<int:product_id>',Product_view.Payment, name='payment'),
    path('review/<int:product_id>',Product_view.ProductReview, name='review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
