$(document).ready(function(){
    $('.search-btn').on( 'click',  function(e){
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/?search_filter='+ searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(function(d) {
                    var itemImagesHtml = '';
                    for (var i = 0; i < d.itemimages.length; i++) {
                        if (d.itemimages[i].item === d.item) {
                            itemImagesHtml += '<div class="image_container">' +
                                '<img src="' + d.itemimages[i].img_url + '" width="200px" height="200px" alt="Image of ' + d.name + '"/>' +
                                '</div>';
                        }
                    }
                    var itemPrice = (d.price === null) ? '0' : d.price;
                    return '<div class="well item">' +
                        '<a href="/items/' + d.id + '">' +
                        '<div class="item_content" id="single_item_image">' +
                        itemImagesHtml +
                        '</div>' +
                        '<div class="item_information">Category: ' + d.category + '</div>' +
                        '<div class="item_information">Condition: ' + d.condition + '</div>' +
                        '<div class="item_information">Location: ' + d.location + '</div>' +
                        '<div class="item_content" id="price">Starting price: $' +
                        itemPrice +
                        '</div>' +
                        '</a>' +
                        '</div>';
                });
                $('.all_items').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error){
                //TODO: SHOW toastr
                console.error(error)
            }
        })

    });
});