module Jekyll
  class CatIndex < Page
    def initialize(site, base, dir, cat)
      @site = site
      @base = base
      @dir = dir
      @name = ''
      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'cat_index.html')
      self.data['cat'] = cat
      cat_title_prefix = site.config['cat_title_prefix'] || ''
      cat_title_suffix = site.config['cat_title_suffix'] || ''
      self.data['title'] = "#{cat_title_prefix}#{cat}#{cat_title_suffix}"
    end
  end
  class CatGenerator < Generator
    safe true
    def generate(site)
      if site.layouts.key? 'cat_index'
        dir = site.config['cat_dir'] || 'category'
        site.categories.keys.each do |cat|
          write_tag_index(site, File.join(dir, cat), cat)
        end
      end
    end
    def write_tag_index(site, dir, cat)
      index = CatIndex.new(site, site.source, dir, cat)
      index.render(site.layouts, site.site_payload)
      index.write(site.dest)
      site.pages << index
    end
  end
  	end