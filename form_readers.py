## imports
import pandas as pd
import pdftotext


def read_suri_files_form_f(path):
    memory_file = open(path, 'rb')
    # pdf = pdftotext.PDF(BytesIO(path).read())
    pdf = pdftotext.PDF(path)
    data = []
    # Iterate over all the pages
    for page in pdf:
        #     print(page)
        data = page.split("\n")
        break
    memory_file.close()

    columns = ['Customer_ID', 'Tax_Year', 'File_Name', 'Form', 'Payee_Type', 'Payee_SSN', 'Payee_Name',
               'Payee_Address_1', 'Payee_Address_2', 'Payee_City', 'Payee_State', 'Payee_Zipcode',
               'Phone_Number', 'Email', 'Payee_EIN', 'Payer_Name', "Insurance_Premiums", "Contributions_to_Health"
        , "Telecommunication_Services", "Advertising", "Internet_and_Cable", "Bundles", "Other_Related_Payments"]

    df = pd.DataFrame(columns=columns)

    form_no = data[0].split()[1]
    tax_year = data[7].split()[2]
    payee_name = data[16].split("Check")[0].strip()
    file_name = (form_no + "-" + tax_year + "-" + payee_name).strip()
    ssn = data[30].split()[0]
    address1 = data[18].split("Contributions")[0].strip()
    address2 = data[19].split()[0]
    if "Marque" in address2:
        address2 = ""
    city = data[21].split("Código")[0].strip()
    state = city.split(",")[1].strip()
    zip_code = data[21].split("Zip Code")[1].strip()
    phone_number = data[24].split()[0]
    email = data[24].split()[1]
    payee_ein = data[12].split()[0]
    payer_name = data[34].strip()
    insurance_premium = data[13].split()[-1]
    contributions_to_health = data[18].split()[-1]
    telecommunication_services = data[23].split()[-1]
    advertising = data[28].split()[-1]
    internet_and_cable = data[33].split()[-1]
    bundles = data[38].split()[-1]
    other_related_payments = data[42].split()[-1]

    row = ["", tax_year, file_name, form_no, "", ssn, payee_name, address1, address2, city, state, zip_code,
           phone_number, email, payee_ein, payer_name, insurance_premium, contributions_to_health,
           telecommunication_services, advertising, internet_and_cable, bundles, other_related_payments]

    df.loc[len(df)] = row

    return df


def read_suri_files_form_a(path):
    memory_file = open(path, 'rb')

    pdf = pdftotext.PDF(memory_file)
    data = []
    # Iterate over all the pages
    for page in pdf:
        #     print(page)
        data = page.split("\n")
        break
    memory_file.close()

    columns = ['Customer_ID', 'Tax_Year', 'File_Name', 'Form', 'Payee_Type', 'Payee_Name',
               'Payee_Address_1', 'Payee_Address_2', 'Payee_City', 'Payee_State', 'Payee_Zipcode',
               'Phone_Number', 'Email', 'Payee_EIN', 'Payer_Name', "Rents", "Interests_under_Section_102304"
        , "Interests_under_Section_10230", "Other_Interests", "Dividends", "Capital_Gain_Distributions",
               "Debt_Discharge", "Royalties"]

    df = pd.DataFrame(columns=columns)

    Customer_ID = ''
    Tax_Year = data[6].split()[2]
    Form = data[0].split()[1]
    Payee_Name = data[13].split("2.")[0].strip()
    File_Name = (Form + "-" + Tax_Year + "-" + Payee_Name).strip()
    Payee_Type = ""
    Payee_Address_1 = data[16].strip()
    Payee_Address_2 = data[18].split("Interests under")[0].strip()
    Payee_City = data[19].split(",")[0]
    Payee_State = data[19].split(",")[1].split()[0]
    Payee_Zipcode = data[19].split(",")[1].split()[1]
    Phone_Number = data[24].split()[0]
    Email = data[24].split()[1]
    Payee_EIN = data[11].split()[0]
    Payer_Name = data[34]  # .split()[0]
    Rents = data[11].split()[-1]
    Interests_under_Section_102304 = data[14].split()[-1]
    Interests_under_Section_10230 = data[18].split()[-1]
    Other_Interests = data[22].split()[-1]
    Dividends = data[25].split()[-1]
    Capital_Gain_Distributions = data[29].split()[-1]
    Debt_Discharge = data[31].split()[-1]
    Royalties = data[37].split()[-1]

    row = [Customer_ID, Tax_Year, File_Name, Form, Payee_Type, Payee_Name,
           Payee_Address_1, Payee_Address_2, Payee_City, Payee_State, Payee_Zipcode,
           Phone_Number, Email, Payee_EIN, Payer_Name, Rents, Interests_under_Section_102304
        , Interests_under_Section_10230, Other_Interests, Dividends, Capital_Gain_Distributions,
           Debt_Discharge, Royalties]

    df.loc[len(df)] = row

    return df


