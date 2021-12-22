from django.db import models

# Create your models here.


# migrations are entirely derived from your models file,
# and are essentially a history that Django can roll through
# to update your database schema to match your current models.


# We can generate our database tables based on the definition of this module,
# we gonna have table called Product
# in that table we are gonna have column called title
# and the type of that column is gonna be varchar(255)

# Promotion - Product (many-to-many relationship)
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # Django will create reverse relationship with Product
    # product_set = ...(product_set by default) check Product class


class Collection(models.Model):
    title = models.CharField(max_length=255)
    # dependency with product
    # '+' means we DONT CARE ABOUT THE REVERSE RELATIONSHIP
    # THIS TELLS DJANGO TO NOT CREATE THE REVERSE RELATIONSHIP
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')

# our first model class


class Product(models.Model):
    # Each model has a number of class variables,
    # each of which represents a database field in the model.
    # here we define the fields of the product:

    # DJANGO creates id field for every model/class/entity/model class AUTO.
    # EVERY MODEL CLASS WILL HAVE ID FIELD WHICH IS GOING TO BE PRIMARY KEY.

    # WHat if we dont want an id field ?
    # what if we need sku field for primay key in this Model/Entity/Class/NAI DOBRE MAI -> TABLE ?
    # S TOZI RED PRODUCT TABLE SHTE IMA SKU KATO PRIMARY KEY
    # PRIMARY KEYYY - sku field/ NOT ID field
    # sku = models.CharField(max_length=10, primary_key=True)
    # with this Django will not create an ID field and make it the primary key

    title = models.CharField(max_length=255)
    # title now is an instance of the CharField class.
    # title now is a field.
    slug = models.SlugField()
    description = models.TextField()
    # FloatField has rounding issues.

    # !ALWAYS! For storing monetary value we use DecimalField.

    # Monetary value - is the amount that would be paid in cash for an asset or
    # service if it were to be sold to a third party

    # Generally, decimals exist in Python to solve the precision issues of floats.
    # let's say the maximum price we support in this system will be 9999.99
    # the args here are required for this field.
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    # auto_now means everytime we update a Product object
    # Django automatically sotres the current datetime in this field
    # check docs - https://docs.djangoproject.com/en/4.0/ref/models/fields/#datetimefield
    last_update = models.DateTimeField(auto_now=True)

    # We are done with the definition of the Product class

    # if we del a collection, we don't delete all products in the collection - PROTECT
    # ONE_TO _ MANY RELATIONSHIP
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    # Django will create the reverse relationship in the Promotion class
    # related_name='products,  Django will use this name in the Promotion class instead of product_set
    # IF YOU USE IT USE IT EVERYWHERE !
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    # Constants
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    # constant - FIXED LIST OF VALUES, should not mess with it
    MEMBERSHIP_CHOICES = [
        # The first element in each tuple is the actual value to be set on the model,
        # and the second element is the human-readable name
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    # max_length is good, so an attack could not happen and hacker plugin code in it ?
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    # we use choice option for possible value for the field
    # SOMETIMES WE NEED TO LIMIT THE LIST OF VALUES THAT CAN BE STORED IN A FIELD
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    # Django automatically create the reverse relationship with Address
    # so we don't need to define here field for reverse relationship: address = .....
    # check address class


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

    placed_at = models.DateTimeField(auto_now_add=True)

    # If we accidentally deleted a customer, we don't end up deleting orders,
    # IN FACT WE SHOULD NEVER DELETE ORDERS FROM OUR DATABASE
    # BECAUSE OUR THESE ORDERS REPRESENT OUR SALES, NEVER DELETED!
    # ONE_TO_MANY RELATIONSHIP
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

# How to implement one-to-one and one-to-many relationship between two models (Address class/Customer class)


class Address(models.Model):
    # ONE-TO-ONE relationship (CUSTOMER-ADDRESS) between two models
    # Let's assume every Customer could have ONE Address
    # And EACH Address should belong to ONE Customer

    # let's add several fields
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # US zip code
    zip = models.CharField(max_length=5, default="43701")

    # A DATABASE relationship has two ends a PARENT and a CHILD
    # The parent should exist before we can store the child
    # IN CUSTOMER-ADDRESS one-to-one relationship
    # THE CUSTOMER(class/entity) IS THE PARENT
    # Because we say 'The Customer has an ADDRESS'
    # So, the Customer should exist before we can create an Address.

    # Here in the CHILD class/entity we need to specify the Parent
    # So here we add Relationship field
    # first arg - the type of the parent model
    # second ard - on_delete - we specify a delete behavior
    # what should happen when we delete a customer
    # if we set it to models.CASCADE -> when we delete a customer
    # the associated address will ALSO be deleted -> CASCADE behavior
    # third ard - primary key
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#onetoonefield
    # If we don't set primary_key, Django will create another field called id
    # so every address will have an id, which means we will end up with ONE-TO-MANY relationship
    # between Customer and addresses, because we can have many addresses with the same Customer
    # but if we make customer a primary_key we can have only one address for each customer
    # Because primary_keys don't allow duplicate values.
    # customer = models.OneToOneField(
    #     Customer, on_delete=models.CASCADE, primary_key=True)

    # ONE-TO-MANY relationship (CUSTOMER-ADDRESS) between two models
    # Let's assume every Customer could have MULTIPLE Address
    # We use ForeignKey, we tell Django that customer is a foreign key in this table
    # We remove primary_key=True, because we want to have multiple addresses for the same customer
    # so we want to allow duplicate values in this column
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
