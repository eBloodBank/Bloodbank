<h1><center>Blood Bank Management System</center></h1>

<center>Django Rest Project</center>

<center><b>Group ID - 28</b></center>

Youtube Demo - https://www.youtube.com/watch?v=X9x91hKCtHU

# Group 28 Members
 1. **Utkarsh Aditya** (Roll No: S20180010182) 

 2. **Vipul Rawat** (Roll No: S20180010192) 

 3. **Pradum Singh** (Roll No: S20180010136)

 4. **Sumanth Bhat** (Roll No: S20180010171)

 5. **Sushant Bondle** (Roll No: S20180010030)

    

 # Problem 

​		In today’s world, general society can only know about the blood donation events through ordinary media means such as radio, news paper or television advertisements. Any of the portals provide with very less or no information about the blood donation events on their respective portal.	

​		The current system that is utilized by the blood bank is manual system. With the manual system, there are issues in managing the donors' records. The records of the donor probably won't be kept securely and there may be cases where the donor's records go missing because of human mistake or debacles. Other than that, blunders may happen when the staff saves more than one record for a similar donor.

​		There is no centralized database of volunteer donors. Along these lines, it turns out to be truly dreary for an individual to search blood if there should be an occurrence of crisis. The only choice he has is to manually look up the register and match the donors individually and call them. 

​		There is likewise no centralized database used to keep the donors' records. Each bank is having their own records of donors. On the off  chance that a donor makes donation in various emergency clinic, no past records can be followed aside from if the donor brings along the donation certificate. Henceforth, the donor is thought of to be a newbie in the event that they make blood donation in another place. 

​		Without a computerized administration system, there are additionally issues in monitoring the genuine measure of every single blood type in the blood bank. Likewise, there is additionally no alert accessible when the blood amount is underneath its standard level or when the blood in the bank has expired.

 # Overview of project

​		Our project is an initiative to connect, digitize and streamline the work flow of blood banks across India. The purpose of the blood bank management system is to simplify and automate the process of searching for blood in case of emergency and maintain the records of blood donors, recipients, blood donation programs and blood stocks in the bank.

## Structure

### Django
*Frontend*

- Home, About and other Informational Pages
- User Module(Register, Login and Logout)
- Docs Page(2 Variations)
- Search Pages 
- List View for other modules

*Backend* 

- User Module
- Blood Bank Module, Blood Packets Module, Blood Donation Event Module and Donation Request Module
- Search Features
- Orders Module
- Database : PostgreSQL

*Testing* 

- Models, views and URLs 
- API Views testing
- Django debug toolbar

*Documentation* 

-  Swagger 
- General Documentation

*Deployment*

- nginx

*Mock Application*

- Django 

### Services Consumed    

- **Facebook** : The users would be provided with the option to share their actions on social media. A donor can share and inspire other people to donate blood by sharing on social media. Other users can like, share and comment too.
- **Paypal** : The users would be provided with an online payment gateway such that any user looking for blood packet could search across the local blood banks on our website and if found, he can buy it online and collect the blood sample from the              respective blood bank. We are using Paypal since it has user friendly documentation and easy to implement service           along with most of the features.

### APIs Exposed 
- **CRUD for Donor :** A service end point to provide list of all registered donors who have donated to any of the registered blood banks. A user can filter the list of donors by providing a city name, which would return list of blood donors in that specific city.     
- **CRUD for Blood Bank and Blood Packets :** A service end point to provide list of all available registered blood banks along with its complete inventory information. A user can filter the list of blood banks by providing a city name, which would return list of blood banks in that specific city. 
- **CRUD for Blood Donation Event :**  A service end point to provide list of all the registered blood events on the website with all their respective details.
- **City wise Donors** : City Filtered list of blood banks
- **City wise Blood Banks** : City Filtered list of blood banks


For more information regarding the project refer the group 28 artifacts folder.



