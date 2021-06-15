FROM sopelirc/sopel:latest as montagu

COPY requirements.txt .
RUN su-exec sopel pip install --user -r requirements.txt

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "sopel" ]
