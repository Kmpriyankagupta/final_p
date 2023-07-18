from django.shortcuts import render, redirect
from .models import MyModel 
from .models import Page 
def home(request):
    data = Page.objects.get(pagename='index')
    return render(request, 'app/index.html', context={'data': data})
def Private_limited(request):
    data = Page.objects.get(pagename='private-limited-company-registration')
    return render(request, 'app/private-limited-company-registration.html', context ={'data':data})



def limited_liability(request):
    data = Page.objects.get(pagename='limited-liability-partnership-registration')
    return render(request, 'app/limited-liability-partnership-registration.html', context={'data': data})

def one_person(request):
    data = Page.objects.get(pagename='one-person-company-registration')
    return render(request, 'app/one-person-company-registration.html', context={'data': data})

def partnership(request):
    data = Page.objects.get(pagename='partnership-firm-registration')
    return render(request, 'app/partnership-firm-registration.html', context={'data': data})

def sole_proprietarship(request):
    data = Page.objects.get(pagename='sole-proprietarship-firm-registration')
    return render(request, 'app/sole-proprietarship-firm-registration.html', context={'data': data})

def register_an(request):
    data = Page.objects.get(pagename='register-an-indian-subsidiary')
    return render(request, 'app/register-an-indian-subsidiary.html', context={'data': data})

def section_8(request):
    data = Page.objects.get(pagename='section-8-company-registration')
    return render(request, 'app/section-8-company-registration.html', context={'data': data})

def producer_company(request):
    data = Page.objects.get(pagename='producer-company-registration')
    return render(request, 'app/producer-company-registration.html', context={'data': data})

def nidhi_company(request):
    data = Page.objects.get(pagename='nidhi-company-registration')
    return render(request, 'app/nidhi-company-registration.html', context={'data': data})

def trademark_registration(request):
    data = Page.objects.get(pagename='trademark-registration')
    return render(request, 'app/trademark-registration.html', context={'data': data})

def trademark_objection(request):
    data = Page.objects.get(pagename='trademark-objection-reply')
    return render(request, 'app/trademark-objection-reply.html', context={'data': data})

def trademark_opposition(request):
    data = Page.objects.get(pagename='trademark-opposition')
    return render(request, 'app/trademark-opposition.html', context={'data': data})

def trademark_renewal(request):
    data = Page.objects.get(pagename='trademark-renewal')
    return render(request, 'app/trademark-renewal.html', context={'data': data})

def trademark_ass(request):
    data = Page.objects.get(pagename='trademark-asignment')
    return render(request, 'app/trademark-asignment.html', context={'data': data})

def patent_sear(request):
    data = Page.objects.get(pagename='patent-search')
    return render(request, 'app/patent-search.html', context={'data': data})

def provisional_patent(request):
    data = Page.objects.get(pagename='provisional-patent')
    return render(request, 'app/provisional-patent.html', context={'data': data})

def permanent_patent(request):
    data = Page.objects.get(pagename='permanent-patent')
    return render(request, 'app/permanent-patent.html', context={'data': data})

def copyright_reg(request):
    data = Page.objects.get(pagename='copyright-registration')
    return render(request, 'app/copyright-registration.html', context={'data': data})

def design_regi(request):
    data = Page.objects.get(pagename='design-registration')
    return render(request, 'app/design-registration.html', context={'data': data})

def proprietorship_to_par(request):
    data = Page.objects.get(pagename='proprietorship-to-partnership')
    return render(request, 'app/proprietorship-to-partnership.html', context={'data': data})

def proprietorship_to_llp(request):
    data = Page.objects.get(pagename='proprietorship-to-LLP')
    return render(request, 'app/proprietorship-to-LLP.html', context={'data': data})

def proprietorship_to_pri(request):
    data = Page.objects.get(pagename='proprietorship-to-private-limited-company')
    return render(request, 'app/proprietorship-to-private-limited-company.html', context={'data': data})

