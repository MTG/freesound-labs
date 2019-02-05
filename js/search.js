(function() {
    function displaySearchResults(results, store) {
      var searchResults = document.getElementById('search-results');
      var resultsFound = document.getElementById('resultsFound');
      resultsFound.innerHTML = '';
  
      if (results.length) { // Are there any results?
        resultsFound.innerHTML = `${results.length} results`
        var appendString = '';
  
        for (var i = 0; i < results.length; i++) {  // Iterate over the results
          var item = store[results[i].ref];
          var css_padding_extra = "";
          if (item.image){
            css_padding_extra = "padding-right:15px;";
          }
          var project_url = "";
          if (item.project_url){
            project_url = `<br><span class="post-meta"><a href="${ item.project_url }" target="_blank">${ item.project_url }</a></span>`
          }
          var tags = "";
          for (tag of item.tags.split(', ')){
            tags += `<a href="/tag/${tag}" style="margin-right:5px; color:#828282;">${tag}</a>`
          }
          var post_image = "";
          if (item.image){
              post_image = `
                <td class="thumbnail_cell" style="vertical-align: middle;">
                    <p><img width="300px" src="/assets/thumbnails/${item.image}" alt="${ item.title } thumbnail" style="border-radius:3px;"></p>
                </td>
                `
          }

          appendString += `
            <li> 
            <table>
                <tr>
                <td style="vertical-align: top;${css_padding_extra} max-width:840px;">
                <h2 style="margin-bottom:0px;"><a class="post-link" href="${ item.url }">${ item.title }</a></h2>
                <p>${item.content.split(" ").splice(0, 35).join(" ")}...</p>
                <span class="post-meta">
                    ${tags}
                </span>
                ${project_url}
                </td>
                ${post_image}
                </tr>
            </table>
            </li>
            `
        }
  
        searchResults.innerHTML = appendString;
        
      } else {
        searchResults.innerHTML = '<li>No results found...</li>';
      }
    }
  
    function getQueryVariable(variable) {
      var query = window.location.search.substring(1);
      var vars = query.split('&');
  
      for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
  
        if (pair[0] === variable) {
          return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
        }
      }
    }
  
    var searchTerm = getQueryVariable('query');
  
    if (searchTerm) {
      document.getElementById('search-box').setAttribute("value", searchTerm);
  
      // Initalize lunr with the fields it will be searching on. I've given title
      // a boost of 10 to indicate matches on this field are more important.
      var idx = lunr(function () {
        this.field('id');
        this.field('title', { boost: 10 });
        this.field('authors');
        this.field('tags');
        this.field('content');
        for (var key in window.store) { 
            this.add({
                'id': key,
                'title': window.store[key].title,
                'authors': window.store[key].authors,
                'tags': window.store[key].tags,
                'content': window.store[key].content,
                'image': window.store[key].image,
                'project_url': window.store[key].project_url,
            }); 
        }
      });
  
      var results = idx.search(searchTerm); // Get lunr to perform a search
      displaySearchResults(results, window.store); // We'll write this in the next section
    }
  })();