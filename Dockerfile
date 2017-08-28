FROM centos:7
COPY *.spec *.py requirements.txt /build/
WORKDIR /build
RUN yum -y install epel-release && \
    yum -y groupinstall "Development Tools" && \
    yum -y install python-pip python-devel && \
    pip install -r requirements.txt && \
    pyinstaller ansible.spec && \
    pyinstaller ansible-playbook.spec && \
    cp -fr /build/ansible* /usr/local/bin && \
    chmod +x /usr/local/bin/ansible* 

CMD python -m SimpleHTTPServer