def proprietorship_to_opc(request):
    data = Page.objects.get(pagename='Sole Proprietorship to OPC')
    return render(request, 'app/proprietorship-to-OPC.html', context={'data': data})

def parternship_to_llp(request):
    data = Page.objects.get(pagename='partnership-to-LLP')
    return render(request, 'app/partnership-to-LLP.html', context={'data': data})

def parternship_to_private(request):
    data = Page.objects.get(pagename='partnership-to-private-limited-company')
    return render(request, 'app/partnership-to-private-limited-company.html', context={'data': data})

def llp_to_private(request):
    data = Page.objects.get(pagename='LLP-to-private-limited-company')
    return render(request, 'app/LLP-to-private-limited-company.html', context={'data': data})

def opc_to_private(request):
    data = Page.objects.get(pagename='OPC-to-private-limited-company')
    return render(request, 'app/OPC-to-private-limited-company.html', context={'data': data})

def private_limited_company_to_llp(request):
    data = Page.objects.get(pagename='private-limited-company-to-LLP')
    return render(request, 'app/private-limited-company-to-LLP.html', context={'data': data})

def private_company_to_public(request):
    data = Page.objects.get(pagename='private-company-to-public-company')
    return render(request, 'app/private-company-to-public-company.html', context={'data': data})

def add_or_reove_a_dir(request):
    data = Page.objects.get(pagename='add-or-remove-a-director-company')
    return render(request, 'app/add-or-remove-a-director-company.html', context={'data': data})

def add_or_reove_a_par(request):
    data = Page.objects.get(pagename='add-or-remove-a-partner-LLP')
    return render(request, 'app/add-or-remove-a-partner-LLP.html', context={'data': data})


def change_business(request):
    data = Page.objects.get(pagename='change-business-activity')
    return render(request, 'app/change-business-activity.html', context={'data': data})

def change_registered(request):
    data = Page.objects.get(pagename='change-registered-office')
    return render(request, 'app/change-registered-office.html', context={'data': data})

def change_company_name(request):
    data = Page.objects.get(pagename='change-company-name')
    return render(request, 'app/change-company-name.html', context={'data': data})

def change_llp_agr(request):
    data = Page.objects.get(pagename='change-LLP-agreement')
    return render(request, 'app/change-LLP-agreement.html', context={'data': data})

def change_partenership_de(request):
    data = Page.objects.get(pagename='change-partnership-deed')
    return render(request, 'app/change-partnership-deed.html', context={'data': data})

def increase_authorised(request):
    data = Page.objects.get(pagename='increase-authorised-share-capital')
    return render(request, 'app/increase-authorised-share-capital.html', context={'data': data})

def close_a_private_limited(request):
    data = Page.objects.get(pagename='close-a-private-limited-company')
    return render(request, 'app/close-a-private-limited-company.html', context={'data': data})

def close_a_limited_liability(request):
    data = Page.objects.get(pagename='close-a-limited-liability-partnership')
    return render(request, 'app/close-a-limited-liability-partnership.html', context={'data': data})

def close_a_one_person(request):
    data = Page.objects.get(pagename='close-a-one-person-company')
    return render(request, 'app/close-a-one-person-company.html', context={'data': data})

def dissolve_a_par(request):
    data = Page.objects.get(pagename='dissolve-a-parnership-farm')
    return render(request, 'app/dissolve-a-parnership-farm.html', context={'data': data})

def gst_registration(request):
    data = Page.objects.get(pagename='GST-registration')
    return render(request, 'app/GST-registration.html', context={'data': data})

def import_export_co(request):
    data = Page.objects.get(pagename='import-export-code-registration')
    return render(request, 'app/import-export-code-registration.html', context={'data': data})

def startup_in(request):
    data = Page.objects.get(pagename='startup-india-registration')
    return render(request, 'app/startup-india-registration.html', context={'data': data})

def lut_under(request):
    data = Page.objects.get(pagename='LUT-under-GST')
    return render(request, 'app/LUT-under-GST.html', context={'data': data})

