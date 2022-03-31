import pandas as pd


def get_form_handler(form):
    if form == "480.6 A":
        columns = ['Customer_ID', 'Tax_Year', 'File_Name', 'Form', 'Payee_Type', 'Payee_Name',
                   'Payee_Address_1', 'Payee_Address_2', 'Payee_City', 'Payee_State', 'Payee_Zipcode',
                   'Phone_Number', 'Email', 'Payee_EIN', 'Payer_Name', "Rents", "Interests_under_Section_102304"
            , "Interests_under_Section_10230", "Other_Interests", "Dividends", "Capital_Gain_Distributions",
                   "Debt_Discharge", "Royalties"]
    elif form == "480.6 D":
        columns = ['Customer_ID', 'Tax_Year', 'File_Name', 'Form', 'Payee_Type', 'Payee_Name',
                   'Payee_Address_1', 'Payee_Address_2', 'Payee_City', 'Payee_State', 'Payee_Zipcode',
                   'Phone_Number', 'Email', 'Payee_EIN', 'Payer_Name', "Accumulated_Gain_on_Nonqualified_Options",
                   "Distributions_of_Amounts_Previously_Notified", "Compensation_for_Injuries"
            , "Deductible_Individual_Retirement_Accounts", "Rent_from_Residential_Property",
                   "Interest_upon_Obligations_from_the_United_States_Government",
                   "Interests_upon_Obligations_from_the_Government_of_Puerto_Rico",
                   "Interests_upon_Certain_Mortgages_1",
                   "Interests_upon_Certain_Mortgages_2", "Interests_on_bonds",
                   "Other_Interests_Subject_to_Alternate_Basic_Tax_1",
                   "Other_Interests_Subject_to_Alternate_Basic_Tax_2",
                   "Other_Interests_Not_Subject_to_Alternate_Basic_Tax", "Dividends_from_Cooperative_Associations_1",
                   "Dividends_from_Cooperative_Associations_2", "Dividends_from_an_International_Insurer"
                   ]
    elif form == "480.6 SP":
        columns = ['Customer_ID', 'Tax_Year', 'File_Name', 'Form', 'Payee_Type', 'Payee_Name',
                   'Payee_Address_1', 'Payee_Address_2', 'Payee_City', 'Payee_State', 'Payee_Zipcode',
                   'Phone_Number', 'Email', 'Payee_EIN', 'Payer_Name',
                   "Payments_for_Services_Rendered_by_Individuals_Not_Subject_to_Withholding",
                   "Payments_for_Services_Rendered_by_Corporations_and_Partnerships_Not_Subject_to_Withholding",
                   "Payments_for_Services_Rendered_by_Individuals_Subject_to_Withholding_1",
                   "Payments_for_Services_Rendered_by_Individuals_Subject_to_Withholding_2",
                   "Payments_for_Services_Rendered_by_Corporations_and_Partnerships_Subject_to_Withholding_1",
                   "Payments_for_Services_Rendered_by_Corporations_and_Partnerships_Subject_to_Withholding_2"

                   ]
    elif form == "480.6 EC":
        columns = ['Customer_ID', 'Tax_Year', 'File_Name', 'Form', 'Payee_Type', 'Payee_Name',
                   'Payee_Address_1', 'Payee_Address_2', 'Payee_City', 'Payee_State', 'Payee_Zipcode',
                   'Phone_Number', 'Email', 'Payee_EIN', 'Payer_Name',
                   "Socio_Gestor",
                   "Socio_Limitado",
                   "Socio_Ilimitado",
                   "Individuo",
                   "Fideicomiso",
                   "Caudal_Relicto"]
    else:
        columns = []

    return form, pd.DataFrame(columns=columns)
