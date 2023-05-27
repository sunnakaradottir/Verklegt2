$(document).ready(function(){
    $('#search-btn').on( 'click',  function(e){
        e.preventDefault();
        var searchText = $('#search-box').val();
        console.log(searchText)
        $.ajax({
            url: '?search_filter='+ searchText,
            type: 'GET',
            success: function(resp) {
                console.log(resp.data)
                 var newHtml = resp.data.map(d => {
                     var itemImagesHtml = '';
                    {% for itemimage in itemimages %}
                        {% if itemimage.item == item %}
                            itemImagesHtml += '<div class="image_container">' +
                                '<img src="' + '{{ itemimage.img_url }}' + '" width="200px" height="200px" alt="Image of ' + '{{ item.name }}' + '"/>' +
                                '</div>';
                        {% endif %}
                    {% endfor %}

                    return `<div class="item_content">
                            <a href="/${d.id}">
                            ${itemImagesHtml}
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                            </a>
                            </div>`;
                });
                $('.single_item').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error){
                //TODO: SHOW toastr
                console.error(error)
            }
        })

    });
});