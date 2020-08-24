# Installation
Good news: you probably will not need to download anything to use this app, all you need is to 
**have Google Chrome installed**
# Login

You can either login using an @gmail address or using an non @gmail addres (like the one your school gave you)

**Don't worry! We do not have access to your data, it is stored locally in your computer

## Logging in with @gmail address
Open the .bat LoginGoogle and insert your email and password. You won't have to do anything when the new Chrome window launch

## Logging in with non @gmail address
Open the .bat LoginInstitutional and use the browser window that launched to sign in. Then, just close the command prompt

# Bot usage
Affter logging in, open the .bat called scheduler and insert the session link, the start date and the session length

After reaching the start time, a new chrome window will open automatically and the bot will join the meet session for you. After the determined session lenght, it will close the browser and exit the meet session

# For devs:
* The python codes are in the PythonScripts folder
* You will need to download chromedriver and put it in the folder that has the code (or add to PATH)
* The necessary libraries are **selenium** and **pause**
