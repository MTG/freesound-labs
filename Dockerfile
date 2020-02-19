FROM jekyll/builder:3.7
RUN mkdir /gem
ADD . /gem
WORKDIR /gem
USER root
RUN bundle install 
