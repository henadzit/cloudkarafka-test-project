A small Docker image that reproduces https://github.com/CloudKarafka/python-kafka-example/issues/3.

```
docker build -t cloudkarafka-test-project:latest .
docker run -e CLOUDKARAFKA_BROKERS='' -e CLOUDKARAFKA_TOPIC='' -e CLOUDKARAFKA_USERNAME='' -e CLOUDKARAFKA_PASSWORD='' cloudkarafka-test-project:latest
```
