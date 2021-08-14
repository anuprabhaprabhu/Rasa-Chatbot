from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['new delhi', 'gurgaon', 'noida', 'faridabad', 'allahabad', 'bhubaneshwar', 'mangalore', 'mumbai', 'ranchi', 'patna', 'mysore', 'aurangabad', 'amritsar', 'puducherry', 'varanasi', 'nagpur', 'vadodara', 'dehradun', 'vizag', 'agra', 'ludhiana', 'kanpur', 'lucknow', 'surat', 'kochi', 'indore', 'ahmedabad', 'coimbatore', 'chennai', 'guwahati', 'jaipur', 'hyderabad', 'bangalore', 'nashik', 'pune', 'kolkata','bhopal', 'goa', 'chandigarh', 'ghaziabad', 'ooty', 'gangtok', 'shimla']

list_results = ""

class ActionTier1and2Cities(Action):
	def name(self):
		return 'action_t1t2_city'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		msg = " "
		if (loc.lower() in WeOperate):
			msg = " "
		else:
			msg = "Sorry, we don’t operate in this city. Can you please specify some other location."
			loc = 'None'
		dispatcher.utter_message(msg)
		return [SlotSet('location',loc)]	


def RestaurantSearch(City,Cuisine,Price):
	if Price == 'low':
		min , max =0,299
	elif Price == 'mid':
		min,max=300,699
	else: #Price == 'high'
		min=700
		max = 8000
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))& (ZomatoData['Average Cost for two'].apply(lambda x: (x>min) & (x<max))) ] # & (ZomatoData.sort_values(['Aggregate rating'],axis=0,ascending=False)) ] 
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		global list_results
		list_results=""
		response=""
		inp =""
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
		if results.shape[0] == 0:
			response= "no results"
			list_results= "no results"
		else:
			inp = 'Showing you top rated restaurants:' 
			for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
							
			list_results = response	
		
		dispatcher.utter_message(inp+"-----  \n"+response)
		return [SlotSet('location',loc)]



class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		sender_email = "upgradchatbot2021@gmail.com"
		password = 'upgradpgdml21'
		receiver_email = tracker.get_slot('mail_id')
		message = MIMEMultipart()
		message['From'] = sender_email
		message['To'] = receiver_email
		message['Subject'] = 'Zomato chatbot'
		global list_results
		msg = 'Top rated restaurants : \n'+list_results
		
		message.attach(MIMEText(msg))
		session = smtplib.SMTP('smtp.gmail.com', 587) 
		session.starttls() 
		session.login(sender_email, password) 
		session.sendmail(sender_email, receiver_email, msg)
		session.quit()
		dispatcher.utter_message("sent")
		return [SlotSet('mail_id',receiver_email)]