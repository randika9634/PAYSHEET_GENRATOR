def titles(pdf,title):
        pdf.set_xy(0.0,0.0)
        pdf.set_font('Arial', 'B', 35)
        pdf.set_text_color(220, 50, 50)
        pdf.cell(w=210.0, h=40.0, align='C', txt=title, border=0)

def regNo(pdf):
        pdf.set_xy(0.0,10.0)
        pdf.set_font('Arial', 'I', 10)
        pdf.set_text_color(100, 00, 10)
        pdf.cell(w=210.0, h=40.0, align='C', txt="REG.NO-W.C.14780", border=0 )

def paysheettitle(pdf):
        pdf.set_xy(0.0,18.0)
        pdf.set_font('Arial', 'B', 20)
        pdf.set_text_color(000, 00, 10)
        pdf.cell(w=210.0, h=40.0, align='C', txt="PAY SHEET", border=0 )

def paymonth(pdf,month):
        pdf.set_xy(0.0,26.0)
        pdf.set_font('Arial', 'B', 16)
        pdf.set_text_color(456, 85, 77)
        pdf.cell(w=210.0, h=40.0, align='C', txt=month, border=0 )

def nametitle(pdf,name):
        pdf.set_xy(00.0,35.0)
        pdf.set_font('Times', 'B', 16)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='C', txt=name, border=0 )       

def line(self):
        self.set_line_width(0.0)
        self.line(10.0,62.0,200.0,62.0) # top one

def name(pdf,name):
        pdf.set_xy(10.0,50.0)
        pdf.set_font('Times', 'B', 16)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="NAME : "+name, border=0 )

def epfNo(pdf,epf):
        pdf.set_xy(160.0,50.0)
        pdf.set_font('Times', 'B', 16)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="EPF : "+epf, border=0 )

def designation(pdf):
        pdf.set_xy(10.0,60.0)
        pdf.set_font('Times', 'B', 16)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="DESIGNATION : ", border=0 )

def workingdays(pdf,workingdays):
        pdf.set_xy(10.0,70.0)
        pdf.set_font('Times', 'B', 16)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="WORKING DAYS : "+workingdays, border=0 )

def rate(pdf,rate):
        pdf.set_xy(160.0,70.0)
        pdf.set_font('Times', 'B', 16)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="Rate : "+rate, border=0 )

def salary(pdf):
        pdf.set_xy(10.0,80.0)
        pdf.set_font('Times','U', 18,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="SALARY ", border=0 )


def basicgt(pdf,basic):
        pdf.set_xy(10.0,90.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="BASIC Inc bgtRA 1000 + 2500 :   ", border=0 )

def basicgtamount(pdf,basic):
        pdf.set_xy(100.0,90.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=basic, border=0 )

def basic(pdf,basic):
        pdf.set_xy(10.0,100.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="TOTAL P.F :   ", border=0 )

def basicamount(pdf,basic):
        pdf.set_xy(100.0,100.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=basic, border=0 )

def ot1(pdf):
        pdf.set_xy(10.0,115.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="O.T 01 :", border=0 )

def ot1amount(pdf,ot1):
        pdf.set_xy(70.0,115.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=ot1, border=0 )

def ot1rate(pdf):
        pdf.set_xy(100.0,115.0)
        pdf.set_font('Times','B', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="RATE O.T 01 :", border=0 )

def ot1rateamount(pdf,ot1r):
        pdf.set_xy(130.0,115.0)
        pdf.set_font('Times','U', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=ot1r, border=0 )

def ot1hrs(pdf):
        pdf.set_xy(150.0,115.0)
        pdf.set_font('Times','B', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=" HOURS O.T 01 :", border=0 )

def ot1hrsamount(pdf,ot1h):
        pdf.set_xy(183.0,115.0)
        pdf.set_font('Times','U', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=ot1h, border=0 )

def ot2(pdf):
        pdf.set_xy(10.0,125.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="O.T 02 :", border=0 )

def ot2amount(pdf,ot2):
        pdf.set_xy(70.0,125.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=ot2, border=0 )

def ot2rate(pdf):
        pdf.set_xy(100.0,125.0)
        pdf.set_font('Times','B', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="RATE O.T 02 :", border=0 )

