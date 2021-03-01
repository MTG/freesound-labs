FROM jekyll/builder:3.8
RUN apk add python3-dev py3-pip openssl-dev
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apk add imagemagick
RUN gem install jekyll-minimagick
RUN gem install jekyll-paginate