def ssi_msme(request):
    data = Page.objects.get(pagename='SSI-MSME-registration')
    return render(request, 'app/SSI-MSME-registration.html', context={'data': data})

def shop_est(request):
    data = Page.objects.get(pagename='shop-establishment-registration')
    return render(request, 'app/shop-establishment-registration.html', context={'data': data})

def professional_tax(request):
    data = Page.objects.get(pagename='professional-tax-registration')
    return render(request, 'app/professional-tax-registration.html', context={'data': data})

def pan_application(request):
    data = Page.objects.get(pagename='PAN-application')
    return render(request, 'app/PAN-application.html', context={'data': data})

def tan_application(request):
    data = Page.objects.get(pagename='TAN-application')
    return render(request, 'app/TAN-application.html', context={'data': data})

def fssai_application(request):
    data = Page.objects.get(pagename='FSSAI-application')
    return render(request, 'app/FSSAI-application.html', context={'data': data})

def esi_registration(request):
    data = Page.objects.get(pagename='ESI-registration')
    return render(request, 'app/ESI-registration.html', context={'data': data})

def pf_registraion(request):
    data = Page.objects.get(pagename='PF-registration')
    return render(request, 'app/PF-registration.html', context={'data': data})

def gem_registration(request):
    data = Page.objects.get(pagename='GEM-registration')
    return render(request, 'app/GEM-registration.html', context={'data': data})

def nsic_re(request):
    data = Page.objects.get(pagename='NSIC-registration')
    return render(request, 'app/NSIC-registration.html', context={'data': data})

def factory_lic(request):
    data = Page.objects.get(pagename='factory-license')
    return render(request, 'app/factory-license.html', context={'data': data})

def trade_license(request):
    data = Page.objects.get(pagename='trade-license')
    return render(request, 'app/trade-license.html', context={'data': data})

def drug_li(request):
    data = Page.objects.get(pagename='drug-license')
    return render(request, 'app/drug-license.html', context={'data': data})

def liquor(request):
    data = Page.objects.get(pagename='liquor-license')
    return render(request, 'app/liquor-license.html', context={'data': data})

def labour(request):
    data = Page.objects.get(pagename='labour-license')
    return render(request, 'app/labour-license.html', context={'data': data})

def ayush(request):
    data = Page.objects.get(pagename='ayush-license')
    return render(request, 'app/ayush-license.html', context={'data': data})

def iso_certi(request):
    data = Page.objects.get(pagename='ISO-certification')
    return render(request, 'app/ISO-certification.html', context={'data': data})

def arai_certi(request):
    data = Page.objects.get(pagename='ARAI-certification')
    return render(request, 'app/ARAI-certification.html', context={'data': data})

def i_cat(request):
    data = Page.objects.get(pagename='I-CAT-certification')
    return render(request, 'app/I-CAT-certification.html', context={'data': data})

def dir3(request):
    data = Page.objects.get(pagename='DIR3-DIN-KYC-filling')
    return render(request, 'app/DIR3-DIN-KYC-filling.html', context={'data': data})

def roc_return_fiiling_for_pvt(request):
    data = Page.objects.get(pagename='ROC-return-filling-for-pvt-ltd')
    return render(request, 'app/ROC-return-filling-for-pvt-ltd.html', context={'data': data})

def roc_return_fiiling_for_opc(request):
    data = Page.objects.get(pagename='ROC-return-filling-for-OPC')
    return render(request, 'app/ROC-return-filling-for-OPC.html', context={'data': data})

def roc_return_fiiling_for_llp(request):
    data = Page.objects.get(pagename='ROC-return-filling-for-LLP')
    return render(request, 'app/ROC-return-filling-for-LLP.html', context={'data': data})

def personal_or_individaul(request):
    data = Page.objects.get(pagename='personal-or-individual-income-tax-filing')
    return render(request, 'app/personal-or-individual-income-tax-filing.html', context={'data': data})

def business_income(request):
    data = Page.objects.get(pagename='business-income-tax-filing')
    return render(request, 'app/business-income-tax-filing.html', context={'data': data})

