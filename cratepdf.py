import pdfsheetfunction
from fpdf import FPDF
style=pdfsheetfunction
def createpdf(payroll):

    pdf = FPDF() 
    
    # Add a page 
    pdf.add_page() 

    pdf.rect(5.0, 5.0, 200.0,287.0)
    # set style and size of font  
    # that you want in the pdf 
    pdf.set_font("Arial", size = 15) 
    
    # create a cell 
    # pdf.cell(200, 10, txt = payroll.name,  
    #         ln = 1, align = 'C') 
    style.titles(pdf=pdf,title=str(payroll.CompanyName))
    style.regNo(pdf=pdf)
    style.paysheettitle(pdf=pdf)
    style.paymonth(pdf=pdf,month=str(payroll.payRollMonth))
    style.nametitle(pdf=pdf,name=str(payroll.name))
    style.line(self=pdf)
    style.name(pdf=pdf,name=str(payroll.name))
    style.epfNo(pdf=pdf,epf=str(payroll.epfNo))
    style.designation(pdf=pdf)
    style.workingdays(pdf=pdf,workingdays=str(payroll.days))
    style.rate(pdf=pdf,rate=str(payroll.rate))
    style.salary(pdf=pdf)
    style.basic(pdf=pdf,basic=str(payroll.amount))
    style.basicgt(pdf=pdf,basic=str(payroll.amount))
    style.basicamount(pdf=pdf,basic=str(payroll.amount))
    style.basicgtamount(pdf=pdf,basic=str(payroll.amount))
    style.ot1(pdf=pdf)
    style.ot1amount(pdf=pdf,ot1=str(payroll.ot1ttl))
    style.ot1rate(pdf=pdf)
    style.ot1rateamount(pdf=pdf,ot1r=str(payroll.ot1rate))
    style.ot1hrs(pdf=pdf)
    style.ot1hrsamount(pdf=pdf,ot1h=str(payroll.ot1hrs))
    style.ot2(pdf=pdf)
    style.ot2amount(pdf=pdf,ot2=str(payroll.ot2ttl))
    style.ot2rate(pdf=pdf)
    style.ot2rateamount(pdf=pdf,ot2r=str(payroll.ot2rate))
    style.ot2hrs(pdf=pdf)
    style.ot2hrsamount(pdf=pdf,ot2h=str(payroll.ot2hrs))
    style.dayoff(pdf=pdf)
    style.dayoffamount(pdf=pdf,dayoffamount=str(payroll.dayoffamount))
    style.dayoffrate(pdf=pdf)
    style.dayoffrateamount(pdf=pdf,dayoofr=str(payroll.rate))
    style.dayoffhrs(pdf=pdf)
    style.dayoffcount(pdf=pdf,dayoffcount=str(payroll.dayoffcount))
    style.attendeceallowence(pdf=pdf)
    style.attendeceallowenceamount(pdf=pdf,ata=str(payroll.attendenceAllowence))
    style.attendeceincentice(pdf=pdf)
    style.attendeceincentiveamount(pdf=pdf,ata=str(payroll.attendenceincentive))
    style.grosssalary(pdf=pdf)
    style.grosssalaryamount(pdf=pdf,gs=str(payroll.grosssalary))
    style.deductions(pdf=pdf)
    style.epf8(pdf=pdf)
    style.epf8amount(pdf=pdf,gs=str(payroll.epf8amount))
    style.salaryadvance(pdf=pdf)
    style.salaryadvanceamount(pdf=pdf,gs=str("           "))
    style.toatldeduction(pdf=pdf)
    style.toatldeductionamount(pdf=pdf,gs=str(payroll.epf8amount))
    style.netpay(pdf=pdf)
    style.netpayamount(pdf=pdf,gs=str(payroll.totalearning))
    style.epf12(pdf=pdf)
    style.epf12amount(pdf=pdf,gs=str(payroll.epf12amount))
    style.etf3(pdf=pdf)
    style.etf3amount(pdf=pdf,gs=str(payroll.etf3))
    # add another cell 
    # pdf.cell(200, 10, txt = str(payroll.rate), 
    #         ln = 2, align = 'C') 
    path="D:/testpdfs/"+str(payroll.epfNo)+".pdf"
    # save the pdf with name .pdf 
    pdf.output(path)
