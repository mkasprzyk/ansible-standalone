FROM registry.access.redhat.com/rhel7
COPY ./dist/ansible /usr/local/bin
RUN chmod +x /usr/local/bin/ansible

CMD ansible --version

