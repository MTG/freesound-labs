FROM jekyll/builder:3.7
RUN gem install jekyll-minimagick
RUN gem install jekyll-paginate
