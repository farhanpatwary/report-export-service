# Setup
1. Create Virtual Environment by running: `python3.6 -m venv env` from the root directory of the project.        
2. Install dependencies using `pip install -r requirements.txt` also from root directory of project.   
3. Create .env file in the root directory of the project as such:
```
UNAME=
PWORD=
```   
Where UNAME is the PostgreSQL database username and PWORD is the password   

Once you have installed all the dependencies and created the `.env` file you should be able to run:   
1. `source env/bin/activate` to activate the virtual environment.       
2. `python app.py` to start the app.       

# Usage
To get a report, send a HTTP GET request to `/<id>/<type>` where `<id>` is the report id and `<type>` is the type of report you want.      
Available IDs: 1,2,4    
Available types: pdf, xml    
# About
I have spent around 3 hours on this task including testing. Since I was under strict time conditions, I focused on creating the minimum viable product, so I focused on making the service work.    
I implemented some testing using pytest towards the end of the task. This is when I realized my mistake of naming the project using hyphens instead of underscores, which made exporting modules to be used in tests quite difficult.   
If I was to start the project again I would start with a name with no hyphens so that my tests can be in their own folder. I thought this was okay since my main focus was getting the application to work.
