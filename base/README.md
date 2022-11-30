
This is used as a base and not meant to be run directly. See the Dockerfile in the root as an example.

To build and tag a new version:

```sh
docker build --platform linux/amd64 -t bgrins/webpage-classifier-base:0.0.1 .
docker push bgrins/webpage-classifier-base:0.0.1
```
