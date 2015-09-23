
from .models import *
from .helpers import *
from .calculations import *


class ReportsMaker(object):
	"""docstring for ReportsMaker"""
	def __init__(self , employer):
		super(ReportsMaker, self).__init__()
		self.data_getter = data_getter()
		self.income_tax = income_tax_calculations(user_id=employer.user.id)
		self.social_security = social_security_calculations(user_id=employer.user.id)
		self.vat = vat_calculations(user_id=employer.user.id)
		self.cross = cross_calculations(user_id=employer.user.id)

	def monthly_employee_report(self, employee, for_year, for_month):
		return self.cross.monthly_employee_report(employee, for_year, for_month)

	def monthly_employer_report(self, for_year, for_month):
		report_data = {
			'social_security': {
				'count_of_employees_that_are_required_to_pay_social_security' : self.social_security.get_count_of_employees_that_are_required_to_pay_social_security_by_employer(for_year , for_month),
	            'sum_of_gross_payment_of_employees_that_are_required_to_pay_social_security': self.social_security.get_sum_of_gross_payment_of_employees_that_are_required_to_pay_social_security_by_employer(for_year , for_month)['my_total'],
	            'sum_of_gross_payment_to_be_paid_at_lower_employer_rate_social_security': self.social_security.get_sum_of_lower_employer_social_security_by_employer(for_year , for_month),
	            'sum_of_gross_payment_to_be_paid_at_lower_employee_rate_social_security': self.social_security.get_sum_of_lower_employee_social_security_by_employer(for_year , for_month),
	            'total_of_social_security_due': self.social_security.get_total_of_social_security_due_by_employer(for_year, for_month),
	            'count_of_employees_that_do_not_exceed_the_social_security_threshold': self.social_security.get_count_of_employees_that_do_not_exceed_the_social_security_threshold_by_employer(for_year, for_month)
			} , 
			'vat': {
				'sum_of_gross_payment_where_no_vat_is_required': self.vat.get_sum_of_gross_payment_where_no_vat_is_required(for_year=for_year , for_month=for_month),
				'count_of_employees_where_no_vat_is_required': self.vat.get_count_of_employees_where_no_vat_is_required(for_year=for_year , for_month=for_month),
				'sum_of_vat_due_where_no_vat_is_required': self.vat.get_sum_of_vat_due_where_no_vat_is_required(for_year=for_year , for_month=for_month)
			} , 
			'income_tax': {
				'count_of_employees_that_got_paid_this_month': self.income_tax.get_count_of_employees_that_got_paid_this_month(for_year=for_year , for_month=for_month),
				'sum_of_gross_payment_and_vat_for_employees_that_got_paid_this_month': self.income_tax.get_sum_of_gross_payment_and_vat_for_employees_that_got_paid_this_month(for_year=for_year , for_month=for_month),
				'sum_of_income_tax':self.income_tax.get_sum_of_income_tax(for_year=for_year , for_month=for_month)
			} ,
			'book_keeping_where_no_vat_is_required': {
				'sum_of_gross_payment_where_no_vat_is_required': self.vat.get_sum_of_gross_payment_where_no_vat_is_required(for_year=for_year , for_month=for_month),
	            'sum_of_employer_social_security_where_no_vat_is_required': self.cross.get_sum_of_employer_social_security_where_no_vat_is_required(for_year=for_year , for_month=for_month),
	            'sum_of_net_payment_where_no_vat_is_required': self.cross.get_sum_of_net_payment_where_no_vat_is_required(for_year=for_year , for_month=for_month),
	            'sum_of_income_tax_where_no_vat_is_required': self.cross.get_sum_of_income_tax_where_no_vat_is_required(for_year=for_year , for_month=for_month),
	            'sum_of_social_security_where_no_vat_is_required': self.cross.get_sum_of_social_security_where_no_vat_is_required(for_year=for_year , for_month=for_month),
	            'list_of_names_and_monthly_net_where_no_vat_is_required': self.cross.get_list_of_names_and_monthly_net_where_no_vat_is_required(for_year=for_year , for_month=for_month),
			} ,
			'book_keeping_where_vat_is_required': {
				'list_of_names_and_income_tax_where_vat_is_required': self.cross.get_list_of_names_and_income_tax_where_vat_is_required(for_year=for_year , for_month=for_month),
				'sum_of_income_tax_where_vat_is_required': self.cross.get_sum_of_income_tax_where_vat_is_required(for_year=for_year , for_month=for_month),
				'list_of_names_and_social_security_employee_where_vat_is_required': self.cross.get_list_of_names_and_social_security_employee_where_vat_is_required(for_year=for_year , for_month=for_month),
				'sum_of_social_security_employer_where_vat_is_required': self.cross.get_sum_of_social_security_employer_where_vat_is_required(for_year=for_year , for_month=for_month),
				'sum_of_social_security_where_vat_is_required': self.cross.get_sum_of_social_security_where_vat_is_required(for_year=for_year , for_month=for_month),
			}
			
		}
		return report_data
	def quarterly_social_security_report(self, for_year, for_month):
		return self.social_security.generate_quarterly_social_security_report(for_year, for_month)
		return [
			{
				'first_name': 'coco',
	            'last_name': 'coco',
	            'government_id': 'coco',
	            'birthday': 'coco',
	            'months_data': 'coco',
			}
		]
	def yearly_employee_report(self, employee, for_year):
		pass
	
	def yearly_social_security_employer_report(self, employer, for_year):
		pass

	#856 report
	def yearly_income_tax_employer_report(self, employer, for_year):
		pass