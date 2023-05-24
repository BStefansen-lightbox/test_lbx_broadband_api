## Getting Started

```
docker image pull mcr.microsoft.com/mssql/server:2017-latest


docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<YourStrong@Passw0rd>" -p 1433:1433 --name mssql --hostname mssql -d mcr.microsoft.com/mssql/server:2017-latest


pipenv install


pipenv shell


cd lbx_broadband_api/


python manage.py runserver
```