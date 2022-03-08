# Keyhole
a tool to explore MongoDB deployments

## Relevant Links
- https://github.com/simagix/keyhole
- https://www.mongodb.com/blog/post/peek-at-your-mongodb-clusters-like-a-pro-with-keyhole-part-1
- https://www.mongodb.com/blog/post/peek-at-your-mongodb-clusters-like-a-pro-with-keyhole-part-2
- https://www.mongodb.com/blog/post/peek-your-clusters-like-pro-with-keyhole-part-3

## installation
- Build and Download Keyhole tutorial: https://www.simagix.com/2021/02/build-and-download-keyhole_7.html
- there are a few method to install and use, in this summary I used the Docker image from https://hub.docker.com/r/simagix/keyhole
  - (in Linux terminal) ```docker pull simagix/keyhole```

## using
  - ```docker run --rm -v /homes/idanp/out:/home/simagix/out simagix/keyhole /keyhole --allinfo "mongodb://user:secret@host.local/test?replicaSet=rs"```
  - ```docker run --rm -v /homes/idanp/out:/home/simagix/out simagix/keyhole /keyhole --info "mongodb://user:secret@host.local/test?replicaSet=rs"```

## Maobi
HTML reports generating tool created for Keyhole

### install and start the docker image
- ``docker run -d -p 3030:3030 simagix/maobi```
-  go to ```http://localhost:3030/``` in the browser