def ot2rateamount(pdf,ot2r):
        pdf.set_xy(130.0,125.0)
        pdf.set_font('Times','U', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=ot2r, border=0 )

def ot2hrs(pdf):
        pdf.set_xy(150.0,125.0)
        pdf.set_font('Times','B', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=" HOURS O.T 02 :", border=0 )

def ot2hrsamount(pdf,ot2h):
        pdf.set_xy(183.0,125.0)
        pdf.set_font('Times','U', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=ot2h, border=0 )






def dayoff(pdf):
        pdf.set_xy(10.0,135.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="DAY OFF/LEAVES :", border=0 )

def dayoffamount(pdf,dayoffamount):
        pdf.set_xy(70.0,135.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=dayoffamount, border=0 )

def dayoffrate(pdf):
        pdf.set_xy(100.0,135.0)
        pdf.set_font('Times','B', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="RATE :", border=0 )

def dayoffrateamount(pdf,dayoofr):
        pdf.set_xy(115.0,135.0)
        pdf.set_font('Times','U', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=dayoofr, border=0 )

def dayoffhrs(pdf):
        pdf.set_xy(150.0,135.0)
        pdf.set_font('Times','B', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=" DAYS :", border=0 )

def dayoffcount(pdf,dayoffcount):
        pdf.set_xy(170.0,135.0)
        pdf.set_font('Times','U', 12,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=dayoffcount, border=0 )












def attendeceallowence(pdf):
        pdf.set_xy(10.0,150.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="ATTENDANCE ALLOWANCE :", border=0 )

def attendeceallowenceamount(pdf,ata):
        pdf.set_xy(100.0,150.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=ata, border=0 )

def attendeceincentice(pdf):
        pdf.set_xy(10.0,160.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="ATTENDANCE INCENTIVE :", border=0 )

def attendeceincentiveamount(pdf,ata):
        pdf.set_xy(100.0,160.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=ata, border=0 )

def grosssalary(pdf):
        pdf.set_xy(10.0,175.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="GROSS SALARY :", border=0 )

def grosssalaryamount(pdf,gs):
        pdf.set_xy(100.0,175.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=gs, border=0 )

def deductions(pdf):
        pdf.set_xy(10.0,185.0)
        pdf.set_font('Times','U', 18,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="DEDUCTIONS ", border=0 )

def epf8(pdf):
        pdf.set_xy(10.0,195.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="EPF 8% :", border=0 )

def epf8amount(pdf,gs):
        pdf.set_xy(100.0,195.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=gs, border=0 )

def salaryadvance(pdf):
        pdf.set_xy(10.0,205.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="SALARY ADVANCE :", border=0 )

def salaryadvanceamount(pdf,gs):
        pdf.set_xy(100.0,205.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=gs, border=0 )

def toatldeduction(pdf):
        pdf.set_xy(10.0,215.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt="TOTAL DEDUCTIONS :", border=0 )

def toatldeductionamount(pdf,gs):
        pdf.set_xy(100.0,215.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=40.0, align='L', txt=gs, border=0 )

def netpay(pdf):
        pdf.set_xy(10.0,260.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.set_fill_color(128, 128, 128)
        pdf.cell(w=190.0, h=10.0, align='L', txt="NET PAY :", border=0, fill = True )

def netpayamount(pdf,gs):
        pdf.set_xy(170.0,260.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.set_fill_color(128, 128, 128)
        pdf.cell(w=190.0, h=10.0, align='L', txt=gs, border=0,  )

def epf12(pdf):
        pdf.set_xy(10.0,240.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=10.0, align='L', txt="E.P.F 12% :", border=0 )

def epf12amount(pdf,gs):
        pdf.set_xy(100.0,240.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=10.0, align='L', txt=gs, border=0 )

def etf3(pdf):
        pdf.set_xy(10.0,250.0)
        pdf.set_font('Times','B', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=10.0, align='L', txt="E.T.F 3% :", border=0 )

def etf3amount(pdf,gs):
        pdf.set_xy(100.0,250.0)
        pdf.set_font('Times','U', 16,)
        pdf.set_text_color(000, 00, 00)
        pdf.cell(w=210.0, h=10.0, align='L', txt=gs, border=0 )




