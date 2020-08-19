
FROM ubuntu:18.04
#FROM library/postgres
ENV POSTGRES_DB productms
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD passwOrd

RUN apt update -y
RUN apt install sudo -y
RUN sudo apt install postgresql postgresql-contrib -y
RUN sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" /etc/postgresql/10/main/postgresql.conf
RUN sudo su -c 'echo -e "\nhost\tall\t\tall\t\t0.0.0.0/0\t\tmd5" >> /etc/postgresql/10/main/pg_hba.conf'
RUN sudo groupadd -r ${POSTGRES_USER}
RUN sudo useradd -r -g ${POSTGRES_USER} -d /opt/${POSTGRES_USER} -s /sbin/nologin ${POSTGRES_USER}
USER postgres
RUN  /etc/init.d/postgresql start &&\
    psql --command "CREATE DATABASE ${POSTGRES_DB};" &&\
    psql --command "Create user ${POSTGRES_USER} with encrypted password '${POSTGRES_PASSWORD}';" &&\
    psql --command "GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_USER};"
RUN  /etc/init.d/postgresql restart
EXPOSE 5432
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/10/main", "-c", "config_file=/etc/postgresql/10/main/postgresql.conf"]


#RUN apt update -y
#ENV DEBIAN_FRONTEND=noninteractive
#RUN apt install vim -y
#RUN apt install sudo -y
#RUN adduser --disabled-password --gecos '' ${POSTGRES_USER}
#RUN adduser ${POSTGRES_USER} sudo
#RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
#RUN apt update -y
#RUN apt install postgresql-12 postgresql-contrib-12 -y
#USER ${POSTGRES_USER}
#RUN sleep 10
#RUN  sudo /etc/init.d/postgresql start &&\
#    psql --command "CREATE USER ${POSTGRES_USER} WITH SUPERUSER PASSWORD '${POSTGRES_PASSWORD}';" &&\
#    createdb -O ${POSTGRES_USER} ${POSTGRES_DB}
#RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/12/main/pg_hba.conf
#RUN echo "listen_addresses='*'" >> /etc/postgresql/12/main/postgresql.conf
##RUN echo "local   all             postgres                                peer"
#EXPOSE 5432
#VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
#CMD ["/usr/lib/postgresql/12/bin/postgres", "-D", "/var/lib/postgresql/12/main", "-c", "config_file=/etc/postgresql/12/main/postgresql.conf"]