def company_income(request):
    data = Page.objects.get(pagename='company-income-tax-filing')
    return render(request, 'app/company-income-tax-filing.html', context={'data': data})

def tds_filing(request):
    data = Page.objects.get(pagename='TDS-filing')
    return render(request, 'app/TDS-filing.html', context={'data': data})

def gst_return(request):
    data = Page.objects.get(pagename='GST-return-filing')
    return render(request, 'app/GST-return-filing.html', context={'data': data})

def video(request):
    data = Page.objects.get(pagename='video')
    return render(request, 'app/video.html', context={'data': data})

def contact(request):
    data = Page.objects.get(pagename='contact')
    return render(request, 'app/contact.html', context={'data': data})

def incorporation(request):
    data = Page.objects.get(pagename='incorporation-of-company')
    return render(request, 'app/incorporation-of-company.html', context={'data': data})

def trademark_blog(request):
    data = Page.objects.get(pagename='trademark_blog')
    return render(request, 'app/trademark-blog.html', context={'data': data})

def gst_blog(request):
    data = Page.objects.get(pagename='gst-blog')
    return render(request, 'app/gst-blog.html', context={'data': data})

def right_issue(request):
    data = Page.objects.get(pagename='right-issue')
    return render(request, 'app/right-issue.html', context={'data': data})

def bonus_issue(request):
    data = Page.objects.get(pagename='bonus-issue')
    return render(request, 'app/bonus-issue.html', context={'data': data})



def msme_registraion(request):
    data = Page.objects.get(pagename='msme-registration')
    return render(request, 'app/msme-registration.html', context={'data': data})

def blog(request):
    data = Page.objects.get(pagename='blog')
    return render(request, 'app/blog.html', context={'data': data})

def conversion_of_pri(request):
    data = Page.objects.get(pagename='conversion-of-private-comapany-into-public-company')
    return render(request, 'app/conversion-of-private-comapany-into-public-company.html', context={'data': data})

def legal_process_of_change(request):
    data = Page.objects.get(pagename='legal-process-of-change-your-company-name')
    return render(request, 'app/legal-process-of-change-your-company-name.html', context={'data': data})

def one_person_company_opc(request):
    data = Page.objects.get(pagename='one-person-company-OPC-registraion-process')
    return render(request, 'app/one-person-company-OPC-registraion-process.html', context={'data': data})



def procedure_for_nidhi_company_registraion(request):
    data = Page.objects.get(pagename='procedure-for-nidhi-company-registration')
    return render(request, 'app/procedure-for-nidhi-company-registration.html', context={'data': data})

def procedure_incorporation_of(request):
    data = Page.objects.get(pagename='procedure-incorporation-of-company')
    return render(request, 'app/procedure-incorporation-of-company.html', context={'data': data})

def employee_stock(request):
    data = Page.objects.get(pagename='employee-stock-ownership-plan')
    return render(request, 'app/employee-stock-ownership-plan.html', context={'data': data})

def public_limited_into_private(request):
    data = Page.objects.get(pagename='public-limited-into-private-limited')
    return render(request, 'app/public-limited-into-private-limited.html', context={'data': data})

def secretarial(request):
    data = Page.objects.get(pagename='secretarial-standard')
    return render(request, 'app/secretarial-standard.html', context={'data': data})

def pre_incorporation(request):
    data = Page.objects.get(pagename='pre-incorporation-contracts')
    return render(request, 'app/pre-incorporation-contracts.html', context={'data': data})

    



def save_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobilenumber = request.POST['mobilenumber']
        typeservicerequired = request.POST['typeservicerequired']
        if MyModel.objects.filter(name=name).exists():
            
            
            return render(request, 'app/message.html', {'error': 'Username already exists.'})
        else:
             MyModel.objects.create(name=name, email=email, mobilenumber=mobilenumber, typeservicerequired=typeservicerequired)
        
        return redirect('home')  # Redirect to a success page
   

    return render(request, 'app/index1.html')



