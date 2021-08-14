## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [low](price)
- [mid](price)
- [high](price)
- book a table in [ooty](location)
- [Mexican](cuisine)
- book in [delhi](location)
- find in [delhi](location)
- book me a table in [delhi](location)
- book a table in [delhi](location)
- [xyz@gmail.com](mail_id)
- [More than Rs. 700](price)
- [thai](cuisine) in [delhi](location)
- [abc23@yahoo.com](mail_id)
- [rgeg23@abc.com](mail_id)
- {"entity": "mail_id", "value":"^[a-zA-Z0-9]+@[a-zA-Z0-9]+/.[a-zA-Z]+$"]
- book in [bombay]{"entity": "location", "value": " Mumbai"}
- [chinese](cuisine) in [pune](location)
- [nandhanaprabu@gmail.com](mail_id)
- book in [delhi]{"entity": "location", "value": "New Delhi"}
- book in [ooty](location)
- [anuprabhaprabhu09@gmail.com](mail_id)
- book in [delhi]{"entity": "location", "value": "New Delhi"}
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [mid](price)
- [apple25@gmail.com](mail_id)

## synonym: Mumbai
- bombay
- Bombay
- Bambai
- mubaim

## synonym: high
- costly

## synonym: low
- cheap

## synonym: mid
- moderate

## synonym:4
- four

## synonym:Chinese
- chines

## synonym:Delhi
- New Delhi

## synonym:Italian
- itali

## synonym:Mexican
- mexico
- mexicana

## synonym:New Delhi
- delhi
- dilli
- nayi dilli
- newdelhi

## synonym:North Indian
- indian
- north india
- mughlai

## synonym:ahmedabad
- amadavad

## synonym:allahabad
- prayag

## synonym:bangalore
- Bengaluru
- bangloro
- bangaluru
- bengalor

## synonym:chennai
- channa
- madras

## synonym:chinese
- Chinese
- Chines

## synonym:coimbatore
- kovai

## synonym:dehradun
- dehra dun

## synonym:gurgaon
- gurugram

## synonym:kolkata
- calcutta
- kolkota
- kolkatta

## synonym:mangalore
- mangaluru
- manguluru

## synonym:palakkad
- palghat

## synonym:pondicherry
- puducherry
- pondy

## synonym:pune
- poona

## synonym:thiruchirappalli
- trichy

## synonym:thiruvananthapuram
- trivandrum

## synonym:varanasi
- kashi
- banaras
- benares

## synonym:vegetarian
- veggie
- vegg

## synonym:visakhapatnam
- vizag
- waltair

## regex:greet
- hey[^\s]*

## regex:mail_id
- [^[a-zA-Z0-9]+@[a-zA-Z0-9]+/.[a-zA-Z]+$]

## regex:pincode
- [0-9]{6}
