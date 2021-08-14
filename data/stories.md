## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{ "location": "pune"}
    - slot{"location": "pune"}
    - action_t1t2_city
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "mnop@gmail.com"}
    - slot{"mail_id": "mnop@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "mnop@gmail.com"}
    - utter_goodbye
    

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export

## complete path 5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"cuisine": "chinese", "location": "pune"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - action_t1t2_city
    - slot{"location": "pune"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "mnop@gmail.com"}
    - slot{"mail_id": "mnop@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "mnop@gmail.com"}


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_Price
* restaurant_search{"price": "More than Rs. 700"}
    - slot{"price": "More than Rs. 700"}
    - action_search_restaurants

* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_Price
* restaurant_search{"price": "More than Rs. 700"}
    - slot{"price": "More than Rs. 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - utter_greet

* greet
    - utter_greet
* restaurant_search{"cuisine": "thai", "location": "delhi"}
    - slot{"cuisine": "thai"}
    - slot{"location": "delhi"}
    - utter_ask_Price
* restaurant_search{"price": "More than Rs. 700"}
    - slot{"price": "More than Rs. 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mailid
* email{"mail_id": "abcd@gmail.com"}
    - slot{"mail_id": "abcd@gmail.com"}
    - action_send_mail

* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "700"}
    - slot{"price": "700"}

* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_Price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_location
* restaurant_search{"cuisine": "thai", "location": "chennai"}
    - slot{"cuisine": "thai"}
    - slot{"location": "chennai"}
    - utter_ask_Price
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - utter_ask_Price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_Price
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - action_search_restaurants
    - slot{"location": "chennai"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz@gmail.com"}
    - slot{"mail_id": "xyz@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz@gmail.com"}
    - utter_goodbye
    - utter_greet

* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "ooty"}

* restaurant_search{"cuisine": "thai", "location": "mumbai"}
    - slot{"cuisine": "thai"}
    - slot{"location": "mumbai"}
    - action_t1t2_city
    - slot{"location": "mumbai"}
    - utter_ask_Price
* greet
    - utter_ask_Price
    - utter_ask_Price
* restaurant_search

* restaurant_search{"cuisine": "thai", "location": "New Delhi"}
    - slot{"cuisine": "thai"}
    - slot{"location": "New Delhi"}
    - action_t1t2_city
    - slot{"location": "New Delhi"}
    - utter_ask_Price
* restaurant_search

* restaurant_search{"cuisine": "thai", "location": "New Delhi"}
    - slot{"cuisine": "thai"}
    - slot{"location": "New Delhi"}
    - action_t1t2_city
    - slot{"location": "New Delhi"}
    - utter_ask_Price
* restaurant_search

* restaurant_search{"cuisine": "chinese", "location": "pune"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - action_t1t2_city
    - slot{"location": "pune"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "mnop@gmail.com"}
    - slot{"mail_id": "mnop@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "mnop@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz@gmail.com"}
    - slot{"mail_id": "xyz@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz@gmail.com"}
    - slot{"mail_id": "xyz@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "axyz9@gmail.com"}
    - slot{"mail_id": "axyz9@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "axyz9@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz09@gmail.com"}
    - slot{"mail_id": "xyz09@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz09@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "axyz@gmail.com"}
    - slot{"mail_id": "axyz9@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "axyz@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "anxyz9@gmail.com"}
    - slot{"mail_id": "anxyz9@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "anxyz9@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "axyz9@gmail.com"}
    - slot{"mail_id": "axyz9@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "axyz9@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz09@gmail.com"}
    - slot{"mail_id": "xyz09@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz09@gmail.com"}

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz09@gmail.com"}
    - slot{"mail_id": "xyz09@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz09@gmail.com"}


* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz09@gmail.com"}
    - slot{"mail_id": "xyz09@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz09@gmail.com"}


* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz09@gmail.com"}
    - slot{"mail_id": "xyz09@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz09@gmail.com"}
    - utter_goodbye

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "xyz09@gmail.com"}
    - slot{"mail_id": "xyz09@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "axyz09@gmail.com"}
    - utter_goodbye

* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "axyz9@gmail.com"}
    - slot{"mail_id": "axyz9@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "axyz9@gmail.com"}
    - utter_goodbye


* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_t1t2_city
    - slot{"location": "ooty"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "ooty"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "axyz9@gmail.com"}
    - slot{"mail_id": "axyz9@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "axyz9@gmail.com"}

* greet
    - utter_greet
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_t1t2_city
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_Price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - utter_ask_mailid
* restaurant_search{"mail_id": "apple25@gmail.com"}
    - slot{"mail_id": "apple25@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "apple25@gmail.com"}
    - utter_goodbye
    - action_restart
