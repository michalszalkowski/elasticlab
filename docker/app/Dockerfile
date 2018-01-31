FROM openjdk:8-jdk-alpine
RUN apk update && apk add bash
VOLUME /tmp
ADD app.jar app.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
EXPOSE 8090