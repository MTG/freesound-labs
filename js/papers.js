(function () {
    'use strict';

    var browser = document.getElementById('papers-browser');
    var list = document.getElementById('papers-list');
    var items = Array.from(list.querySelectorAll('.papers-item'));
    items = items.map(function (item, index) {
        return { item: item, index: index };
    }).sort(function (a, b) {
        var dateA = a.item.dataset.sortDate;
        var dateB = b.item.dataset.sortDate;
        return dateA === dateB ? a.index - b.index : (dateA < dateB ? 1 : -1);
    }).map(function (entry) {
        list.appendChild(entry.item);
        return entry.item;
    });
    var search = document.getElementById('papers-search');
    var status = document.getElementById('papers-status');
    var pagination = browser.querySelector('.papers-pagination');
    var pageLabel = document.getElementById('papers-page');
    var previous = document.getElementById('papers-previous');
    var next = document.getElementById('papers-next');
    var pageSize = 20;
    var page = 1;
    function normalize(text) {
        return text.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    }

    var searchable = items.map(function (item) {
        var abstract = item.querySelector('.papers-abstract p');
        return normalize(item.querySelector('.papers-citation').textContent + ' ' +
            (abstract ? abstract.textContent : ''));
    });

    function render() {
        var query = normalize(search.value.trim());
        var terms = query ? query.split(/\s+/) : [];
        var matched = 0;
        var start = (page - 1) * pageSize;

        items.forEach(function (item, index) {
            var matches = terms.every(function (term) {
                return searchable[index].includes(term);
            });
            var visible = matches && matched >= start && matched < start + pageSize;
            item.hidden = !visible;
            var details = item.querySelector('details');
            if (!visible && details) {
                details.open = false;
            }
            if (matches) {
                matched += 1;
            }
        });

        var pages = Math.ceil(matched / pageSize);
        status.textContent = matched === 0
            ? 'No papers found.'
            : 'Showing ' + (start + 1) + '-' + Math.min(start + pageSize, matched) + ' of ' + matched + ' papers.';
        pageLabel.textContent = pages ? 'Page ' + page + ' of ' + pages : 'No pages';
        previous.disabled = page <= 1;
        next.disabled = page >= pages;
        pagination.hidden = pages <= 1;
    }

    search.addEventListener('input', function () {
        page = 1;
        render();
    });
    previous.addEventListener('click', function () {
        page -= 1;
        render();
    });
    next.addEventListener('click', function () {
        page += 1;
        render();
    });

    browser.querySelector('.papers-search').hidden = false;
    status.hidden = false;
    render();
}());
