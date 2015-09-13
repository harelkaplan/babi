from decimal import *

from django.utils import timezone

import factory
from . import models

from faker import Faker
import random

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)


class EmployerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Employer
    user = factory.SubFactory(UserFactory)
    is_required_to_pay_vat = True
    business_id = random.randint(1000000,10000000)
    income_tax_id = random.randint(1000000,10000000)
    phone_number = random.randint(10000000,100000000)

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Employee
    user = factory.SubFactory(UserFactory)
    employer = factory.SubFactory(EmployerFactory)
    birthday = fake.simple_profile()['birthdate']
    government_id = random.randint(10000000,100000000)

class MonthlyEmployerDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Monthly_employer_data 
    employee = factory.SubFactory(EmployeeFactory)
    created = timezone.now()
    entered_by = 'admin'
    is_approved = True
    for_year = 0
    for_month = 0
    is_required_to_pay_vat = True
    is_required_to_pay_income_tax = True
    lower_tax_threshold = Decimal(0.05)
    upper_tax_threshold = Decimal(0.1)
    income_tax_threshold = Decimal(60000)
    exact_income_tax_percentage = Decimal(0.15)

class MonthlyEmployeeDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Monthly_employee_data 
    employee = factory.SubFactory(EmployeeFactory)
    created = timezone.now()
    entered_by = 'admin'
    is_approved = True
    gross_payment = Decimal(1000)
    salary = Decimal(900)
    general_expenses = Decimal(100)
    gross_or_cost = True
    is_required_to_pay_social_security = True
    is_employer_the_main_employer = True
    gross_payment_from_others = Decimal(200)
    for_year = 0
    for_month = 0

class MonthlySystemDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Monthly_system_data 
    created = timezone.now()
    for_year = 0
    for_month = 0
    vat_percentage = Decimal(0.17)
    social_security_threshold = 70000
    lower_employee_social_security_percentage = Decimal(0.07)
    lower_employer_social_security_percentage = Decimal(0.1)
    upper_employee_social_security_percentage = Decimal(0.12)
    upper_employer_social_security_percentage = Decimal(0.14)
    maximal_sum_to_pay_social_security = 100000
    income_tax_default = Decimal(0.3)


class MyGenerators(object):
    """Functions that assist in creating factories that handle the constraints in my models' ".save()" method"""
    def __init__(self):
        super(MyGenerators, self).__init__()
    
    def stub(self):
        return True

    def generateMonthlyEmployeeDataWithFactory(self, *args, **kwargs):
        """I have to make sure a user has employer data before inserting employee data. 
        After I do that, I use the kwargs given to create the monthly data objects"""
        employeeData = kwargs.get('employeeData',{})
        employerData = kwargs.get('employerData',{})
        
        if 'employee' not in employeeData:
            return False
        
        if 'employee' not in employerData:
            employerData['employee'] = employeeData['employee']
        
        try:
            employerDataFromDb = models.Monthly_employer_data.objects.filter(employee=employeeData['employee'])[0]
        except IndexError as e:
            MonthlyEmployerDataFactory(**employerData)
        
        return MonthlyEmployeeDataFactory(**employeeData)


















            
        
        