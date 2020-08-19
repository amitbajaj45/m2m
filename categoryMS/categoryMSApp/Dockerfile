FROM maven:3.5-jdk-8 AS build

# set the working directory
WORKDIR /usr/src/app

# copy just the pom.xml
COPY ./app/pom.xml /usr/src/app/pom.xml

# just install the dependencies for caching
RUN mvn -T 4C -T 4 dependency:go-offline

# copy the application code
COPY ./app /usr/src/app

# package the application
RUN mvn package -T 4C -T 2 -Dmaven.test.skip=true

# create our Wildfly based application server
FROM jboss/wildfly:11.0.0.Final AS application

# install postgresql support
RUN mkdir -p $JBOSS_HOME/modules/system/layers/base/org/postgresql/main
COPY ./postgresql $JBOSS_HOME/modules/system/layers/base/org/postgresql/main
RUN /bin/sh -c '$JBOSS_HOME/bin/standalone.sh &' \
	&& sleep 10 \
	&& $JBOSS_HOME/bin/jboss-cli.sh --connect --command="/subsystem=datasources/jdbc-driver=postgresql:add(driver-name=postgresql,driver-module-name=org.postgresql, driver-class-name=org.postgresql.Driver)" \
	&& $JBOSS_HOME/bin/jboss-cli.sh --connect --command=:shutdown \
	&& rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history/ \
	&& rm -rf $JBOSS_HOME/standalone/log/*

#RUN /bin/sh -c '$JBOSS_HOME/bin/standalone.sh &' \
#	&& sleep 10 \
#	&& rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history/ \
#	&& rm -rf $JBOSS_HOME/standalone/log/*

# copy and deploy the war file from build layer to application layer
COPY --from=build /usr/src/app/target/categoryMicroService.war /opt/jboss/wildfly/standalone/deployments/categoryMicroService.war

# copy our configuration
COPY ./standalone.xml /opt/jboss/wildfly/standalone/configuration/standalone.xml

# install nc for entrypoint script and copy the entrypoint script
USER root
RUN yum install nc -y
USER jboss
COPY ./docker-entrypoint.sh /opt/jboss/docker-entrypoint.sh

# expose the application port and the management port
EXPOSE 8080 9990

ENV DB_URL jdbc:postgresql://categoryMicroDBELB-521e8572997f3ec3.elb.us-east-1.amazonaws.com:5432/categoryMS?ApplicationName=categoryMicroService
ENV DB_HOST categoryMicroDBELB-521e8572997f3ec3.elb.us-east-1.amazonaws.com
ENV DB_PORT 5432
ENV DB_NAME categoryMS
ENV DB_USER admin
ENV DB_PASS password

# run the application
ENTRYPOINT [ "/opt/jboss/docker-entrypoint.sh" ]
CMD [ "-b", "0.0.0.0", "-bmanagement", "0.0.0.0" ]
