FROM centos:7
COPY *.spec *.py requirements.txt /build/
WORKDIR /build
RUN yum -y install epel-release && \
    yum -y groupinstall "Development Tools" && \
    yum -y install python-pip python-devel krb5-devel && \
    pip install -r requirements.txt && \
    ln -s $(which ansible) && \
    ln -s $(which ansible-playbook) && \
    pyinstaller ansible.spec && \
    pyinstaller ansible-playbook.spec && \
    cp -fr /build/ansible* /usr/local/bin && \
    chmod +x /usr/local/bin/ansible* 

CMD python -m SimpleHTTPServer
