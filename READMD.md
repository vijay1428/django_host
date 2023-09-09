# Continuously Deploying Django to AWS EC2 with Docker and GitLab

Configure GitLab CI to continuously deploy a Django and Docker application to AWS EC2.

## Want to learn how to build this?

Check out the [tutorial](https://testdriven.io/blog/deploying-django-to-ec2-with-docker-and-gitlab/).

## Want to use this project?

### Development

Run locally:

```sh
$ docker-compose up -d --build
```

Verify [http://localhost:8000/](http://localhost:8000/) works as expected:

```json
{
  "hello": "world"
}
```

### CI and Production

See the [tutorial](https://testdriven.io/blog/deploying-django-to-ec2-with-docker-and-gitlab/).
