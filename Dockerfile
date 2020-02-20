FROM jekyll/builder:3.8
RUN apk add python3-dev py3-pip openssl-dev
RUN pip3 install scholarly python-slugify
RUN apk add imagemagick
RUN gem install jekyll-minimagick
RUN gem install jekyll-paginate
