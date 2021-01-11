
try:	
	from tkinter import *
	import os

	root = Tk()
	root.title("Swordwari Money Calculator")
	root.geometry("1930x1100")

	l11 = Label(text="Swordwari Dental Clinic Money Calculator",bg="black",fg="white",font="comicsansms 18 bold",padx=4,pady=4)
	l11.pack()


	# Start Making Variables For Entry Widget

	en1 = StringVar()
	en2 = IntVar()
	en3 = IntVar()
	en4 = IntVar()
	en5 = IntVar()
	en6 = IntVar()
	en7 = IntVar()
	en8 = IntVar()
	en9 = IntVar()
	en10 = IntVar()
	en11 = IntVar()
	en12 = IntVar()
	en13 = IntVar()
	en14 = IntVar()
	en15 = IntVar()
	en16 = IntVar()
	en17 = IntVar()
	en18 = IntVar()
	en19 = IntVar()
	en20 = IntVar()
	en21 = IntVar()
	en22 = IntVar()
	en23 = IntVar()
	en24 = IntVar()
	en25 = IntVar()
	en26 = IntVar()
	en27 = IntVar()
	en28 = IntVar()
	en29 = IntVar()
	en30 = IntVar()
	en31 = IntVar()
	en32 = IntVar()
	en33 = IntVar()
	en34 = IntVar()
	en35 = IntVar()
	en36 = IntVar()
	en37 = IntVar()
	en38 = IntVar()
	en39 = IntVar()

	cus1 = StringVar()
	cus2 = StringVar()
	cus3 = StringVar()
	cus4 = StringVar()
	cus5 = StringVar()
	cus6 = StringVar()
	cus7 = StringVar()
	cus8 = StringVar()
	cus9 = StringVar()
	cus10 = StringVar()
	cus11 = StringVar()

	# Making Frames

	f1 = Frame(borderwidth = 10,bg="black") 
	f2 = Frame(borderwidth = 10,bg="black") 
	f3 = Frame(borderwidth = 10,bg="black") 
	f4 = Frame(borderwidth = 10,bg="black") 
	f5 = Frame(borderwidth = 10,bg="black") 
	f6 = Frame(borderwidth = 10,bg="black") 
	f7 = Frame(borderwidth = 10,bg="black") 
	f8 = Frame(borderwidth = 10,bg="black") 
	f9 = Frame(borderwidth = 10,bg="black") 
	f10 = Frame(borderwidth = 10,bg="black") 
	f11 = Frame(borderwidth = 10,bg="black") 
	f12 = Frame(borderwidth = 10,bg="black") 
	f13 = Frame(borderwidth = 10,bg="black")

	# Making Main Function
	def funcmain():
		for i in range(0,999999999):
			root.update()
			try:
				en4.set((en2.get())-(en3.get()))
				en7.set((en5.get())-(en6.get()))
				en10.set((en8.get())-(en9.get()))
				en13.set((en11.get())-(en12.get()))
				en16.set((en14.get())-(en15.get()))
				en19.set((en17.get())-(en18.get()))
				en22.set((en20.get())-(en21.get()))
				en25.set((en23.get())-(en24.get()))
				en28.set((en26.get())-(en27.get()))
				en31.set((en29.get())-(en30.get()))
				en34.set((en32.get())-(en33.get()))
				b1.config(text=f"Total Earned Amount: RS {(en3.get())+(en6.get())+(en9.get())+(en12.get())+(en15.get())+(en18.get())+(en21.get())+(en24.get())+(en27.get())+(en30.get())+(en33.get())}")
				root.update()
			except:
				pass

	def savingforbackup():
		os.system('mkdir Customer')
		os.system('mkdir TIME')
		os.system('mkdir TAKEN')
		os.system('cls')

		if (cus1.get())=="":
			os.system('del Customer\\customer1.data')
			os.system('cls')
		else:
			f = open('Customer/customer1.data','w+')
			f.write((cus1.get()))
			f.close()

		if (cus2.get())=="":
			os.system('del Customer\\customer2.data')
			os.system('cls')
		else:
			g = open('Customer/customer2.data','w+')
			g.write((cus2.get()))
			g.close()

		if (cus3.get())=="":
			os.system('del Customer\\customer3.data')
			os.system('cls')
		else:
			h = open('Customer/customer3.data','w+')
			h.write((cus3.get()))
			h.close()

		if (cus4.get())=="":
			os.system('del Customer\\customer4.data')
			os.system('cls')
		else:
			i = open('Customer/customer4.data','w+')
			i.write((cus4.get()))
			i.close()

		if (cus5.get())=="":
			os.system('del Customer\\customer5.data')
			os.system('cls')
		else:
			j = open('Customer/customer5.data','w+')
			j.write((cus5.get()))
			j.close()

		if (cus6.get())=="":
			os.system('del Customer\\customer6.data')
			os.system('cls')
		else:
			k = open('Customer/customer6.data','w+')
			k.write((cus6.get()))
			k.close()

		if (cus7.get())=="":
			os.system('del Customer\\customer7.data')
			os.system('cls')
		else:
			l = open('Customer/customer7.data','w+')
			l.write((cus7.get()))
			l.close()

		if (cus8.get())=="":
			os.system('del Customer\\customer8.data')
			os.system('cls')
		else:
			m = open('Customer/customer8.data','w+')
			m.write((cus8.get()))
			m.close()

		if (cus9.get())=="":
			os.system('del Customer\\customer9.data')
			os.system('cls')
		else:
			n = open('Customer/customer9.data','w+')
			n.write((cus9.get()))
			n.close()

		if (cus10.get())=="":
			os.system('del Customer\\customer10.data')
			os.system('cls')
		else:
			o = open('Customer/customer10.data','w+')
			o.write((cus10.get()))
			o.close()

		if (cus11.get())=="":
			os.system('del Customer\\customer11.data')
			os.system('cls')
		else:
			p = open('Customer/customer11.data','w+')
			p.write((cus11.get()))
			p.close()

		if (en2.get())==0:
			pass
		else:
			f = open('TAKEN/second.data','w+')
			f.write(str((en2.get())))
			f.close()

		if (en3.get())==0:
			pass
		else:
			f = open('TAKEN/third.data','w+')
			f.write(str((en3.get())))
			f.close()
		
		if (en5.get())==0:
			pass
		else:
			f = open('TAKEN/fifth.data','w+')
			f.write(str((en5.get())))
			f.close()
			
		if (en6.get())==0:
			pass
		else:
			f = open('TAKEN/sixth.data','w+')
			f.write(str((en6.get())))
			f.close()
			
		if (en8.get())==0:
			pass
		else:
			f = open('TAKEN/eighth.data','w+')
			f.write(str((en8.get())))
			f.close()
			
		if (en9.get())==0:
			pass
		else:
			f = open('TAKEN/ninth.data','w+')
			f.write(str((en9.get())))
			f.close()
			
		if (en11.get())==0:
			pass
		else:
			f = open('TAKEN/eleven.data','w+')
			f.write(str((en11.get())))
			f.close()
			
		if (en12.get())==0:
			pass
		else:
			f = open('TAKEN/twelve.data','w+')
			f.write(str((en12.get())))
			f.close()
			
		if (en14.get())==0:
			pass
		else:
			f = open('TAKEN/fourteen.data','w+')
			f.write(str((en14.get())))
			f.close()
			
		if (en15.get())==0:
			pass
		else:
			f = open('TAKEN/fifteen.data','w+')
			f.write(str((en15.get())))
			f.close()
			
		if (en17.get())==0:
			pass
		else:
			f = open('TAKEN/seventeen.data','w+')
			f.write(str((en17.get())))
			f.close()
			
		if (en18.get())==0:
			pass
		else:
			f = open('TAKEN/eighteen.data','w+')
			f.write(str((en18.get())))
			f.close()
			
		if (en20.get())==0:
			pass
		else:
			f = open('TAKEN/twenty.data','w+')
			f.write(str((en20.get())))
			f.close()
			
		if (en21.get())==0:
			pass
		else:
			f = open('TAKEN/twentyone.data','w+')
			f.write(str((en21.get())))
			f.close()
			
		if (en23.get())==0:
			pass
		else:
			f = open('TAKEN/twentythree.data','w+')
			f.write(str((en23.get())))
			f.close()
			
		if (en24.get())==0:
			pass
		else:
			f = open('TAKEN/twentyfour.data','w+')
			f.write(str((en24.get())))
			f.close()
			
		if (en26.get())==0:
			pass
		else:
			f = open('TAKEN/twentysix.data','w+')
			f.write(str((en26.get())))
			f.close()
			
		if (en27.get())==0:
			pass
		else:
			f = open('TAKEN/twentyseven.data','w+')
			f.write(str((en27.get())))
			f.close()

		if (en29.get())==0:
			pass
		else:
			f = open('TAKEN/twentynine.data','w+')
			f.write(str((en29.get())))
			f.close()

		if (en30.get())==0:
			pass
		else:
			f = open('TAKEN/thirty.data','w+')
			f.write(str((en30.get())))
			f.close()

		if (en32.get())==0:
			pass
		else:
			f = open('TAKEN/thirtytwo.data','w+')
			f.write(str((en32.get())))
			f.close()

		if (en33.get())==0:
			pass
		else:
			f = open('TAKEN/thirtythree.data','w+')
			f.write(str((en33.get())))
			f.close()
		if (en1.get())=="":
			os.system('del TIME\\date.data')
			os.system('cls')
		else:
			f = open('TIME/date.data','w+')
			f.write(en1.get())
			f.close()
	def loadingforbackup():
		try:
			f = open('Customer/customer1.data','r+')
			for words in f:
				break
			cus1.set(words)
			f.close()

			f = open('Customer/customer2.data','r+')
			for words in f:
				break
			cus2.set(words)
			f.close()

			f = open('Customer/customer3.data','r+')
			for words in f:
				break
			cus3.set(words)
			f.close()

			f = open('Customer/customer4.data','r+')
			for words in f:
				break
			cus4.set(words)
			f.close()

			f = open('Customer/customer5.data','r+')
			for words in f:
				break
			cus5.set(words)
			f.close()

			f = open('Customer/customer6.data','r+')
			for words in f:
				break
			cus6.set(words)
			f.close()

			f = open('Customer/customer7.data','r+')
			for words in f:
				break
			cus7.set(words)
			f.close()

			f = open('Customer/customer8.data','r+')
			for words in f:
				break
			cus8.set(words)
			f.close()

			f = open('Customer/customer9.data','r+')
			for words in f:
				break
			cus9.set(words)
			f.close()

			f = open('Customer/customer10.data','r+')
			for words in f:
				break
			cus10.set(words)
			f.close()

			f = open('Customer/customer11.data','r+')
			for words in f:
				break
			cus11.set(words)
			f.close()


			f = open('Customer/customer12.data','r+')
			for words in f:
				break
			cus12.set(words)
			f.close()
			
		except:
			pass
	def loadingfornextbackup():
		try:
			f = open('TIME/date.data','r+')
			for words in f:
				break
			en1.set(words)
			f.close()

			f = open('TAKEN/second.data','r+')
			for words in f:
				break
			en2.set(words)
			f.close()

			f = open('TAKEN/third.data','r+')
			for words in f:
				break
			en3.set(words)
			f.close()
			
			f = open('TAKEN/fifth.data','r+')
			for words in f:
				break
			en5.set(words)
			f.close()
			
			f = open('TAKEN/sixth.data','r+')
			for words in f:
				break
			en6.set(words)
			f.close()
			
			f = open('TAKEN/eighth.data','r+')
			for words in f:
				break
			en8.set(words)
			f.close()
			
			f = open('TAKEN/ninth.data','r+')
			for words in f:
				break
			en9.set(words)
			f.close()
			
			f = open('TAKEN/eleven.data','r+')
			for words in f:
				break
			en11.set(words)
			f.close()
			
			f = open('TAKEN/twelve.data','r+')
			for words in f:
				break
			en12.set(words)
			f.close()
			
			f = open('TAKEN/fourteen.data','r+')
			for words in f:
				break
			en14.set(words)
			f.close()
			
			f = open('TAKEN/fifteen.data','r+')
			for words in f:
				break
			en15.set(words)
			f.close()
			
			f = open('TAKEN/seventeen.data','r+')
			for words in f:
				break
			en17.set(words)
			f.close()
			
			f = open('TAKEN/eighteen.data','r+')
			for words in f:
				break
			en18.set(words)
			f.close()
			
			f = open('TAKEN/twenty.data','r+')
			for words in f:
				break
			en20.set(words)
			f.close()
			
			f = open('TAKEN/twentyone.data','r+')
			for words in f:
				break
			en21.set(words)
			f.close()
			
			f = open('TAKEN/twentythree.data','r+')
			for words in f:
				break
			en23.set(words)
			f.close()
			
			f = open('TAKEN/twentyfour.data','r+')
			for words in f:
				break
			en24.set(words)
			f.close()
			
			f = open('TAKEN/twentysix.data','r+')
			for words in f:
				break
			en26.set(words)
			f.close()
			
			f = open('TAKEN/twentyseven.data','r+')
			for words in f:
				break
			en27.set(words)
			f.close()

			f = open('TAKEN/twentynine.data','r+')
			for words in f:
				break
			en29.set(words)
			f.close()

			f = open('TAKEN/thirty.data','r+')
			for words in f:
				break
			en30.set(words)
			f.close()

			f = open('TAKEN/thirtytwo.data','r+')
			for words in f:
				break
			en32.set(words)
			f.close()

			f = open('TAKEN/thirtythree.data','r+')
			for words in f:
				break
			en33.set(words)
			f.close()
		except:
			pass

	Label(f1,text="Date: ",bg="black",fg="white",font="comicsansms 12 italic").pack(side=LEFT)
	Entry(f1,textvariable=en1,bg="white",fg="black",font="comicsansms 12 bold").pack(side=LEFT)

	Label(f2, text="Customer's Name               ",bg="black",fg="white",font="comicsansms 12 italic").pack(side=LEFT)
	Label(f2, text="Amount Customer Gave You               ",bg="black",fg="white",font="comicsansms 12 italic").pack(side=LEFT)
	Label(f2, text="Actual Amount          ",bg="black",fg="white",font="comicsansms 12 italic").pack(side=LEFT)
	Label(f2, text="    Money To Return",bg="black",fg="white",font="comicsansms 12 italic").pack(side=LEFT)

	Entry(f3,textvariable=cus1,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f3,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f3,textvariable=en2,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f3,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f3,textvariable=en3,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f3,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f3,textvariable=en4,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f4,textvariable=cus2,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f4,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f4,textvariable=en5,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f4,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f4,textvariable=en6,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f4,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f4,textvariable=en7,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f5,textvariable=cus3,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f5,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f5,textvariable=en8,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f5,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f5,textvariable=en9,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f5,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f5,textvariable=en10,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f6,textvariable=cus4,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f6,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f6,textvariable=en11,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f6,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f6,textvariable=en12,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f6,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f6,textvariable=en13,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f7,textvariable=cus5,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f7,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f7,textvariable=en14,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f7,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f7,textvariable=en15,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f7,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f7,textvariable=en16,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f8,textvariable=cus6,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f8,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f8,textvariable=en17,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f8,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f8,textvariable=en18,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f8,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f8,textvariable=en19,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f9,textvariable=cus7,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f9,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f9,textvariable=en20,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f9,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f9,textvariable=en21,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f9,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f9,textvariable=en22,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f10,textvariable=cus8,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f10,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f10,textvariable=en23,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f10,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f10,textvariable=en24,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f10,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f10,textvariable=en25,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f11,textvariable=cus9,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f11,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f11,textvariable=en26,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f11,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f11,textvariable=en27,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f11,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f11,textvariable=en28,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	Entry(f12,textvariable=cus10,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f12,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f12,textvariable=en29,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f12,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f12,textvariable=en30,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f12,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f12,textvariable=en31,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)
	Label(f12,text="    ",bg="black").pack(side=LEFT)
	b1 = Button(f12,text=f"Total Earned Amount: {0}",bg="black",fg="white",font="comicsansms 14 italic",state=DISABLED,pady=30,padx=30)
	b1.pack(side=LEFT)

	Entry(f13,textvariable=cus11,bg="white",fg="black",font="comicsansms 12 bold",width=21).pack(side=LEFT)
	Label(f13,text="              RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f13,textvariable=en32,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f13,text="                                    RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f13,textvariable=en33,bg="white",fg="black",font="comicsansms 12 bold",width=5).pack(side=LEFT)
	Label(f13,text="                       RS",bg="black",fg="white",font="12").pack(side=LEFT)
	Entry(f13,textvariable=en34,bg="white",fg="black",font="comicsansms 12 bold",width=5,state=DISABLED).pack(side=LEFT)

	# Packing Frames
	f1.pack(anchor="w")
	f2.pack(anchor="w")
	f3.pack(anchor="w")
	f4.pack(anchor="w")
	f5.pack(anchor="w")
	f6.pack(anchor="w")
	f7.pack(anchor="w")
	f8.pack(anchor="w")
	f9.pack(anchor="w")
	f10.pack(anchor="w")
	f11.pack(anchor="w")
	f12.pack(anchor="w")
	f13.pack(anchor="w")

	root.config(bg="black")

	loadingforbackup()
	loadingfornextbackup()
	funcmain()
	root.mainloop()
except:
	savingforbackup()
	quit()