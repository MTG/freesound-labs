FROM jekyll/builder:3.8

RUN apk add python3-dev py3-pip openssl-dev imagemagick git

RUN gem install jekyll-minimagick jekyll-paginate

WORKDIR /build

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD build-fslabs.sh .

