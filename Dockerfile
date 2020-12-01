FROM python:3.8-slim

LABEL "com.github.actions.name"="Notion2Github"
LABEL "com.github.actions.description"="Automatic syncronization from Notion to Github"
LABEL "repository"="https://github.com/younho9/notion2github"
LABEL "maintainer"="Younho Choo <younho9.choo@gmail.com>"

WORKDIR /usr/src/app

COPY requirements.txt main.py ./
COPY /github/workspace/narkdown.config.json ./narkdown.config.json
RUN ls

RUN ls

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/usr/src/app/main.py"]
