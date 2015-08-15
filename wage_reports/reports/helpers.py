from django.utils import timezone

def get_month_in_question_for_employee_locking():
    this_month = timezone.now()
    month_in_question = this_month.month
    return month_in_question

def get_year_in_question_for_employee_locking():
    this_month = timezone.now()
    year_in_question = this_month.year
    return year_in_question

def get_month_in_question_for_employer_locking():
    this_month = timezone.now()
    month_in_question = this_month.month - 1
    if month_in_question == 0:
        return 12
    return month_in_question

def get_year_in_question_for_employer_locking():
    this_month = timezone.now()
    year_in_question = this_month.year
    month_in_question = get_month_in_question_for_employer_locking()
    if month_in_question == 12:
        return year_in_question - 1
    return year_in_question

def calculate_social_security_employer(overall_gross,social_security_threshold,lower_employer_social_security_percentage,upper_employer_social_security_percentage,is_required_to_pay_social_security):
    return calculate_social_security_generic(overall_gross,social_security_threshold,lower_employer_social_security_percentage,upper_employer_social_security_percentage,is_required_to_pay_social_security)

def calculate_social_security_generic(overall_gross,social_security_threshold,lower_social_security_percentage,upper_social_security_percentage,is_required_to_pay_social_security):
    if not is_required_to_pay_social_security:
        return 0   
    if overall_gross <= social_security_threshold:
        return overall_gross * lower_social_security_percentage
    else:
        diminished_sum = social_security_threshold * lower_social_security_percentage
        standard_sum = (overall_gross - social_security_threshold) * upper_social_security_percentage
        return diminished_sum + standard_sum



def calculate_social_security_employee(overall_gross,social_security_threshold,lower_employee_social_security_percentage,upper_employee_social_security_percentage,is_required_to_pay_social_security , is_employer_the_main_employer, gross_payment_from_others):
    if not is_required_to_pay_social_security:
        return 0   
    if is_employer_the_main_employer:
        updated_threshold = social_security_threshold
    else:
        updated_threshold = social_security_threshold - gross_payment_from_others
        if updated_threshold < 0:
            updated_threshold = 0

    return calculate_social_security_generic(overall_gross,updated_threshold,lower_employee_social_security_percentage,upper_employee_social_security_percentage,is_required_to_pay_social_security)