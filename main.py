from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton,MDRaisedButton
# AND FOR DIALOG IF YOU CLICK DELETE THEN SHOW DIALOG CONFIRM
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar



# CREATE DATA IN YOU DATATABLE FOR FAKE DATA 
data = {
	'1':{"name":"john","age":"25","gender":"male"},
	'2':{"name":"rewr","age":"25","gender":"male"},
	'3':{"name":"grgr","age":"25","gender":"male"},
	'4':{"name":"opoe","age":"25","gender":"male"},
	'5':{"name":"klwq","age":"25","gender":"male"},


}



class MainScreen(Screen):
	"""docstring for MainScreen"""
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)

		self.layout = MDBoxLayout(orientation="vertical",
			padding=20,
			spacing=10
			)
		self.table = MDDataTable(
			size_hint=(1,None),
			# HEIGHT OF YOU TABLE
			height=dp(600),
			# AND ENABLE CHECKBOX IN YOU TABLE
			check=True,
			# AND CREATE COLUMN DATA
			column_data=[
				("No . ",dp(30)),
				("Name . ",dp(30)),
				("Age . ",dp(30)),
				("Gender . ",dp(30)),
			],

			# AND NOW LOOP DATA IN you data for row table
			row_data=[
			(key,data[key]['name'],data[key]['age'],data[key]['gender'])
				for key in data.keys()
			],
			# AND SORT YOU TABLE
			sorted_on="No . ",
			# ASCENDING OR DESCENDING
			sorted_order="ASC"

			)
		# AND NOW ADD YOU TABLE TO self.layout
		# FOR ADD TO APP
		self.layout.add_widget(self.table)
		# AND FOR SCROLL VERTICAL ADD SCROLLVEW
		scroll_view = ScrollView(do_scroll_x=True)
		scroll_view.add_widget(self.layout)

		# AND NOW ADD scroll_view TO YOU ROOT APP
		self.add_widget(scroll_view)

		# AND NOW IF YOU CLICK CHECKBOX IN TABLE 
		# THEN RUN FUNCTION 

		self.table.bind(on_check_press=self.handle_check_press)
		self.you_delete_row = []

		# AND CREATE DELETE BUTTON
		delete_button = MDRaisedButton(
			text="Delete",
			# AND COLOR TO BUTTON 
			md_bg_color="red",
			on_release=self.handle_delete_press
			)
		self.add_widget(delete_button)

	# FUNCTION IF YOU CLICK CHECKBOX
	def handle_check_press(self,instance_table,current_row):
		# GET NUMBER IF YOU SELECTED DATA
		# THIS GET EXAMPLE NUMBER 
		row_data = current_row[0]
		if current_row[-1]:
			self.you_delete_row.append(row_data)
		else:
			# IF YOU UNCHECK THE CHECKBOX THEN REMOVE
			# FROM you_delete_row
			try:
				self.you_delete_row.remove(row_data)
			except ValueError as e:
				print(e)
			else:
				del data[row_data]

		# NOW FOR SEE YOU SELECTED I PRINT THE DATA
		print(len(self.you_delete_row),self.you_delete_row)



	def handle_delete_press(self,instance_button):
		# AND NOW DELETE YOU SELECTED DATA

		if not self.you_delete_row:
			# YOU CAN RUN FUCNTION IF NO DATA SELECTED HERE
			return
		dialog = MDDialog(
			text="Are you sure for delete ?",
			buttons=[
				MDFlatButton(
					text="cancel",
					# CLOSE DIALOG
					on_release=lambda *args:dialog.dismiss()
					),
				MDFlatButton(
					text="Delete",
					# CLOSE DIALOG
					on_release=lambda *args:self.handle_delete_confirm(dialog)
					),

			]

			)
		# AND OPEN DIALOG
		dialog.open()



	def handle_delete_confirm(self,dialog):	
		# THIS FUNCTION WILL DELETE PROCESS
		for row_data in self.you_delete_row:
			del data[row_data]
			# AND FIND AND remove IF FOUND
			if self.table.row_data:
				self.table.row_data = [ row for row in self.table.row_data if row[0] != row_data]
			else:
				self.table.row_data = []

		self.you_delete_row = []

		# AND CLOSE DIALOG 
		dialog.dismiss()

		# AND SHOW SNACKBAR AND SEND MESSAGE SUCCESS DELETE
		Snackbar(
			text="YOu succes remove",
			# POSITION IN TOP 
			pos_hint={"top":1},
			# THIS WILL CREATE SPACE FROM YOU snackbar
			# TO TOP
			snackbar_y="10dp",
			# AND RED BGCOLOR
			bg_color=(1,0,0,1)
			).open()







class MyApp(MDApp):
	def build(self):
		return MainScreen()

if __name__ == "__main__":
	MyApp().run()