def read_suri_files_form_d(path):
    memory_file = open(path, 'rb')
    pdf = pdftotext.PDF(memory_file)
    data = []
    # Iterate over all the pages
    for page in pdf:
        #     print(page)
        data = page.split("\n")
        break
    memory_file.close()

    columns = ['Customer_ID', 'Tax_Year', 'File_Name', 'Form', 'Payee_Type', 'Payee_Name',
               'Payee_Address_1', 'Payee_Address_2', 'Payee_City', 'Payee_State', 'Payee_Zipcode',
               'Phone_Number', 'Email', 'Payee_EIN', 'Payer_Name', "Accumulated_Gain_on_Nonqualified_Options",
               "Distributions_of_Amounts_Previously_Notified", "Compensation_for_Injuries"
        , "Deductible_Individual_Retirement_Accounts", "Rent_from_Residential_Property",
               "Interest_upon_Obligations_from_the_United_States_Government",
               "Interests_upon_Obligations_from_the_Government_of_Puerto_Rico", "Interests_upon_Certain_Mortgages_1",
               "Interests_upon_Certain_Mortgages_2", "Interests_on_bonds",
               "Other_Interests_Subject_to_Alternate_Basic_Tax_1", "Other_Interests_Subject_to_Alternate_Basic_Tax_2",
               "Other_Interests_Not_Subject_to_Alternate_Basic_Tax", "Dividends_from_Cooperative_Associations_1",
               "Dividends_from_Cooperative_Associations_2", "Dividends_from_an_International_Insurer"
               ]

    df = pd.DataFrame(columns=columns)
    Customer_ID = data[12].split()[1]
    Tax_Year = data[7].split()[0]
    Form = data[0].split()[1]
    Payee_Name = data[14].split("    ")[-1]
    Payee_Type = ""
    File_Name = (Form + "-" + Tax_Year + "-" + Payee_Name).strip()
    Payee_Address_1 = data[16].split("    ")[0].strip()
    Payee_Address_2 = ""
    Payee_City = data[18].split("Zip Code")[1].split(",")[0].strip()
    Payee_State = data[18].split("Zip Code")[1].split(",")[1].split()[0]
    Payee_Zipcode = data[18].split("Zip Code")[1].split(",")[1].split()[1]
    Phone_Number = data[20].split()[0]
    Email = data[20].split()[1]
    Payee_EIN = data[12].split()[1]
    Payer_Name = data[14].split("    ")[0]
    Accumulated_Gain_on_Nonqualified_Options = data[27].split()[-1]
    Distributions_of_Amounts_Previously_Notified = data[30].split()[-1]
    Compensation_for_Injuries = data[32].split()[-1]
    Deductible_Individual_Retirement_Accounts = data[34].split()[-1]
    Rent_from_Residential_Property = data[36].split()[-1]
    Interest_upon_Obligations_from_the_United_States_Government = data[38].split()[-1]
    Interests_upon_Obligations_from_the_Government_of_Puerto_Rico = data[40].split()[-1]
    Interests_upon_Certain_Mortgages_1 = data[42].split()[-2]
    Interests_upon_Certain_Mortgages_2 = data[42].split()[-1]
    Interests_on_bonds = data[44].split()[-1]
    Other_Interests_Subject_to_Alternate_Basic_Tax_1 = data[46].split()[-1]
    Other_Interests_Subject_to_Alternate_Basic_Tax_2 = data[47].split()[-1]
    Other_Interests_Not_Subject_to_Alternate_Basic_Tax = data[48].split()[-1]
    Dividends_from_Cooperative_Associations_1 = data[51].split()[-2]
    Dividends_from_Cooperative_Associations_2 = data[51].split()[-1]
    Dividends_from_an_International_Insurer = data[52].split()[-1]
    scope = locals()
    row = [eval(x, scope) for x in columns]
    df.loc[len(df)] = row
    return df



