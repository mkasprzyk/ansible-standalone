FROM registry.access.redhat.com/rhel7
COPY ./dist/ansible ./dist/ansible-playbook /usr/local/bin/
RUN chmod +x /usr/local/bin/ansible && chmod +x /usr/local/bin/ansible-playbook

CMD ansible --version && ansible-playbook --version

