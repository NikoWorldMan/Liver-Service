# Setup for github pages 

-

(Mine egne notater om github pages.)

# Dev stuff

Utviklings prosesen av Github pages: Skriv ned informasjon om det vi har gjort. Skriv spørsmål til informasjonen jeg har. skriv ned informasjon basert på de spørsmåla. Still spørsmål til den nye informasjonen.

# Pycharm mkdocs setup

Pycharm setup

Terminal commands docs.
```markdown
22.11.23
#writing down some terminal commands, so I don't forget how to get mkdocs running.

#In pycharm
pip install mkdocs-material
#Might need to Add on adminastrative privliges: --user

#In Pycharm terminal
mkdocs serve 
#if this don't work use the one below
python -m mkdocs serve

#Add on to mkdocs serve: --dev-addr=0.0.0.0:8000
#insert own value on where and what port to host it on.
```

# Publishing pages


On github
```markdown
#Adding gh-pages to github
#The .github file that has the workflows and ci.yml file needs to be first and on top of the other files.


#Write in ci.yml file to run the (file name) and deploy the file with the docs.
- run: cd (file name) && mkdocs gh-deploy --force

#Pages will only be available on public projects.
#In settings, in pages select the gh-pages and save it.
#From actions the deployment can be monitored, to check the process for faults and it's progress in deploying.
```