def read_suri_files_form_sp(path):
    memory_file = open(path, 'rb')
    pdf = pdftotext.PDF(memory_file)
    data = []
    # Iterate over all the pages
    for page in pdf:
        #     print(page)
        data = page.split("\n")
        break
    memory_file.close()

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

    df = pd.DataFrame(columns=columns)

    Customer_ID = ""
    Tax_Year = data[6].split()[2]
    Form = data[0].split()[1]
    Payee_Name = data[29].split("          ")[0]
    Payee_Type = ""
    File_Name = (Form + "-" + Tax_Year + "-" + Payee_Name).strip()
    Payee_Address_1 = data[31].split("          ")[0]
    Payee_Address_2 = ""
    Payee_City = data[33].split(",")[0]
    try:
        Payee_State = data[33].split(",")[1].split()[0]
    except:
        Payee_State = "PR"
    try:
        Payee_Zipcode = data[33].split(",")[1].split()[1]
    except:
        Payee_Zipcode = "00984-4819"
    Phone_Number = data[23].split()[0]
    Email = data[23].split()[1]
    Payee_EIN = data[26].split()[0]
    Payer_Name = data[15].split("      ")[0].strip()
    Payments_for_Services_Rendered_by_Individuals_Not_Subject_to_Withholding = data[17].split()[-1]
    Payments_for_Services_Rendered_by_Corporations_and_Partnerships_Not_Subject_to_Withholding = data[23].split()[-1]
    Payments_for_Services_Rendered_by_Individuals_Subject_to_Withholding_1 = data[27].split()[-1]
    Payments_for_Services_Rendered_by_Individuals_Subject_to_Withholding_2 = data[27].split()[-2]
    Payments_for_Services_Rendered_by_Corporations_and_Partnerships_Subject_to_Withholding_1 = data[32].split()[-2]
    Payments_for_Services_Rendered_by_Corporations_and_Partnerships_Subject_to_Withholding_2 = data[32].split()[-1]

    scope = locals()
    row = [eval(x, scope) for x in columns]
    df.loc[len(df)] = row

    return df


def read_suri_files_form_ec(path):
    memory_file = open(path, 'rb')
    pdf = pdftotext.PDF(memory_file)
    data = []
    # Iterate over all the pages
    for page in pdf:
        #     print(page)
        data = page.split("\n")
        break
    memory_file.close()

    columns = ['Customer_ID', 'Tax_Year', 'File_Name', 'Form', 'Payee_Type', 'Payee_Name',
               'Payee_Address_1', 'Payee_Address_2', 'Payee_City', 'Payee_State', 'Payee_Zipcode',
               'Phone_Number', 'Email', 'Payee_EIN', 'Payer_Name',
               "Socio_Gestor",
               "Socio_Limitado",
               "Socio_Ilimitado",
               "Individuo",
               "Fideicomiso",
               "Caudal_Relicto"

               ]

    df = pd.DataFrame(columns=columns)

    Customer_ID = ""
    Tax_Year = data[0].split()[0] + data[1].split()[3]
    Form = data[1].split()[1]
    Payee_Name = data[18].split("       ")[0]
    Payee_Type = ""
    File_Name = (Form + "-" + Tax_Year + "-" + Payee_Name).strip()
    Payee_Address_1 = data[24].split(",")[0].strip()
    Payee_Address_2 = ""
    Payee_City = data[24].split(",")[0].split()[-2] + " " + data[24].split(",")[0].split()[-1]
    Payee_State = data[24].split(",")[1].split()[0]
    Payee_Zipcode = data[24].split(",")[1].split()[-1]
    Phone_Number = data[26].split()[-1]
    Email = ""
    Payee_EIN = data[19].split()[-2]
    Payer_Name = ""
    Socio_Gestor = "No"
    Socio_Limitado = "Yes"
    Socio_Ilimitado = "No"
    Individuo = "Yes"
    Fideicomiso = "No"
    Caudal_Relicto = "No"

    scope = locals()
    row = [eval(x, scope) for x in columns]
    df.loc[len(df)] = row

    return df